# -*- coding: utf-8 -*-

from os import getenv
from os.path import basename

from pbt.core import Car


class PyVirtEnvCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', '222')
    default_root_fg = getenv('PBT_CAR_FG', 'black')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_icon_bg = default_root_bg
    default_icon_fg = '33'
    default_icon_fm = default_root_fm
    default_name_bg = default_root_bg
    default_name_fg = default_root_fg
    default_name_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_PYVIRTENV_BG', default_root_bg),
            'fg': getenv('PBT_CAR_PYVIRTENV_FG', default_root_fg),
            'fm': getenv('PBT_CAR_PYVIRTENV_FM', default_root_fm),
            'text': getenv(
                'PBT_CAR_PYVIRTENV_FORMAT',
                ' {{ Icon }} {{ Name }} '),
        },
        'Icon': {
            'bg': getenv(
                'PBT_CAR_PYVIRTENV_ICON_BG', getenv(
                    'PBT_CAR_PYVIRTENV_BG', default_icon_bg)),
            'fg': getenv(
                'PBT_CAR_PYVIRTENV_ICON_FG', getenv(
                    'PBT_CAR_PYVIRTENV_FG', default_icon_fg)),
            'fm': getenv(
                'PBT_CAR_PYVIRTENV_ICON_FM', getenv(
                    'PBT_CAR_PYVIRTENV_FM', default_icon_fm)),
            'text': getenv('PBT_CAR_PYVIRTENV_ICON_TEXT', ''),
        },
        'Name': {
            'bg': getenv(
                'PBT_CAR_PYVIRTENV_NAME_BG', getenv(
                    'PBT_CAR_PYVIRTENV_BG', default_name_bg)),
            'fg': getenv(
                'PBT_CAR_PYVIRTENV_NAME_FG', getenv(
                    'PBT_CAR_PYVIRTENV_FG', default_name_fg)),
            'fm': getenv(
                'PBT_CAR_PYVIRTENV_NAME_FM', getenv(
                    'PBT_CAR_PYVIRTENV_FM', default_name_fm)),
            'text': getenv(
                'PBT_CAR_PYVIRTENV_NAME_TEXT',
                basename(getenv('VIRTUAL_ENV', ''))),
        },
    }

    display = getenv(
        'PBT_CAR_PYVIRTENV_DISPLAY',
        True
        if getenv('VIRTUAL_ENV', '')
        else False)
    wrap = getenv('PBT_CAR_PYVIRTENV_WRAP', False)
    sep = getenv('PBT_CAR_PYVIRTENV_SEP', None)
