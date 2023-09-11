import requests

response = requests.post(
    url='http://wialon.realcom.kg/wialon/ajax.html?svc=report/exec_report&sid=d80fed3b3194019732b7ef0e5f32f5f5',
    data={
        "sid": "d80fed3b3194019732b7ef0e5f32f5f5",
        "params": '{"reportResourceId":6354,"reportTemplateId":1,"reportTemplate":null,"reportObjectId":6591,"reportObjectSecId":0,"interval":{"flags":16777216,"from":1688204160,"to":1690859159},"remoteExec":0}'
    }
)

print(response.json())