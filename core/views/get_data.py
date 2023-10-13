from django.views import View
from django.shortcuts import render
import requests
from core.models import Transport


class GetDataView(View):
    template_name = 'core/get_data.html'

    def get(self, request):
        context = {}
        cars = Transport.objects.all()[:3]
        cars_data = []
        for car in cars:
            cars_data.append([car])
        context["cars_data"] = cars_data
        return render(request, self.template_name, context)

    def post(self, request):
        # example
        # 6591 
        # Daf 01KG 795AC 
        # 2023 Июль 01 15:36
        # 2023 Август 01 09:05
        context = {}
        cars = Transport.objects.all()[:3]
        cars_data = []
        sid = "4c54b170a2478d8b9b5627e05c4a370d"
        for car in cars:
            response = requests.post(
                url=f'http://wialon.realcom.kg/wialon/ajax.html?svc=report/exec_report&sid={sid}',
                data={
                    "sid": sid,
                    "params": '{"reportResourceId":6354,"reportTemplateId":1,"reportTemplate":null,"reportObjectId":%s,"reportObjectSecId":0,"interval":{"flags":16777216,"from":1688204160,"to":1690859159},"remoteExec":0}' % car.id_realcom
                }
            )
            data = response.json()
            odometer_mileage = data["reportResult"]["stats"][6][1]
            cars_data.append([car, odometer_mileage])
        context["cars_data"] = cars_data
        # context["value"] = data[0]["reportResult"]["stats"][6][1]
        return render(request, self.template_name, context)