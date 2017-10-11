from time import gmtime, strftime
from os import getenv

from pbt.core import Car


class TimeCar(Car):
    default_root_bg = 'light_blue'
    default_root_fg = 'light_gray'
    default_datetime_bg = default_root_bg
    default_datetime_fg = default_root_fg
    default_date_bg = default_root_bg
    default_date_fg = default_root_fg
    default_time_bg = default_root_bg

    model = {
        'root': {
            'bg': getenv('PBT_CAR_TIME_BG', default_root_bg),
            'fg': getenv('PBT_CAR_TIME_FG', default_root_fg),
            'text': getenv('PBT_CAR_TIME_FORMAT', ' {{ DateTime }} '),
        },
        'DateTime': {
            'bg': getenv(
                'PBT_CAR_TIME_DATETIME_BG', getenv(
                    'PBT_CAR_TIME_BG', default_datetime_bg)),
            'fg': getenv(
                'PBT_CAR_TIME_DATETIME_FG', getenv(
                    'PBT_CAR_TIME_FG', default_datetime_fg)),
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
            'text': strftime(getenv(
                'PBT_CAR_TIME_DATE_FORMAT', '%a %d %b'), gmtime()),
        },
        'Time': {
            'bg': getenv(
                'PBT_CAR_TIME_TIME_BG', getenv(
                    'PBT_CAR_TIME_DATETIME_BG', getenv(
                        'PBT_CAR_TIME_BG', default_time_bg))),
            'fg': getenv(
                'PBT_CAR_TIME_TIME_FG', getenv(
                    'PBT_CAR_TIME_DATETIME_FG', getenv(
                        'PBT_CAR_TIME_FG', 'light_yellow'))),
            'text': strftime(getenv(
                'PBT_CAR_TIME_TIME_FORMAT', '%H:%M:%S'), gmtime()),
        },
    }

    display = getenv('PBT_CAR_TIME_DISPLAY', True)
