# -*- coding: utf-8 -*-

from os import getenv

from pbt.core import Car


class CustomCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', 'yellow')
    default_root_fg = getenv('PBT_CAR_FG', 'default')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_text_bg = default_root_bg
    default_text_fg = default_root_fg
    default_text_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_CUSTOM_BG', default_root_bg),
            'fg': getenv('PBT_CAR_CUSTOM_FG', default_root_fg),
            'fm': getenv('PBT_CAR_CUSTOM_FM', default_root_fm),
            'text': getenv('PBT_CAR_CUSTOM_FORMAT', ' {{ Text }} '),
        },
        'Text': {
            'bg': getenv(
                'PBT_CAR_CUSTOM_TEXT_BG', getenv(
                    'PBT_CAR_CUSTOM_BG', default_text_bg)),
            'fg': getenv(
                'PBT_CAR_CUSTOM_TEXT_FG', getenv(
                    'PBT_CAR_CUSTOM_FG', default_text_fg)),
            'fm': getenv(
                'PBT_CAR_CUSTOM_TEXT_FM', getenv(
                    'PBT_CAR_CUSTOM_FM', default_text_fm)),
            'text': getenv('PBT_CAR_CUSTOM_TEXT', '?'),
        },
    }

    display = getenv('PBT_CAR_TEXT_DISPLAY', True)
    wrap = getenv('PBT_CAR_TEXT_WRAP', False)
    sep = getenv('PBT_CAR_TEXT_SEP', None)
