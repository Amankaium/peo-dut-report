from django.views import View
from django.shortcuts import render
import requests
from core.models import Transport


class GetDataView(View):
    template_name = 'core/get_data.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # 6591 
        # Daf 01KG 795AC 
        context = {}
        cars = Transport.objects.all()
        data = []
        for car in cars:
            response = requests.post(
                url='http://wialon.realcom.kg/wialon/ajax.html?svc=report/exec_report&sid=5eecc4a145ca6ca2a3a17c4e65b96f49',
                data={
                    "sid": "5eecc4a145ca6ca2a3a17c4e65b96f49",
                    "params": '{"reportResourceId":6354,"reportTemplateId":1,"reportTemplate":null,"reportObjectId":%s,"reportObjectSecId":0,"interval":{"flags":16777216,"from":1688204160,"to":1690859159},"remoteExec":0}' % car.id_realcom
                }
            )
            # context["data"] = response.json()
            data.append(response.json())
        context["data"] = data
        context["value"] = data[0]["reportResult"]["stats"][6][1]
        return render(request, self.template_name, context)

    # def post(self, request):
    #     response = requests.post(
    #         url='https://wialon.realcom.kg/wialon/ajax.html?svc=core/batch&sid=5eecc4a145ca6ca2a3a17c4e65b96f49',
    #         data={
    #             "sid": "5eecc4a145ca6ca2a3a17c4e65b96f49",
    #             "params": '''{"params":[{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit","flags":8397079,"mode":1}]}},{"svc":"item/update_custom_property","params":{"itemId":6362,"name":"inf_map","value":""}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"col","data":["5878","6352","6562","6563","6564","6566","6567","6568","6569","6570","6571","6572","6573","6574","6575","6576","6577","6578","6579","6580","6581","6582","6583","6584","6585","6586","6587","6589","6590","6591","6592","6593","6594","6595","6596","6597","6599","6600","6601","6602","6603","6605","6606","6607","6608","6609","6610","6616","6617","6618","6619","6629","6632","6634","6635","6638","6639","6640","6641","6642","6643","6644","6645","6646","6647","6648","6649","6650","6661","6662","6663","6664","6665","6666","6667","6677","6678","6687","6688","6689","6690","6691","6693","6694","6696","6697","6698","6699","6700","6701","6702","6703","6704","6705","6706","6707","6711","6712","6713","6715","6719","6720","6721","6722","6724","6725","6726","6728","6729","6731","6732","6738","6739","6750","6751","6753","6757","6758","6764","7068","7142","7143","7144","7170","7365"],"flags":4294967295,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"id","data":6362,"flags":513,"mode":1}]}},{"svc":"render/set_locale","params":{"tzOffset":134239328,"language":"ru","flags":256,"formatDate":"%Y-%m-%E %H:%M:%S"}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":4097,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1048577,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":519,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1031,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit_group","flags":21,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":313,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit_group","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"user","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":769,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":66049,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_resource","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_retranslator","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_retranslator","flags":1,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_route","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_route","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":33281,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":131585,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":2097665,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":8389121,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":8197,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"user","flags":2053,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_route","flags":3845,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_route","flags":4294967295,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":49439,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":458783,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":14680095,"mode":1}]}},{"svc":"core/get_hw_types","params":{"includeType":true}}],"flags":0}'''
    #         }
    #     )
    #     context = {}
    #     context["data"] = response.json()
    #     return render(request, self.template_name, context)
    

# [
#       {
#           "i": 5878,
#           "d": {
#               "nm": "Daf 01KG 924AI",
#               "cls": 2,
#               "id": 5878,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1627019002,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1808,
#               "cnm": 76242,
#               "cneh": 2762.6875,
#               "cnkb": 116091,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 76242,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/DAF XF 105.460 седельный тягач (1).png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6352,
#           "d": {
#               "nm": "Daf 01KG 449AE",
#               "cls": 2,
#               "id": 6352,
#               "prp": {
#                   "idrive": "1;1",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1647430263,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109651767",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331198",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 5838601,
#               "cneh": 2696.52861111,
#               "cnkb": 241618,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 5838601,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6562,
#           "d": {
#               "nm": "Daf 01KG 916AI",
#               "cls": 2,
#               "id": 6562,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1658901516,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1808,
#               "cnm": 53872,
#               "cneh": 3297.05777778,
#               "cnkb": 126479,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 53872,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6563,
#           "d": {
#               "nm": "Daf 01KG 275AE",
#               "cls": 2,
#               "id": 6563,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1658902819,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350424062199607",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996555963847",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 4427634,
#               "cneh": 2230.35583333,
#               "cnkb": 176753,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4427634,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6564,
#           "d": {
#               "nm": "Howo 8967 BB",
#               "cls": 2,
#               "id": 6564,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659000658,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1811,
#               "cnm": 16478,
#               "cneh": 906.578888889,
#               "cnkb": 24138,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 16478,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6566,
#           "d": {
#               "nm": "Daf 01KG 124AE",
#               "cls": 2,
#               "id": 6566,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659062661,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109223922",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331218",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 5336050,
#               "cneh": 1884.14083333,
#               "cnkb": 160299,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 5336050,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6567,
#           "d": {
#               "nm": "Daf 01KG 451AE",
#               "cls": 2,
#               "id": 6567,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659062809,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350424061600753",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996555963845",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 3345751,
#               "cneh": 2059.38027778,
#               "cnkb": 191762,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3345751,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6568,
#           "d": {
#               "nm": "Daf 01KG 495AG",
#               "cls": 2,
#               "id": 6568,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659065036,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108052587",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331227",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 68070,
#               "cneh": 1675.255,
#               "cnkb": 214068,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 68070,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6569,
#           "d": {
#               "nm": "Daf 01KG 973AD",
#               "cls": 2,
#               "id": 6569,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659065521,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 27994,
#               "cneh": 1696.81916667,
#               "cnkb": 120708,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 27994,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6570,
#           "d": {
#               "nm": "Daf 01KG 902AD",
#               "cls": 2,
#               "id": 6570,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659065804,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508635649",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576192",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 2000625,
#               "cneh": 3028.29444444,
#               "cnkb": 231688,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 2000625,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6571,
#           "d": {
#               "nm": "Daf 01KG 471AH",
#               "cls": 2,
#               "id": 6571,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659067060,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109260536",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+9969559331180",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 649099,
#               "cneh": 82.8127777778,
#               "cnkb": 26229,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 649099,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6572,
#           "d": {
#               "nm": "Daf 01KG 1066H",
#               "cls": 2,
#               "id": 6572,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659067576,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853041",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576190",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 2143822,
#               "cneh": 1573.29138889,
#               "cnkb": 178563,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 2143822,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6573,
#           "d": {
#               "nm": "Daf 04KG 411АС",
#               "cls": 2,
#               "id": 6573,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659068007,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508635730",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576189",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 17429293,
#               "cneh": 1564.57166667,
#               "cnkb": 130866,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 17429293,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6574,
#           "d": {
#               "nm": "Daf 01KG 543AE",
#               "cls": 2,
#               "id": 6574,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659068319,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109651791",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576188",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 61189,
#               "cneh": 1383.85888889,
#               "cnkb": 234370,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 61189,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6575,
#           "d": {
#               "nm": "Daf 01KG 748AE",
#               "cls": 2,
#               "id": 6575,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659068591,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 10474223,
#               "cneh": 2158.29222222,
#               "cnkb": 94742,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 10474223,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6576,
#           "d": {
#               "nm": "Daf 01KG 944AD",
#               "cls": 2,
#               "id": 6576,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659068749,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109292851",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331223",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 4288270,
#               "cneh": 1710.73638889,
#               "cnkb": 306407,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4288270,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6577,
#           "d": {
#               "nm": "Daf 01KG 450AE",
#               "cls": 2,
#               "id": 6577,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659069026,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109289956",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331197",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 5289507,
#               "cneh": 1362.53638889,
#               "cnkb": 115788,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 5289507,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6578,
#           "d": {
#               "nm": "Daf  04KG 418AC",
#               "cls": 2,
#               "id": 6578,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659159777,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088837218",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996995500451",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 1484779,
#               "cneh": 1742.90361111,
#               "cnkb": 135511,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1484779,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6579,
#           "d": {
#               "nm": "Daf 01KG 1056H",
#               "cls": 2,
#               "id": 6579,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659160280,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508674994",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576007",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 1917932,
#               "cneh": 3044.26,
#               "cnkb": 211988,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1917932,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6580,
#           "d": {
#               "nm": "Daf 01KG 625AE",
#               "cls": 2,
#               "id": 6580,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659160625,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109744307",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331232",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 56764,
#               "cneh": 1466.53194444,
#               "cnkb": 162583,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 56764,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6581,
#           "d": {
#               "nm": "Daf  01KG 541AE",
#               "cls": 2,
#               "id": 6581,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659160862,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853322",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576365",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 4192800,
#               "cneh": 2847.57777778,
#               "cnkb": 164867,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4192800,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6582,
#           "d": {
#               "nm": "Daf  01KG 0582M",
#               "cls": 2,
#               "id": 6582,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659161508,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108073054",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331228",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 3649538,
#               "cneh": 1124.74277778,
#               "cnkb": 114910,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3649538,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6583,
#           "d": {
#               "nm": "Daf 01KG 542AE",
#               "cls": 2,
#               "id": 6583,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659161763,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350317176553232",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576002",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 5947315,
#               "cneh": 2504.26361111,
#               "cnkb": 187115,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 5947315,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6584,
#           "d": {
#               "nm": "Daf 01KG 747AE",
#               "cls": 2,
#               "id": 6584,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659162005,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677666",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576203",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 66018,
#               "cneh": 2245.6625,
#               "cnkb": 208322,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 66018,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6585,
#           "d": {
#               "nm": "Daf 01KG 397AE",
#               "cls": 2,
#               "id": 6585,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659162309,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677658",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576202",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 1892625,
#               "cneh": 2234.65444444,
#               "cnkb": 153912,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1892625,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6586,
#           "d": {
#               "nm": "Daf  01KG 743AE",
#               "cls": 2,
#               "id": 6586,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659162518,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508680199",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576201",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 71798,
#               "cneh": 2964.4975,
#               "cnkb": 175928,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 71798,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6587,
#           "d": {
#               "nm": "Daf  04KG 422AC",
#               "cls": 2,
#               "id": 6587,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659162689,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508634634",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576200",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 12660778,
#               "cneh": 2896.49722222,
#               "cnkb": 134972,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 12660778,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6589,
#           "d": {
#               "nm": "Daf 01KG 0500M",
#               "cls": 2,
#               "id": 6589,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659411210,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853231",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997575197",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 55381,
#               "cneh": 1293.00194444,
#               "cnkb": 176410,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 55381,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6590,
#           "d": {
#               "nm": "Daf 01KG 564AH",
#               "cls": 2,
#               "id": 6590,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659411494,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108050672",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996995500123",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 1840361,
#               "cneh": 1737.57277778,
#               "cnkb": 165996,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1840361,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6591,
#           "d": {
#               "nm": "Daf 01KG 795AC",
#               "cls": 2,
#               "id": 6591,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "solid_colors": "255",
#                   "track_solid": "255",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659411696,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109265345",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576011",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 68626,
#               "cneh": 1963.74444444,
#               "cnkb": 294698,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 68626,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6592,
#           "d": {
#               "nm": "Daf 01KG 1055H",
#               "cls": 2,
#               "id": 6592,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659412075,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677740",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576012",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 4096620,
#               "cneh": 2751.41916667,
#               "cnkb": 190390,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4096620,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6593,
#           "d": {
#               "nm": "Daf 01KG 476AE",
#               "cls": 2,
#               "id": 6593,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659412396,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108173888",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576016",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 12621641,
#               "cneh": 2620.54527778,
#               "cnkb": 173510,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 12621641,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6594,
#           "d": {
#               "nm": "Daf 01KG 976AH",
#               "cls": 2,
#               "id": 6594,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659412844,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508675066",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576017",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 83515,
#               "cneh": 2743.95194444,
#               "cnkb": 220200,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 83515,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6595,
#           "d": {
#               "nm": "Daf 01KG 276AE",
#               "cls": 2,
#               "id": 6595,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659413074,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508674903",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576018",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 68877,
#               "cneh": 2348.61555556,
#               "cnkb": 114967,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 68877,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6596,
#           "d": {
#               "nm": "Daf 01KG 945AD",
#               "cls": 2,
#               "id": 6596,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659438976,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 3622886,
#               "cneh": 2301.50277778,
#               "cnkb": 114276,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3622886,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6597,
#           "d": {
#               "nm": "Daf 01KG 612AG",
#               "cls": 2,
#               "id": 6597,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659439364,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508675009",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576020",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 2531083,
#               "cneh": 2738.96388889,
#               "cnkb": 193264,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 2531083,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6599,
#           "d": {
#               "nm": "Daf 04KG 427AC",
#               "cls": 2,
#               "id": 6599,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659495522,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508674937",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576008",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 53039,
#               "cneh": 1989.44361111,
#               "cnkb": 141204,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 53039,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6600,
#           "d": {
#               "nm": "Axor 01KG 284AG",
#               "cls": 2,
#               "id": 6600,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659496206,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1811,
#               "cnm": 47553,
#               "cneh": 1626.6,
#               "cnkb": 152453,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 47553,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6601,
#           "d": {
#               "nm": "Axor 01KG 287AG",
#               "cls": 2,
#               "id": 6601,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659499886,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 55646,
#               "cneh": 1671.27194444,
#               "cnkb": 121171,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 55646,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6602,
#           "d": {
#               "nm": "Axor 01KG 097AJ",
#               "cls": 2,
#               "id": 6602,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659523709,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1811,
#               "cnm": 38724,
#               "cneh": 1213.19083333,
#               "cnkb": 120259,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 38724,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6603,
#           "d": {
#               "nm": "Daf 01KG 474AE",
#               "cls": 2,
#               "id": 6603,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659523988,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109260510",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996995500381",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 3958596,
#               "cneh": 1340.50638889,
#               "cnkb": 127594,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3958596,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6605,
#           "d": {
#               "nm": "Axor 01KG 093AJ",
#               "cls": 2,
#               "id": 6605,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659603354,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 58373,
#               "cneh": 1676.01027778,
#               "cnkb": 164867,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 58373,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6606,
#           "d": {
#               "nm": "Axor 01KG 095AJ",
#               "cls": 2,
#               "id": 6606,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659603381,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 54961,
#               "cneh": 1890.23388889,
#               "cnkb": 182010,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 54961,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6607,
#           "d": {
#               "nm": "Daf 01KG 325AE",
#               "cls": 2,
#               "id": 6607,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659605084,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 4262997,
#               "cneh": 1922.98694444,
#               "cnkb": 113475,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4262997,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6608,
#           "d": {
#               "nm": "Daf 01KG 274AE",
#               "cls": 2,
#               "id": 6608,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659606307,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544509416908",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576031",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 6279533,
#               "cneh": 2068.79111111,
#               "cnkb": 221044,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 6279533,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6609,
#           "d": {
#               "nm": "Axor 01KG 285AG",
#               "cls": 2,
#               "id": 6609,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659610425,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 59639,
#               "cneh": 1977.18638889,
#               "cnkb": 152268,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 59639,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6610,
#           "d": {
#               "nm": "Axor 01KG 094AJ",
#               "cls": 2,
#               "id": 6610,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659610745,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 66799,
#               "cneh": 2176.36777778,
#               "cnkb": 186863,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 66799,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6616,
#           "d": {
#               "nm": "Daf 01KG 603AH",
#               "cls": 2,
#               "id": 6616,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659928777,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109218179",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576135",
#               "ph2": "+996995900368",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 63068,
#               "cneh": 2518.4525,
#               "cnkb": 163031,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 63068,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6617,
#           "d": {
#               "nm": "Axor 01KG 096AJ",
#               "cls": 2,
#               "id": 6617,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659929048,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1808,
#               "cnm": 614634,
#               "cneh": 2429.36444444,
#               "cnkb": 105646,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 614634,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6618,
#           "d": {
#               "nm": "Axor 01KG 283AG",
#               "cls": 2,
#               "id": 6618,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659929517,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 1397583,
#               "cneh": 1973.78833333,
#               "cnkb": 154062,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1397583,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6619,
#           "d": {
#               "nm": "Daf 04KG 527AC",
#               "cls": 2,
#               "id": 6619,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1659929929,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109670981",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331178",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 52543,
#               "cneh": 1721.01944444,
#               "cnkb": 93890,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 52543,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6629,
#           "d": {
#               "nm": "Daf 01KG 915AI",
#               "cls": 2,
#               "id": 6629,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660187503,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 73878,
#               "cneh": 2266.28083333,
#               "cnkb": 85852,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 73878,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6632,
#           "d": {
#               "nm": "Daf 01KG 900AD",
#               "cls": 2,
#               "id": 6632,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660188064,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1809,
#               "cnm": 61467,
#               "cneh": 2436.20583333,
#               "cnkb": 91124,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 61467,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6634,
#           "d": {
#               "nm": "Daf 01KG 123AE",
#               "cls": 2,
#               "id": 6634,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660188358,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677278",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576106",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 3714566,
#               "cneh": 2304.53694444,
#               "cnkb": 132892,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3714566,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6635,
#           "d": {
#               "nm": "Daf 01KG 086AE",
#               "cls": 2,
#               "id": 6635,
#               "prp": {
#                   "idrive": "3;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660188567,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677922",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576105",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 5822674,
#               "cneh": 2226.3625,
#               "cnkb": 138097,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 5822674,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6638,
#           "d": {
#               "nm": "Howo 8963 BB",
#               "cls": 2,
#               "id": 6638,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660618966,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853090",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576099",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 28035,
#               "cneh": 2450.12277778,
#               "cnkb": 29062,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 28035,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6639,
#           "d": {
#               "nm": "Shaanxi 01KG 372AO",
#               "cls": 2,
#               "id": 6639,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660619964,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109218096",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576100",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 18826,
#               "cneh": 1026.94472222,
#               "cnkb": 22822,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 18826,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6640,
#           "d": {
#               "nm": "Howo 01KG 712AA",
#               "cls": 2,
#               "id": 6640,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660620889,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480086663251",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576101",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 24914,
#               "cneh": 1396.32138889,
#               "cnkb": 28328,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 24914,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6641,
#           "d": {
#               "nm": "Kamaz 01KG 075AE",
#               "cls": 2,
#               "id": 6641,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660621169,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853298",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576102",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 1061,
#               "cneh": 1097.80805556,
#               "cnkb": 4181,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1061,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6642,
#           "d": {
#               "nm": "Howo 01KG 715AA",
#               "cls": 2,
#               "id": 6642,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660621189,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480086968437",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576127",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 21850,
#               "cneh": 1794.35666667,
#               "cnkb": 21225,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 21850,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6643,
#           "d": {
#               "nm": "Howo 8671 BB",
#               "cls": 2,
#               "id": 6643,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660622738,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853264",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576128",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 35966,
#               "cneh": 1513.68888889,
#               "cnkb": 36126,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 35966,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6644,
#           "d": {
#               "nm": "Howo 01KG 714AA",
#               "cls": 2,
#               "id": 6644,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660623260,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480087436772",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576088",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 30010,
#               "cneh": 1338.73833333,
#               "cnkb": 27724,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 30010,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6645,
#           "d": {
#               "nm": "Daf 01KG 1694M",
#               "cls": 2,
#               "id": 6645,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660639073,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508680314",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576089",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 66894,
#               "cneh": 2363.13694444,
#               "cnkb": 122136,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 66894,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6646,
#           "d": {
#               "nm": "Daf 01KG 746AE",
#               "cls": 2,
#               "id": 6646,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660640122,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108235992",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576090",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 67194,
#               "cneh": 1318.72416667,
#               "cnkb": 334317,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 67194,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6647,
#           "d": {
#               "nm": "Daf 01KG 1065H",
#               "cls": 2,
#               "id": 6647,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660640493,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676734",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576091",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 4454721,
#               "cneh": 2467.34666667,
#               "cnkb": 167441,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4454721,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6648,
#           "d": {
#               "nm": "Actros 4682 BC",
#               "cls": 2,
#               "id": 6648,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660640672,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109655420",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576036",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 549,
#               "cneh": 470.951388889,
#               "cnkb": 17555,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 549,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6649,
#           "d": {
#               "nm": "Daf 01KG 749AE",
#               "cls": 2,
#               "id": 6649,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660640700,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676619",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576125",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 12586654,
#               "cneh": 2911.29666667,
#               "cnkb": 82601,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 12586654,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6650,
#           "d": {
#               "nm": "Daf 4680 BC",
#               "cls": 2,
#               "id": 6650,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1660647360,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676742",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576037",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 44428986,
#               "cneh": 1034.3425,
#               "cnkb": 25690,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 44428986,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6661,
#           "d": {
#               "nm": "Daf 01KG 2191M",
#               "cls": 2,
#               "id": 6661,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661338044,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676577",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576430",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 62231,
#               "cneh": 2530.66194444,
#               "cnkb": 99110,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 62231,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6662,
#           "d": {
#               "nm": "Daf 01KG 744AE",
#               "cls": 2,
#               "id": 6662,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661338530,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508677674",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576431",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 2004267,
#               "cneh": 2162.0925,
#               "cnkb": 83097,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 2004267,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6663,
#           "d": {
#               "nm": "Daf 01KG 477AE",
#               "cls": 2,
#               "id": 6663,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661338780,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676510",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576325",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 11813502,
#               "cneh": 2132.96055556,
#               "cnkb": 79438,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 11813502,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6664,
#           "d": {
#               "nm": "Daf 01KG 914AI",
#               "cls": 2,
#               "id": 6664,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661339100,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508672659",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576433",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 38721,
#               "cneh": 0,
#               "cnkb": 100080,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 38721,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6665,
#           "d": {
#               "nm": "Daf 01KG 901AD",
#               "cls": 2,
#               "id": 6665,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661339503,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676593",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576429",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 1058761,
#               "cneh": 2740.37194444,
#               "cnkb": 86341,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1058761,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6666,
#           "d": {
#               "nm": "Axor 01KG 286AG",
#               "cls": 2,
#               "id": 6666,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661339670,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508676494",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576428",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 1405659,
#               "cneh": 2366.81055556,
#               "cnkb": 134003,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1405659,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6667,
#           "d": {
#               "nm": "Daf 01KG 933AL",
#               "cls": 2,
#               "id": 6667,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1661395281,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632103090392",
#               "uid2": "",
#               "hw": 4287,
#               "ph": "+996997576445",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 26987,
#               "cneh": 1377.42944444,
#               "cnkb": 22357,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 26987,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6677,
#           "d": {
#               "nm": "Howo 01KG 716AA",
#               "cls": 2,
#               "id": 6677,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662439520,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109602042",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576310",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 21509,
#               "cneh": 1142.21583333,
#               "cnkb": 34480,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 21509,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6678,
#           "d": {
#               "nm": "Howo 01KG 725AA",
#               "cls": 2,
#               "id": 6678,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662440784,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108072858",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576309",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 31834,
#               "cneh": 1249.87027778,
#               "cnkb": 24517,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 31834,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6687,
#           "d": {
#               "nm": "Howo 5113 BC Дут",
#               "cls": 2,
#               "id": 6687,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662959016,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108173987",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576362",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 20559,
#               "cneh": 960.901944444,
#               "cnkb": 95661,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 20559,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6688,
#           "d": {
#               "nm": "Howo 8672 BB",
#               "cls": 2,
#               "id": 6688,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662961289,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109744323",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576371",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 30040,
#               "cneh": 1312.04138889,
#               "cnkb": 42988,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 30040,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6689,
#           "d": {
#               "nm": "Howo 01KG 713AA",
#               "cls": 2,
#               "id": 6689,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662971259,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109369048",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576369",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 30713,
#               "cneh": 1387.55805556,
#               "cnkb": 36431,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 30713,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6690,
#           "d": {
#               "nm": "Kamaz 7433 BC",
#               "cls": 2,
#               "id": 6690,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662973219,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109285483",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576372",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 19289,
#               "cneh": 4588.265,
#               "cnkb": 104503,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 19289,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6691,
#           "d": {
#               "nm": "Howo 5127 BC",
#               "cls": 2,
#               "id": 6691,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662974214,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109369030",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576306",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 12766,
#               "cneh": 891.264166667,
#               "cnkb": 18284,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 12766,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6693,
#           "d": {
#               "nm": "Howo 01KG 723AA",
#               "cls": 2,
#               "id": 6693,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662974858,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109369014",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576375",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 26391,
#               "cneh": 1820.54777778,
#               "cnkb": 34613,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 26391,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6694,
#           "d": {
#               "nm": "Shaanxi 01KG 395AO",
#               "cls": 2,
#               "id": 6694,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662975436,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853066",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576374",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 21483,
#               "cneh": 2156.68166667,
#               "cnkb": 29867,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 21483,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6696,
#           "d": {
#               "nm": "Howo 01KG 724AA",
#               "cls": 2,
#               "id": 6696,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662976513,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108160042",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576373",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 24712,
#               "cneh": 1865.39944444,
#               "cnkb": 36829,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 24712,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6697,
#           "d": {
#               "nm": "Howo 01KG 728AA",
#               "cls": 2,
#               "id": 6697,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662976848,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480088853272",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576366",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 26306,
#               "cneh": 1674.67722222,
#               "cnkb": 31110,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 26306,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6698,
#           "d": {
#               "nm": "Kamaz 01KG278AT",
#               "cls": 2,
#               "id": 6698,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662977928,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108778504",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996995500382",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 6195,
#               "cneh": 1282.10055556,
#               "cnkb": 18023,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 6195,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6699,
#           "d": {
#               "nm": "Howo 5126 BC",
#               "cls": 2,
#               "id": 6699,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662980037,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109294535",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576456",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 14814,
#               "cneh": 701.011388889,
#               "cnkb": 19763,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 14814,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6700,
#           "d": {
#               "nm": "Howo 7054 BC",
#               "cls": 2,
#               "id": 6700,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662980391,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109352754",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576361",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 22579,
#               "cneh": 123.956388889,
#               "cnkb": 29308,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 22579,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6701,
#           "d": {
#               "nm": "Kamaz 06KG122ABO",
#               "cls": 2,
#               "id": 6701,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1662981570,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108160075",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576359",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 12192,
#               "cneh": 261.961666667,
#               "cnkb": 222855,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 12192,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6702,
#           "d": {
#               "nm": "Shaanxi 01KG 396AO",
#               "cls": 2,
#               "id": 6702,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663037336,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108277895",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576358",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 41826,
#               "cneh": 1466.64805556,
#               "cnkb": 61308,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 41826,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6703,
#           "d": {
#               "nm": "Daf 01KG 1067H",
#               "cls": 2,
#               "id": 6703,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663037797,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508673459",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576349",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 13327227,
#               "cneh": 2169.39694444,
#               "cnkb": 126863,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 13327227,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6704,
#           "d": {
#               "nm": "Daf 4681 BC",
#               "cls": 2,
#               "id": 6704,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663038222,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508673558",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576308",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 22314,
#               "cneh": 1578.08388889,
#               "cnkb": 141517,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 22314,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6705,
#           "d": {
#               "nm": "Daf 01KG 370AG",
#               "cls": 2,
#               "id": 6705,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663038641,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508672808",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576346",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 49030,
#               "cneh": 3148.695,
#               "cnkb": 149877,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 49030,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6706,
#           "d": {
#               "nm": "Daf 01KG 238AH",
#               "cls": 2,
#               "id": 6706,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663039292,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508673251",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576348",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 9644258,
#               "cneh": 2113.51,
#               "cnkb": 131224,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 9644258,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6707,
#           "d": {
#               "nm": "Daf 01KG 804AH",
#               "cls": 2,
#               "id": 6707,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663039955,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508673301",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576347",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1809,
#               "cnm": 3851654,
#               "cneh": 2486.90111111,
#               "cnkb": 109502,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 3851654,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6711,
#           "d": {
#               "nm": "Sprinter 01KG 672AJ",
#               "cls": 2,
#               "id": 6711,
#               "prp": {
#                   "idrive": "1;1",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663141887,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108072023",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 70734,
#               "cneh": 0,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 70734,
#               "pflds": {},
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volkswagen Crafter (15).png",
#               "ugi": 1,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6712,
#           "d": {
#               "nm": "Mercedes-Benz 8855 BC",
#               "cls": 2,
#               "id": 6712,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663142025,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109671013",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331221",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 20801,
#               "cneh": 683.656388889,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 20801,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volkswagen Crafter (9).png",
#               "ugi": 1,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6713,
#           "d": {
#               "nm": "Sprinter 01KG 033АК",
#               "cls": 2,
#               "id": 6713,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663142096,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108092724",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 64839,
#               "cneh": 0,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 64839,
#               "pflds": {},
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volkswagen Crafter (15).png",
#               "ugi": 1,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6715,
#           "d": {
#               "nm": "Sprinter 01KG 571AG",
#               "cls": 2,
#               "id": 6715,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663143796,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109747383",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 70200,
#               "cneh": 1353.38972222,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 70200,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volkswagen Crafter (9).png",
#               "ugi": 1,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6719,
#           "d": {
#               "nm": "Howo 5112 BC",
#               "cls": 2,
#               "id": 6719,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566528,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109369105",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576212",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 39533,
#               "cneh": 1490.58305556,
#               "cnkb": 35199,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 39533,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6720,
#           "d": {
#               "nm": "Actros 01KG 546AH",
#               "cls": 2,
#               "id": 6720,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566596,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480086663269",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996559331134",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 38433,
#               "cneh": 1267.69611111,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 38433,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6721,
#           "d": {
#               "nm": "Howo 01KG 479AG",
#               "cls": 2,
#               "id": 6721,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566633,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109580859",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576218",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 28949,
#               "cneh": 0,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 28949,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Камаз цистерна АЦПТ-9,5.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6722,
#           "d": {
#               "nm": "Howo 5109 BC",
#               "cls": 2,
#               "id": 6722,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566656,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109727328",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576217",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 25215,
#               "cneh": 1435.64194444,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 25215,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6724,
#           "d": {
#               "nm": "Zil 9065 BC",
#               "cls": 2,
#               "id": 6724,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "39219",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566754,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108157170",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 35845,
#               "cneh": 1044.28527778,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 35845,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/035 - копия.png",
#               "ugi": 2,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6725,
#           "d": {
#               "nm": "Daf 01KG 405AF",
#               "cls": 2,
#               "id": 6725,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566813,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108157741",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576253",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 22378,
#               "cneh": 1414.97638889,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 22378,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6726,
#           "d": {
#               "nm": "Howo 5124 BC",
#               "cls": 2,
#               "id": 6726,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663566838,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632102820914",
#               "uid2": "",
#               "hw": 4287,
#               "ph": "+996997576222",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 21239,
#               "cneh": 1127.21583333,
#               "cnkb": 25175,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 21239,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volvo FH третье поколение с полуприцепом (1).png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6731,
#           "d": {
#               "nm": "Daf 4176 ВС",
#               "cls": 2,
#               "id": 6731,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663729094,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1808,
#               "cnm": 7683512,
#               "cneh": 729.089722222,
#               "cnkb": 54831,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 7683512,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6732,
#           "d": {
#               "nm": "Actros 01KG 547AH",
#               "cls": 2,
#               "id": 6732,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663729531,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "cfl": 1808,
#               "cnm": 42308,
#               "cneh": 1837.64416667,
#               "cnkb": 44833,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 42308,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 825472598003
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6738,
#           "d": {
#               "nm": "Howo 5110 BC",
#               "cls": 2,
#               "id": 6738,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663754499,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108092708",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576258",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 24914,
#               "cneh": 1252.34888889,
#               "cnkb": 31918,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 24914,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6739,
#           "d": {
#               "nm": "Kamaz 01KG599AG",
#               "cls": 2,
#               "id": 6739,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1663756774,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109655412",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576179",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 38683,
#               "cneh": 1256.94555556,
#               "cnkb": 31661,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 38683,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6750,
#           "d": {
#               "nm": "Daf 01KG 658AD",
#               "cls": 2,
#               "id": 6750,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1664335874,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508672907",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576213",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 64824,
#               "cneh": 2453.72583333,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 64824,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6751,
#           "d": {
#               "nm": "Daf 2778 BC",
#               "cls": 2,
#               "id": 6751,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1664336358,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "350544508672832",
#               "uid2": "",
#               "hw": 4288,
#               "ph": "+996997576214",
#               "ph2": "",
#               "psw": "",
#               "cfl": 785,
#               "cnm": 20259,
#               "cneh": 1327.18833333,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 20259,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 2,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6753,
#           "d": {
#               "nm": "Howo 01KG 624AC",
#               "cls": 2,
#               "id": 6753,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1664351138,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "358480087436863",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576216",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 27831,
#               "cneh": 1299.96638889,
#               "cnkb": 35854,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 27831,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6757,
#           "d": {
#               "nm": "Daf 01KG 273AE",
#               "cls": 2,
#               "id": 6757,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1664505450,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109127370",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576220",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 30774,
#               "cneh": 1537.04888889,
#               "cnkb": 40009,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 30774,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 1,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 6758,
#           "d": {
#               "nm": "Daf 4177 BC",
#               "cls": 2,
#               "id": 6758,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1664505894,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109655065",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997576221",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 1181959,
#               "cneh": 782.515833333,
#               "cnkb": 17059,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 1181959,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/032 - копия.png",
#               "ugi": 1,
#               "uacl": 880317333491
#           },
#           "f": 8397079
#       },
#       {
#           "i": 7068,
#           "d": {
#               "nm": "ЗиЛ 8207BC",
#               "cls": 2,
#               "id": 7068,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1673245960,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109370863",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996701260408",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1811,
#               "cnm": 4601,
#               "cneh": 215.290833333,
#               "cnkb": 10301,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 4601,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 7170,
#           "d": {
#               "nm": "Daf 01KG068AO",
#               "cls": 2,
#               "id": 7170,
#               "prp": {
#                   "idrive": "1;1",
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "monitoring_battery_id": "0",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1678867477,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632108156685",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996997882084",
#               "ph2": "",
#               "psw": "",
#               "cfl": 1808,
#               "cnm": 6494,
#               "cneh": 565.873611111,
#               "cnkb": 33197,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 6494,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Mercedes-Benz Actros.png",
#               "ugi": 1,
#               "uacl": 880317317107
#           },
#           "f": 8397079
#       },
#       {
#           "i": 7365,
#           "d": {
#               "nm": "Sprinter 01KG 324AT",
#               "cls": 2,
#               "id": 7365,
#               "prp": {
#                   "img_rot": "0",
#                   "label_color": "16711680",
#                   "trip_colors": "1",
#                   "use_sensor_color": "1"
#               },
#               "crt": 6353,
#               "bact": 6354,
#               "mu": 0,
#               "ct": 1687238896,
#               "ftp": {
#                   "ch": 0,
#                   "tp": 0,
#                   "fl": 0
#               },
#               "uid": "359632109600202",
#               "uid2": "",
#               "hw": 2425,
#               "ph": "+996995500383",
#               "ph2": "",
#               "psw": "",
#               "cfl": 784,
#               "cnm": 15807,
#               "cneh": 0,
#               "cnkb": 0,
#               "act": 1,
#               "dactt": 0,
#               "cnm_km": 15807,
#               "pflds": {
#                   "1": {
#                       "id": 1,
#                       "n": "vehicle_class",
#                       "v": "empty_vehicle"
#                   }
#               },
#               "pfldsmax": 0,
#               "uri": "\/avl_library_image\/1188\/0\/library\/unit\/Volkswagen Crafter (15).png",
#               "ugi": 1,
#               "uacl": 877079330803
#           },
#           "f": 8397079
#       }
#   ],