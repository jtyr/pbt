# -*- coding: utf-8 -*-

from time import localtime, strftime
from os import getenv

from pbt.core import Car


class TimeCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', 'light_blue')
    default_root_fg = getenv('PBT_CAR_FG', 'light_gray')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_datetime_bg = default_root_bg
    default_datetime_fg = default_root_fg
    default_datetime_fm = default_root_fm
    default_date_bg = default_root_bg
    default_date_fg = default_root_fg
    default_date_fm = default_root_fm
    default_time_bg = default_root_bg
    default_time_fg = 'light_yellow'
    default_time_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_TIME_BG', default_root_bg),
            'fg': getenv('PBT_CAR_TIME_FG', default_root_fg),
            'fm': getenv('PBT_CAR_TIME_FM', default_root_fm),
            'text': getenv('PBT_CAR_TIME_FORMAT', ' {{ DateTime }} '),
        },
        'DateTime': {
            'bg': getenv(
                'PBT_CAR_TIME_DATETIME_BG', getenv(
                    'PBT_CAR_TIME_BG', default_datetime_bg)),
            'fg': getenv(
                'PBT_CAR_TIME_DATETIME_FG', getenv(
                    'PBT_CAR_TIME_FG', default_datetime_fg)),
            'fm': getenv(
                'PBT_CAR_TIME_DATETIME_FM', getenv(
                    'PBT_CAR_TIME_FM', default_datetime_fm)),
            'text': getenv(
                'PBT_CAR_TIME_DATETIME_FORMAT', '{{ Date }} {{ Time }}'),
        },
        'Date': {
            'bg': getenv(
                'PBT_CAR_TIME_DATE_BG', getenv(
                    'PBT_CAR_TIME_DATETIME_BG', getenv(
                        'PBT_CAR_TIME_BG', default_date_bg))),
            'fg': getenv(
                'PBT_CAR_TIME_DATE_FG', getenv(
                    'PBT_CAR_TIME_DATETIME_FG', getenv(
                        'PBT_CAR_TIME_FG', default_date_fg))),
            'fm': getenv(
                'PBT_CAR_TIME_DATE_FM', getenv(
                    'PBT_CAR_TIME_DATETIME_FM', getenv(
                        'PBT_CAR_TIME_FM', default_date_fm))),
            'text': strftime(getenv(
                'PBT_CAR_TIME_DATE_FORMAT', '%a %d %b'), localtime()),
        },
        'Time': {
            'bg': getenv(
                'PBT_CAR_TIME_TIME_BG', getenv(
                    'PBT_CAR_TIME_DATETIME_BG', getenv(
                        'PBT_CAR_TIME_BG', default_time_bg))),
            'fg': getenv(
                'PBT_CAR_TIME_TIME_FG', getenv(
                    'PBT_CAR_TIME_DATETIME_FG', getenv(
                        'PBT_CAR_TIME_FG', default_time_fg))),
            'fm': getenv(
                'PBT_CAR_TIME_TIME_FM', getenv(
                    'PBT_CAR_TIME_DATETIME_FM', getenv(
                        'PBT_CAR_TIME_FM', default_time_fm))),
            'text': strftime(getenv(
                'PBT_CAR_TIME_TIME_FORMAT', '%H:%M:%S'), localtime()),
        },
    }

    display = getenv('PBT_CAR_TIME_DISPLAY', True)
    wrap = getenv('PBT_CAR_TIME_WRAP', False)
    sep = getenv('PBT_CAR_TIME_SEP', None)
