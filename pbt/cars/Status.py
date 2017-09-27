from os import getenv
from sys import argv

from pbt.core import Car


class StatusCar(Car):
    model = {
        'root': {
            'bg': getenv('PBT_CAR_STATUS_BG', 'red'),
            'fg': getenv('PBT_CAR_STATUS_FG', 'light_gray'),
            'format': getenv('PBT_CAR_STATUS_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_STATUS_SYMBOL_BG', getenv(
                    'PBT_CAR_STATUS_BG', 'red')),
            'fg': getenv(
                'PBT_CAR_STATUS_SYMBOL_FG', getenv(
                    'PBT_CAR_STATUS_FG', 'light_gray')),
            'text': getenv(
                'PBT_CAR_STATUS_SYMBOL_TEXT', (
                    '{{ ' + (
                        'Ok'
                        if len(argv) > 1 and argv[1] == '0'
                        else
                        'Error'
                    ) + ' }}'
                )
            ),
        },
        'Error': {
            'bg': getenv(
                'PBT_CAR_STATUS_ERROR_BG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_BG', getenv(
                        'PBT_CAR_STATUS_BG', 'red'))),
            'fg': getenv(
                'PBT_CAR_STATUS_ERROR_FG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_FG', getenv(
                        'PBT_CAR_STATUS_FG', 'light_gray'))),
            'text': getenv('PBT_CAR_STATUS_ERROR_TEXT', '\u2718'),
        },
        'Ok': {
            'bg': getenv('PBT_CAR_STATUS_OK_BG', 'orange'),
            'fg': getenv('PBT_CAR_STATUS_OK_FG', 'green'),
            'text': getenv('PBT_CAR_STATUS_OK_TEXT', '\u2718'),
        },
    }

    display = (
        False
        if (
            len(argv) == 1 or (
                len(argv) > 1 and
                argv[1] == '0'
            )
        ) else
        True)
