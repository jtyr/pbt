# -*- coding: utf-8 -*-

from os import getenv, getuid, uname
from pwd import getpwuid

from pbt.core import Car


class HostnameCar(Car):
    default_root_bg = 'dark_gray'
    default_root_fg = '252'
    default_root_fm = 'none'
    default_userhost_bg = default_root_bg
    default_userhost_fg = default_root_fg
    default_userhost_fm = default_root_fm
    default_user_bg = default_root_bg
    default_user_fg = default_root_fg
    default_user_fm = default_root_fm
    default_host_bg = default_root_bg
    default_host_fg = default_root_fg
    default_host_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_HOSTNAME_BG', default_root_bg),
            'fg': getenv('PBT_CAR_HOSTNAME_FG', default_root_fg),
            'fm': getenv('PBT_CAR_HOSTNAME_FM', default_root_fm),
            'text': getenv('PBT_CAR_HOSTNAME_FORMAT', ' {{ UserHost }} '),
        },
        'UserHost': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                    'PBT_CAR_HOSTNAME_BG', default_userhost_bg)),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                    'PBT_CAR_HOSTNAME_FG', default_userhost_fg)),
            'fm': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_FM', getenv(
                    'PBT_CAR_HOSTNAME_FM', default_userhost_fm)),
            'text': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_FORMAT', '{{ User }}@{{ Host }}'),
        },
        'User': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_USER_BG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                        'PBT_CAR_HOSTNAME_BG', default_user_bg))),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_USER_FG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                        'PBT_CAR_HOSTNAME_FG', default_user_fg))),
            'fm': getenv(
                'PBT_CAR_HOSTNAME_USER_FM', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FM', getenv(
                        'PBT_CAR_HOSTNAME_FM', default_user_fm))),
            'text': getenv(
                'PBT_CAR_HOSTNAME_USER_TEXT', getpwuid(getuid())[0]),
        },
        'Host': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_BG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                        'PBT_CAR_HOSTNAME_BG', default_host_bg))),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_FG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                        'PBT_CAR_HOSTNAME_FG', default_host_fg))),
            'fm': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_FM', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FM', getenv(
                        'PBT_CAR_HOSTNAME_FM', default_host_fm))),
            'text': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_TEXT', uname()[1].split('.')[0]),
        },
    }

    display = getenv('PBT_CAR_HOSTNAME_DISPLAY', True)
