from time import gmtime, strftime
from os import getenv

from pbt.core import Car


class TimeCar(Car):
    model = {
        'root': {
            'bg': getenv('PBT_CAR_TIME_BG', 'light_blue'),
            'fg': getenv('PBT_CAR_TIME_FG', 'light_gray'),
            'format': getenv('PBT_CAR_TIME_FORMAT', " {{ DateTime }} "),
        },
        'DateTime': {
            'bg': getenv(
                'PBT_CAR_TIME_DATETIME_BG', getenv(
                    'PBT_CAR_TIME_BG', 'light_blue')),
            'fg': getenv(
                'PBT_CAR_TIME_DATETIME_FG', getenv(
                    'PBT_CAR_TIME_FG', 'light_gray')),
            'text': getenv(
                'PBT_CAR_TIME_DATETIME_TEXT', '{{ Date }} {{ Time }}'),
        },
        'Date': {
            'bg': getenv(
                'PBT_CAR_TIME_DATE_BG', getenv(
                    'PBT_CAR_TIME_DATETIME_BG', getenv(
                        'PBT_CAR_TIME_BG', 'light_blue'))),
            'fg': getenv(
                'PBT_CAR_TIME_DATE_FG', getenv(
                    'PBT_CAR_TIME_DATETIME_FG', getenv(
                        'PBT_CAR_TIME_FG', 'light_gray'))),
            'text': strftime(getenv(
                'PBT_CAR_TIME_DATE_FORMAT', '%a %d %b'), gmtime()),
        },
        'Time': {
            'bg': getenv(
                'PBT_CAR_TIME_TIME_BG', getenv(
                    'PBT_CAR_TIME_DATETIME_BG', getenv(
                        'PBT_CAR_TIME_BG', 'light_blue'))),
            'fg': getenv(
                'PBT_CAR_TIME_TIME_FG', getenv(
                    'PBT_CAR_TIME_DATETIME_FG', getenv(
                        'PBT_CAR_TIME_FG', 'light_yellow'))),
            'text': strftime(getenv(
                'PBT_CAR_TIME_TIME_FORMAT', '%H:%M:%S'), gmtime()),
        },
    }
