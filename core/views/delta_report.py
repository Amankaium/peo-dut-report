from datetime import datetime
import calendar
import locale
from openpyxl import load_workbook
from django.views import View
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from core.serializers import *
from core.models import DeltaReport, MonthReport
import requests


locale.setlocale(locale.LC_TIME, 'ru_RU')
month_names = [month for month in calendar.month_name]


class DeltaReportAddView(CreateView):
    model = MonthReport
    fields = ['month', 'year']
    template_name = "core/delta_reports_add.html"

    def post(self, request):
        context = {}

        excel_file = request.FILES["excel_file"]
        new_excel_source = ExcelSource.objects.create(
            excel_file=excel_file,
            created_by=request.user
        )
        messages.success(request, "Файл добавлен")

        try:
            new_month_report = MonthReport.objects.create(
                source=new_excel_source,
                month=request.POST["month"],
                year=request.POST["year"]
            )
        except:
            return HttpResponse(f"Ошибка! Такой отчёт уже существует")
            
        messages.success(request, f"Создан {new_month_report}")

        excel_file_source = load_workbook('media/' + new_excel_source.excel_file.name)
        page = excel_file_source["Проверка ПЭО"]
        delta_reports_to_create = []

        for row in page:
            if row[0].row == 1:
                continue

            car_name = row[1].value

            if car_name == "нет ДУТ":
                continue
            if car_name is None or car_name in ['', ' ']:
                break

            month_names.index("Июль")

            date_format = "%Y %B %d %H:%M"
            period_start = datetime.strptime(row[2].value, date_format)
            period_end = datetime.strptime(row[3].value, date_format)

            fact_km = row[4].value
            start_balance = row[7].value
            fueling_gsm = row[9].value
            actual_fuel_consumption = row[11].value
            norm_fuel_consumption = row[12].value
            departure = row[13].value
            actual = row[16].value
            fuel_calculation_norm = row[17].value
            departure_balance = row[18].value
            end_balance = row[19].value
            end_mech_balance = row[21].value
            difference = row[22].value
            deficiency = row[23].value
            note = row[25].value

            car_object, car_created = Transport.objects.get_or_create(
                name=car_name
            )

            new_delta_report = DeltaReport(
                month_report=new_month_report,
                transport=car_object,
                vehicle_name=car_name,
                period_start=period_start,
                period_end=period_end,
                fact_km=fact_km,
                start_balance=start_balance,
                fueling_gsm=fueling_gsm,
                actual_fuel_consumption=actual_fuel_consumption,
                norm_fuel_consumption=norm_fuel_consumption,
                departure=departure,
                actual=actual,
                fuel_calculation_norm=fuel_calculation_norm,
                departure_balance=departure_balance,
                end_balance=end_balance,
                end_mech_balance=end_mech_balance,
                difference=difference,
                deficiency=deficiency,
                note=note,
            )
            delta_reports_to_create.append(new_delta_report)
        DeltaReport.objects.bulk_create(delta_reports_to_create)
           
        messages.success(request, f"Добавлен отчёт об отклонениях")
        return redirect('home')


class DeltaReportUpdateView(View):
    template_name = 'core/delta_reports_update.html'

    def get_context(self):
        month_reports = MonthReport.objects.all()
        # q = len(month_reports)
        # if q > 3:
        #     month_reports = month_reports[q-3:]
        month_report = MonthReport.objects.get(id=self.kwargs["id"])
        delta_reports = DeltaReport.objects.filter(month_report=month_report)
        context = {
            "month_reports": month_reports,
            "month_report": month_report,
            "delta_reports": delta_reports,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        sid = "f55c3c5ba189e0330b91ffe2bd20f71d"

        car_numbers = ["Daf 01KG 1694M", "Daf 01KG 900AD"]
        delta_reports = DeltaReport.objects.filter(transport__name__in=car_numbers, month_report=context["month_report"])
        print(len(delta_reports))
        for obj in context["delta_reports"][:2]:
        # for obj in delta_reports:
            period_start = int(obj.period_start.timestamp())
            period_end = int(obj.period_end.timestamp())
            id_realcom = obj.transport.id_realcom

            response = requests.post(
                url=f'http://wialon.realcom.kg/wialon/ajax.html?svc=report/exec_report&sid={sid}',
                data={
                    "sid": sid,
                    "params": '{"reportResourceId":6354,"reportTemplateId":1,"reportTemplate":null,"reportObjectId":%s,"reportObjectSecId":0,"interval":{"flags":16777216,"from":%s,"to":%s},"remoteExec":0}' % (id_realcom, period_start, period_end)
                }
            )
            data = response.json()
            odometer_mileage = data["reportResult"]["stats"][6][1].split()[0]
            trip_mileage = data["reportResult"]["stats"][7][1].split()[0]
            start_level = data["reportResult"]["stats"][16][1].split()[0]
            total_refueled = data["reportResult"]["stats"][19][1].split()[0]
            avg_trip_dut_consumption = data["reportResult"]["stats"][14][1].split()[0]
            avg_dut_consumption = data["reportResult"]["stats"][15][1].split()[0]
            end_level = data["reportResult"]["stats"][17][1].split()[0]
            difference = data["reportResult"]["stats"][22][1].split()[0]

            not_valid_val = ['-----', '', ' ']

            obj.odometer_mileage = float(odometer_mileage) if odometer_mileage not in not_valid_val else None
            obj.trip_mileage = float(trip_mileage) if trip_mileage not in not_valid_val else None
            obj.start_level = float(start_level) if start_level not in not_valid_val else None
            obj.total_refueled = float(total_refueled) if total_refueled not in not_valid_val else None
            obj.avg_trip_dut_consumption = float(avg_trip_dut_consumption) if avg_trip_dut_consumption not in not_valid_val else None
            obj.avg_dut_consumption = float(avg_dut_consumption) if avg_dut_consumption not in not_valid_val else None
            obj.end_level = float(end_level) if end_level not in not_valid_val else None
            obj.difference = float(difference) if difference not in not_valid_val else None

            obj.save()
        
        context["data"] = data
        return render(request, self.template_name, context)


class DeltaReportViewSet(ModelViewSet):
    queryset = DeltaReport.objects.all()
    serializer_class = DeltaReportSerializer
