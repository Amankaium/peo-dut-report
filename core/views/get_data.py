from django.views import View
from django.shortcuts import render
import requests


class GetDataView(View):
    template_name = 'core/get_data.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        response = requests.post(
            url='http://wialon.realcom.kg/wialon/ajax.html?svc=report/exec_report&sid=33feb7834319099915dd56a6fcbe2949',
            data={
                "sid": "33feb7834319099915dd56a6fcbe2949",
                "params": '{"reportResourceId":6354,"reportTemplateId":1,"reportTemplate":null,"reportObjectId":6591,"reportObjectSecId":0,"interval":{"flags":16777216,"from":1688204160,"to":1690859159},"remoteExec":0}'
            }
        )
        context = {}
        context["data"] = response.json()
        return render(request, self.template_name, context)