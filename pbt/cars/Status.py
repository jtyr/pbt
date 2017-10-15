# -*- coding: utf-8 -*-

from os import getenv
from sys import argv

from pbt.core import Car


def _is_ok():
    if len(argv) == 1 or (len(argv) > 1 and argv[1] == '0'):
        ret = True
    else:
        ret = False

    return ret


class StatusCar(Car):
    default_error_bg = 'red'
    default_error_fg = 'light_gray'
    default_error_fm = 'none'
    default_ok_bg = 'green'
    default_ok_fg = 'light_gray'
    default_ok_fm = 'none'
    default_root_bg = getenv(
        'PBT_CAR_BG',
        default_ok_bg if _is_ok() else default_error_bg)
    default_root_fg = getenv(
        'PBT_CAR_FG',
        default_ok_fg if _is_ok() else default_error_fg)
    default_root_fm = getenv(
        'PBT_CAR_FM',
        default_ok_fg if _is_ok() else default_error_fm)
    default_symbol_bg = default_root_bg
    default_symbol_fg = default_root_fg
    default_symbol_fm = default_root_fm
    default_code_bg = default_root_bg
    default_code_fg = default_root_fg
    default_code_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_STATUS_BG', default_root_bg),
            'fg': getenv('PBT_CAR_STATUS_FG', default_root_fg),
            'fm': getenv('PBT_CAR_STATUS_FM', default_root_fm),
            'text': getenv('PBT_CAR_STATUS_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_STATUS_SYMBOL_BG', getenv(
                    'PBT_CAR_STATUS_BG', default_symbol_bg)),
            'fg': getenv(
                'PBT_CAR_STATUS_SYMBOL_FG', getenv(
                    'PBT_CAR_STATUS_FG', default_symbol_fg)),
            'fm': getenv(
                'PBT_CAR_STATUS_SYMBOL_FM', getenv(
                    'PBT_CAR_STATUS_FM', default_symbol_fm)),
            'text': getenv(
                'PBT_CAR_STATUS_SYMBOL_FORMAT', (
                    '{{ ' + ('Ok' if _is_ok() else 'Error') + ' }}'
                )
            ),
        },
        'Code': {
            'bg': getenv(
                'PBT_CAR_STATUS_CODE_BG', getenv(
                    'PBT_CAR_STATUS_BG', default_code_bg)),
            'fg': getenv(
                'PBT_CAR_STATUS_CODE_FG', getenv(
                    'PBT_CAR_STATUS_FG', default_code_fg)),
            'fm': getenv(
                'PBT_CAR_STATUS_CODE_FM', getenv(
                    'PBT_CAR_STATUS_FM', default_code_fm)),
            'text': getenv(
                'PBT_CAR_STATUS_CODE_TEXT', argv[1] if len(argv) > 1 else '?'),
        },
        'Error': {
            'bg': getenv(
                'PBT_CAR_STATUS_ERROR_BG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_BG', getenv(
                        'PBT_CAR_STATUS_BG', default_error_bg))),
            'fg': getenv(
                'PBT_CAR_STATUS_ERROR_FG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_FG', getenv(
                        'PBT_CAR_STATUS_FG', default_error_fg))),
            'fm': getenv(
                'PBT_CAR_STATUS_ERROR_FM', getenv(
                    'PBT_CAR_STATUS_SYMBOL_FM', getenv(
                        'PBT_CAR_STATUS_FM', default_error_fm))),
            'text': getenv('PBT_CAR_STATUS_ERROR_TEXT', '✘'),
        },
        'Ok': {
            'bg': getenv(
                'PBT_CAR_STATUS_OK_BG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_BG', getenv(
                        'PBT_CAR_STATUS_BG', default_ok_bg))),
            'fg': getenv(
                'PBT_CAR_STATUS_OK_FG', getenv(
                    'PBT_CAR_STATUS_SYMBOL_FG', getenv(
                        'PBT_CAR_STATUS_FG', default_ok_fg))),
            'fm': getenv(
                'PBT_CAR_STATUS_OK_FM', getenv(
                    'PBT_CAR_STATUS_SYMBOL_FM', getenv(
                        'PBT_CAR_STATUS_FM', default_ok_fm))),
            'text': getenv('PBT_CAR_STATUS_OK_TEXT', '✔'),
        },
    }

    display = getenv('PBT_CAR_STATUS_DISPLAY', False if _is_ok() else True)
    wrap = getenv('PBT_CAR_STATUS_WRAP', False)
    sep = getenv('PBT_CAR_STATUS_SEP', None)
