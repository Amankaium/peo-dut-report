{
    "reportResult": {
        "msgsRendered": 1,
        "stats": [
            [
                "Отчет",
                "Отчет по ТС"
            ],
            [
                "Объект",
                "Axor 01KG 283AG"
            ],
            [
                "Время выполнения отчета",
                "2024-06-13 17:48:38"
            ],
            [
                "Начало интервала",
                "2024-06-01 00:00:00"
            ],
            [
                "Окончание интервала",
                "2024-06-13 23:59:59"
            ],
            [
                "Время в движении",
                "0:00:00"
            ],
            [
                "Пробег в поездках",  # trip_mileage
                "0.00 км"
            ],
            [
                "Потрачено по ДУТ",
                "2.17 л"
            ],
            [
                "Ср. расход по ДУТ в поездках",
                "0.00 л\/100 км"
            ],
            [
                "Ср. расход по ДУТ (весь пробег)",
                "0.00 л\/100 км"
            ],
            [
                "Нач. уровень", # start_level
                "440.17 л"
            ],
            [
                "Кон. уровень",
                "438.00 л"
            ],
            [
                "Всего топлива слито",
                "0.00 л"
            ],
            [
                "Всего заправлено",
                "0.00 л"
            ],
            [
                "Всего топлива зарегистрировано",
                "0.00 л"
            ],
            [
                "Разница",
                "-----"
            ]
        ],
        "tables": [
            {
                "name": "unit_generic",
                "label": "Сводка",
                "grouping": {
                    "type": "day"
                },
                "flags": 16781585,
                "rows": 13,
                "level": 2,
                "columns": 14,
                "header": [
                    "№",
                    "Группировка",
                    "Пробег в поездках",
                    "Моточасы",
                    "Потрачено по ДАРТ",
                    "Ср. расход по ДАРТ",
                    "Потрачено по ДУТ",
                    "Ср. расход по ДУТ",
                    "Нач. уровень",
                    "Кон. уровень",
                    "Заправлено",
                    "Слито",
                    "Всего заправок",
                    "Всего сливов"
                ],
                "header_type": [
                    "",
                    "",
                    "mileage",
                    "eh",
                    "fuel_consumption_abs",
                    "avg_fuel_consumption_abs",
                    "fuel_consumption_fls",
                    "avg_fuel_consumption_fls",
                    "fuel_level_begin",
                    "fuel_level_end",
                    "filled",
                    "thefted",
                    "fillings_count",
                    "thefts_count"
                ],
                "total": [
                    "",
                    "Итого",
                    "0.00 км",
                    "0:00:00",
                    "0.00 л",
                    "0.00 л\/100 км",
                    "2.33 л",
                    "0.00 л\/100 км",
                    "440.17 л",
                    "438.00 л",
                    "0.00 л",
                    "0.00 л",
                    "0",
                    "0"
                ],
                "totalRaw": [
                    {
                        "v": 0,
                        "vt": 0
                    },
                    {
                        "v": 0,
                        "vt": 0
                    },
                    {
                        "v": 0,
                        "vt": 10
                    },
                    {
                        "v": 0,
                        "vt": 40
                    },
                    {
                        "v": 0,
                        "vt": 50
                    },
                    {
                        "v": 0,
                        "vt": 51
                    },
                    {
                        "v": 2.33334350586,
                        "vt": 50
                    },
                    {
                        "v": 0,
                        "vt": 51
                    },
                    {
                        "v": 440.166656494,
                        "vt": 54
                    },
                    {
                        "v": 438,
                        "vt": 54
                    },
                    {
                        "v": 0,
                        "vt": 50
                    },
                    {
                        "v": 0,
                        "vt": 50
                    },
                    {
                        "v": 0,
                        "vt": 2
                    },
                    {
                        "v": 0,
                        "vt": 2
                    }
                ]
            },
            {
                "name": "unit_stays",
                "label": "Стоянки",
                "grouping": {
                    "type": "day"
                },
                "flags": 16781585,
                "rows": 1,
                "level": 2,
                "columns": 8,
                "header": [
                    "№",
                    "Группировка",
                    "Начало",
                    "Конец",
                    "Длительность",
                    "Общее время",
                    "Время между",
                    "Положение"
                ],
                "header_type": [
                    "",
                    "",
                    "time_begin",
                    "time_end",
                    "duration",
                    "duration_ival",
                    "duration_prev",
                    "location"
                ],
                "total": [
                    "",
                    "Итого",
                    "00:03:06",
                    "2024-06-13 17:46:36",
                    "12 дней 17:43:30",
                    "12 дней 17:43:30",
                    "0:00:00",
                    ""
                ],
                "totalRaw": [
                    {
                        "v": 0,
                        "vt": 0
                    },
                    {
                        "v": 0,
                        "vt": 0
                    },
                    {
                        "v": 1717178586,
                        "vt": 31
                    },
                    {
                        "v": 1718279196,
                        "vt": 30
                    },
                    {
                        "v": 1100610,
                        "vt": 40
                    },
                    {
                        "v": 1100610,
                        "vt": 40
                    },
                    {
                        "v": 0,
                        "vt": 40
                    },
                    {
                        "v": -348201.3876,
                        "vt": 0
                    }
                ]
            }
        ],
        "attachments": [
            {
                "name": "График Абсолютный пробег",
                "type": "chart",
                "datasets": [
                    "Абсолютный пробег"
                ],
                "axis_y": [
                    "Пробег, км"
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Trips"
                        }
                    ]
                }
            },
            {
                "name": "График",
                "type": "chart",
                "datasets": [
                    "Абсолютный пробег",
                    "Пробег в поездках"
                ],
                "axis_y": [
                    "Пробег, км"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 1,
                            "name": "Trips"
                        }
                    ]
                }
            },
            {
                "name": "График Температура ",
                "type": "chart",
                "datasets": [
                    "Температура двигателя (сглаж.)",
                    "Зажигание"
                ],
                "axis_y": [
                    "Температура, °C",
                    "Вкл\/Выкл"
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*"
                }
            },
            {
                "name": "Скорость- Обороты двигателя ",
                "type": "chart",
                "datasets": [
                    "Скорость, км\/ч",
                    "Обороты двигателя"
                ],
                "axis_y": [
                    "Скорость, км\/ч",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "sensor_mask": "*",
                    "chart_markers": {
                        "f": 0
                    }
                }
            },
            {
                "name": "График пд (Акселератор)",
                "type": "chart",
                "datasets": [
                    "Акселератор (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График пд (Расход топлива)",
                "type": "chart",
                "datasets": [
                    "Расход топлива (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График пд (Расход топлива точ)",
                "type": "chart",
                "datasets": [
                    "Расход топлива точ (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График пд (Скорость)",
                "type": "chart",
                "datasets": [
                    "Скорость (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График пд (Высота)",
                "type": "chart",
                "datasets": [
                    "Высота (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График пд (Пробег)",
                "type": "chart",
                "datasets": [
                    "Пробег (сглаж.)",
                    "Обороты двигателя",
                    "Обороты двигателя (сглаж.)"
                ],
                "axis_y": [
                    " ",
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График уровень топлива",
                "type": "chart",
                "datasets": [
                    "Уровень топлива",
                    "Обработанный уровень топлива",
                    "Зажигание"
                ],
                "axis_y": [
                    "Объем, л",
                    "Вкл\/Выкл"
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 264
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        },
                        {
                            "id": "chart_engine_hours_regions",
                            "color": 16381105,
                            "priority": 4,
                            "name": "Моточасы"
                        }
                    ]
                }
            },
            {
                "name": "График Обороты двигателя",
                "type": "chart",
                "datasets": [
                    "Обороты двигателя (сглаж.)",
                    "Обороты двигателя"
                ],
                "axis_y": [
                    "об\/мин"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Trips"
                        }
                    ]
                }
            },
            {
                "name": "График",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Напряжение"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    "Напряжение, В"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "sensor_mask": "*"
                }
            },
            {
                "name": "График (Акселератор)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Акселератор"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График (Расход топлива)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Расход топлива"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График (Расход топлива точ)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Расход топлива точ"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График (Скорость)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Скорость"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График (Высота)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Высота"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График (Пробег)",
                "type": "chart",
                "datasets": [
                    "Зажигание",
                    "Пробег"
                ],
                "axis_y": [
                    "Вкл\/Выкл",
                    " "
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "chart_markers": {
                        "f": 0
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            },
            {
                "name": "График скорость",
                "type": "chart",
                "datasets": [
                    "Скорость, км\/ч",
                    "Скорость (сглаж.), км\/ч"
                ],
                "axis_y": [
                    "Скорость, км\/ч"
                ],
                "axis_x": "Время",
                "flags": 532,
                "p": {
                    "sensor_mask": "*"
                }
            },
            {
                "name": "График уровень топлива",
                "type": "chart",
                "datasets": [
                    "Уровень топлива",
                    "Обработанный уровень топлива",
                    "Напряжение"
                ],
                "axis_y": [
                    "Объем, л",
                    "Напряжение, В"
                ],
                "axis_x": "Время",
                "flags": 20,
                "p": {
                    "chart_markers": {
                        "f": 264
                    },
                    "sensor_mask": "*",
                    "chart_regions": [
                        {
                            "id": "chart_trips_regions",
                            "color": 16766408,
                            "priority": 5,
                            "name": "Поездки"
                        }
                    ]
                }
            }
        ]
    },
    "reportLayer": {
        "name": "report unit_msgs",
        "bounds": [
            0,
            0,
            0,
            0
        ],
        "units": []
    },
    "layerCount": 2
}