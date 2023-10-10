from core.serializers import *
from core.models import DeltaReport
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from openpyxl import load_workbook


class DeltaReportAddView(View):
    def get(self, request):
        return render(request, 'core/delta_reports_add.html')

    def post(self, request):
        excel_file = request.FILES["excel_file"]
        new_excel_source = ExcelSource.objects.create(
            excel_file=excel_file,
            created_by=request.user
        )
        messages.success(request, "Файл добавлен")
        context = {}
        excel_file_source = load_workbook('media/' + new_excel_source.excel_file.name)
        page = excel_file_source[excel_file_source.sheetnames[1]]
        created_qty = 0
        no_count = False
        for row in page:
            if not no_count:
                if row[0].row == 1:
                    no_count = True
                continue
            vehicle_name = row[0].value
            period_start = row[1].value
            period_end = row[2].value
            fact_km = row[3].value
            odometer_mileage = row[4].value
            trip_mileage = row[5].value
            start_balance = row[6].value
            start_level = row[7].value
            fueling_gsm = row[8].value
            total_refueled = row[9].value
            actual_fuel_consumption = row[10].value
            norm_fuel_consumption = row[11].value
            departure = row[12].value
            avg_trip_dut_consumption = row[13].value
            actual = row[14].value
            fuel_calculation_norm = row[15].value
            departure_balance = row[16].value
            end_balance = row[17].value
            end_level = row[18].value
            end_mech_balance = row[19].value
            difference = row[20].value
            deficiency = row[21].value
            surplus = row[22].value
            total_fuel_drained = row[23].value
            new_delta_report, created = DeltaReport.objects.get_or_create(
                vehicle_name=vehicle_name,
                period_start=period_start,
                period_end=period_end,
                fact_km=fact_km,
                odometer_mileage=odometer_mileage,
                trip_mileage=trip_mileage,
                start_balance=start_balance,
                start_level=start_level,
                fueling_gsm=fueling_gsm,
                total_refueled=total_refueled,
                actual_fuel_consumption=actual_fuel_consumption,
                norm_fuel_consumption=norm_fuel_consumption,
                departure=departure,
                avg_trip_dut_consumption=avg_trip_dut_consumption,
                actual=actual,
                fuel_calculation_norm=fuel_calculation_norm,
                departure_balance=departure_balance,
                end_balance=end_balance,
                end_level=end_level,
                end_mech_balance=end_mech_balance,
                difference=difference,
                deficiency=deficiency,
                surplus=surplus,
                total_fuel_drained=total_fuel_drained,
            )
            if created:
                created_qty += 1
        messages.success(request, f"Добавлено {created_qty} отчёты об отклонениях")
        return render(request, 'delta_reports_add.html', context)


class DeltaReportViewSet(ModelViewSet):
    queryset = DeltaReport.objects.all()
    serializer_class = DeltaReportSerializer
