fetch("http://wialon.realcom.kg/wialon/ajax.html?svc=core/batch&sid=50f06b29b358759bdab7d2f00761ef60", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded"
  },
  "referrer": "http://wialon.realcom.kg/wialon/post.html",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "params=%7B%22params%22%3A%5B%7B%22svc%22%3A%22core%2Fset_session_property%22%2C%22params%22%3A%7B%22prop_name%22%3A%22skip_nonactive_items%22%2C%22prop_value%22%3A1%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A4294967295%2C%22mode%22%3A2%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_route%22%2C%22flags%22%3A4294967295%2C%22mode%22%3A2%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit%22%2C%22flags%22%3A4294967295%2C%22mode%22%3A2%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_unit_group%22%2C%22flags%22%3A4294967295%2C%22mode%22%3A2%7D%5D%7D%7D%2C%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22user%22%2C%22flags%22%3A4294967295%2C%22mode%22%3A2%7D%5D%7D%7D%2C%7B%22svc%22%3A%22render%2Fremove_layer%22%2C%22params%22%3A%7B%22layerName%22%3A%22messages%22%7D%7D%2C%7B%22svc%22%3A%22render%2Fremove_layer%22%2C%22params%22%3A%7B%22layerName%22%3A%22%22%7D%7D%2C%7B%22svc%22%3A%22report%2Fcleanup_result%22%2C%22params%22%3A%7B%7D%7D%2C%7B%22svc%22%3A%22events%2Fupdate_units%22%2C%22params%22%3A%7B%22mode%22%3A%22clear%22%7D%7D%5D%2C%22flags%22%3A0%7D&sid=50f06b29b358759bdab7d2f00761ef60",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
})
.then(r => r.json())
.then(data => console.log(data))

;



request_params = {
    "params": [
      {
        "svc": "core/set_session_property",
        "params": {
          "prop_name": "skip_nonactive_items",
          "prop_value": 1
        }
      },
      {
        "svc": "core/update_data_flags",
        "params": {
          "spec": [
            {
              "type": "type",
              "data": "avl_resource",
              "flags": 4294967295,
              "mode": 2
            }
          ]
        }
      },
      {
        "svc": "core/update_data_flags",
        "params": {
          "spec": [
            {
              "type": "type",
              "data": "avl_route",
              "flags": 4294967295,
              "mode": 2
            }
          ]
        }
      },
      {
        "svc": "core/update_data_flags",
        "params": {
          "spec": [
            {
              "type": "type",
              "data": "avl_unit",
              "flags": 4294967295,
              "mode": 2
            }
          ]
        }
      },
      {
        "svc": "core/update_data_flags",
        "params": {
          "spec": [
            {
              "type": "type",
              "data": "avl_unit_group",
              "flags": 4294967295,
              "mode": 2
            }
          ]
        }
      },
      {
        "svc": "core/update_data_flags",
        "params": {
          "spec": [
            {
              "type": "type",
              "data": "user",
              "flags": 4294967295,
              "mode": 2
            }
          ]
        }
      },
      {
        "svc": "render/remove_layer",
        "params": {
          "layerName": "messages"
        }
      },
      {
        "svc": "render/remove_layer",
        "params": {
          "layerName": ""
        }
      },
      {
        "svc": "report/cleanup_result",
        "params": {}
      },
      {
        "svc": "events/update_units",
        "params": {
          "mode": "clear"
        }
      }
    ],
    "flags": 0
  }

response = [
    {
        "error": 0
    },
    [
        {
            "i": 6354,
            "d": null,
            "f": 0
        }
    ],
    [],
    [
        {
            "i": 5878,
            "d": null,
            "f": 0
        },
        {
            "i": 6352,
            "d": null,
            "f": 0
        },
        {
            "i": 6562,
            "d": null,
            "f": 0
        },
        {
            "i": 6563,
            "d": null,
            "f": 0
        },
        {
            "i": 6564,
            "d": null,
            "f": 0
        },
        {
            "i": 6566,
            "d": null,
            "f": 0
        },
        {
            "i": 6567,
            "d": null,
            "f": 0
        },
        {
            "i": 6568,
            "d": null,
            "f": 0
        },
        {
            "i": 6569,
            "d": null,
            "f": 0
        },
        {
            "i": 6570,
            "d": null,
            "f": 0
        },
        {
            "i": 6571,
            "d": null,
            "f": 0
        },
        {
            "i": 6572,
            "d": null,
            "f": 0
        },
        {
            "i": 6573,
            "d": null,
            "f": 0
        },
        {
            "i": 6574,
            "d": null,
            "f": 0
        },
        {
            "i": 6575,
            "d": null,
            "f": 0
        },
        {
            "i": 6576,
            "d": null,
            "f": 0
        },
        {
            "i": 6577,
            "d": null,
            "f": 0
        },
        {
            "i": 6578,
            "d": null,
            "f": 0
        },
        {
            "i": 6579,
            "d": null,
            "f": 0
        },
        {
            "i": 6580,
            "d": null,
            "f": 0
        },
        {
            "i": 6581,
            "d": null,
            "f": 0
        },
        {
            "i": 6582,
            "d": null,
            "f": 0
        },
        {
            "i": 6583,
            "d": null,
            "f": 0
        },
        {
            "i": 6584,
            "d": null,
            "f": 0
        },
        {
            "i": 6585,
            "d": null,
            "f": 0
        },
        {
            "i": 6586,
            "d": null,
            "f": 0
        },
        {
            "i": 6587,
            "d": null,
            "f": 0
        },
        {
            "i": 6589,
            "d": null,
            "f": 0
        },
        {
            "i": 6590,
            "d": null,
            "f": 0
        },
        {
            "i": 6591,
            "d": null,
            "f": 0
        },
        {
            "i": 6592,
            "d": null,
            "f": 0
        },
        {
            "i": 6593,
            "d": null,
            "f": 0
        },
        {
            "i": 6594,
            "d": null,
            "f": 0
        },
        {
            "i": 6595,
            "d": null,
            "f": 0
        },
        {
            "i": 6596,
            "d": null,
            "f": 0
        },
        {
            "i": 6597,
            "d": null,
            "f": 0
        },
        {
            "i": 6599,
            "d": null,
            "f": 0
        },
        {
            "i": 6600,
            "d": null,
            "f": 0
        },
        {
            "i": 6601,
            "d": null,
            "f": 0
        },
        {
            "i": 6602,
            "d": null,
            "f": 0
        },
        {
            "i": 6603,
            "d": null,
            "f": 0
        },
        {
            "i": 6605,
            "d": null,
            "f": 0
        },
        {
            "i": 6606,
            "d": null,
            "f": 0
        },
        {
            "i": 6607,
            "d": null,
            "f": 0
        },
        {
            "i": 6608,
            "d": null,
            "f": 0
        },
        {
            "i": 6609,
            "d": null,
            "f": 0
        },
        {
            "i": 6610,
            "d": null,
            "f": 0
        },
        {
            "i": 6616,
            "d": null,
            "f": 0
        },
        {
            "i": 6617,
            "d": null,
            "f": 0
        },
        {
            "i": 6618,
            "d": null,
            "f": 0
        },
        {
            "i": 6619,
            "d": null,
            "f": 0
        },
        {
            "i": 6629,
            "d": null,
            "f": 0
        },
        {
            "i": 6632,
            "d": null,
            "f": 0
        },
        {
            "i": 6634,
            "d": null,
            "f": 0
        },
        {
            "i": 6635,
            "d": null,
            "f": 0
        },
        {
            "i": 6638,
            "d": null,
            "f": 0
        },
        {
            "i": 6639,
            "d": null,
            "f": 0
        },
        {
            "i": 6640,
            "d": null,
            "f": 0
        },
        {
            "i": 6641,
            "d": null,
            "f": 0
        },
        {
            "i": 6642,
            "d": null,
            "f": 0
        },
        {
            "i": 6643,
            "d": null,
            "f": 0
        },
        {
            "i": 6644,
            "d": null,
            "f": 0
        },
        {
            "i": 6645,
            "d": null,
            "f": 0
        },
        {
            "i": 6646,
            "d": null,
            "f": 0
        },
        {
            "i": 6647,
            "d": null,
            "f": 0
        },
        {
            "i": 6648,
            "d": null,
            "f": 0
        },
        {
            "i": 6649,
            "d": null,
            "f": 0
        },
        {
            "i": 6650,
            "d": null,
            "f": 0
        },
        {
            "i": 6661,
            "d": null,
            "f": 0
        },
        {
            "i": 6662,
            "d": null,
            "f": 0
        },
        {
            "i": 6663,
            "d": null,
            "f": 0
        },
        {
            "i": 6664,
            "d": null,
            "f": 0
        },
        {
            "i": 6665,
            "d": null,
            "f": 0
        },
        {
            "i": 6666,
            "d": null,
            "f": 0
        },
        {
            "i": 6667,
            "d": null,
            "f": 0
        },
        {
            "i": 6677,
            "d": null,
            "f": 0
        },
        {
            "i": 6678,
            "d": null,
            "f": 0
        },
        {
            "i": 6687,
            "d": null,
            "f": 0
        },
        {
            "i": 6688,
            "d": null,
            "f": 0
        },
        {
            "i": 6689,
            "d": null,
            "f": 0
        },
        {
            "i": 6690,
            "d": null,
            "f": 0
        },
        {
            "i": 6691,
            "d": null,
            "f": 0
        },
        {
            "i": 6693,
            "d": null,
            "f": 0
        },
        {
            "i": 6694,
            "d": null,
            "f": 0
        },
        {
            "i": 6696,
            "d": null,
            "f": 0
        },
        {
            "i": 6697,
            "d": null,
            "f": 0
        },
        {
            "i": 6698,
            "d": null,
            "f": 0
        },
        {
            "i": 6699,
            "d": null,
            "f": 0
        },
        {
            "i": 6700,
            "d": null,
            "f": 0
        },
        {
            "i": 6701,
            "d": null,
            "f": 0
        },
        {
            "i": 6702,
            "d": null,
            "f": 0
        },
        {
            "i": 6703,
            "d": null,
            "f": 0
        },
        {
            "i": 6704,
            "d": null,
            "f": 0
        },
        {
            "i": 6705,
            "d": null,
            "f": 0
        },
        {
            "i": 6706,
            "d": null,
            "f": 0
        },
        {
            "i": 6707,
            "d": null,
            "f": 0
        },
        {
            "i": 6711,
            "d": null,
            "f": 0
        },
        {
            "i": 6712,
            "d": null,
            "f": 0
        },
        {
            "i": 6713,
            "d": null,
            "f": 0
        },
        {
            "i": 6715,
            "d": null,
            "f": 0
        },
        {
            "i": 6719,
            "d": null,
            "f": 0
        },
        {
            "i": 6720,
            "d": null,
            "f": 0
        },
        {
            "i": 6721,
            "d": null,
            "f": 0
        },
        {
            "i": 6722,
            "d": null,
            "f": 0
        },
        {
            "i": 6724,
            "d": null,
            "f": 0
        },
        {
            "i": 6725,
            "d": null,
            "f": 0
        },
        {
            "i": 6726,
            "d": null,
            "f": 0
        },
        {
            "i": 6731,
            "d": null,
            "f": 0
        },
        {
            "i": 6732,
            "d": null,
            "f": 0
        },
        {
            "i": 6738,
            "d": null,
            "f": 0
        },
        {
            "i": 6739,
            "d": null,
            "f": 0
        },
        {
            "i": 6750,
            "d": null,
            "f": 0
        },
        {
            "i": 6751,
            "d": null,
            "f": 0
        },
        {
            "i": 6753,
            "d": null,
            "f": 0
        },
        {
            "i": 6757,
            "d": null,
            "f": 0
        },
        {
            "i": 6758,
            "d": null,
            "f": 0
        },
        {
            "i": 7068,
            "d": null,
            "f": 0
        },
        {
            "i": 7170,
            "d": null,
            "f": 0
        },
        {
            "i": 7365,
            "d": null,
            "f": 0
        }
    ],
    [
        {
            "i": 6728,
            "d": null,
            "f": 0
        },
        {
            "i": 6729,
            "d": null,
            "f": 0
        },
        {
            "i": 6764,
            "d": null,
            "f": 0
        },
        {
            "i": 7142,
            "d": null,
            "f": 0
        },
        {
            "i": 7143,
            "d": null,
            "f": 0
        },
        {
            "i": 7144,
            "d": null,
            "f": 0
        }
    ],
    [],
    {
        "error": 4
    },
    {
        "error": 4
    },
    {
        "error": 0
    },
    {
        "units": 0
    }
]