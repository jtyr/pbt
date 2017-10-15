# -*- coding: utf-8 -*-

from os import getenv
from platform import system

from pbt.core import Car


SYMBOLS = {
    'arch': '',
    'centos': '',
    'coreos': '',
    'darwin': '',
    'debian': '',
    'docker': '',
    'elementary': '',
    'fedora': '',
    'freebsd': '',
    'gentoo': '',
    'linux': '',
    'linuxmint': '',
    'mageia': '',
    'mandriva': '',
    'opensuse': '',
    'raspbian': '',
    'redhat': '',
    'sabayon': '',
    'slackware': '',
    'ubuntu': '',
    'windows': '',
}


def _get_os_symbol():
    name = getenv('PBT_CAR_OS_NAME', system()).lower()
    ret = None

    if name and name in SYMBOLS:
        ret = SYMBOLS[name]
    else:
        ret = "?"

    return ret


class OsCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', '235')
    default_root_fg = getenv('PBT_CAR_FG', 'white')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_symbol_bg = default_root_bg
    default_symbol_fg = default_root_fg
    default_symbol_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_OS_BG', default_root_bg),
            'fg': getenv('PBT_CAR_OS_FG', default_root_fg),
            'fm': getenv('PBT_CAR_OS_FM', default_root_fm),
            'text': getenv('PBT_CAR_OS_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_OS_SYMBOL_BG', getenv(
                    'PBT_CAR_OS_BG', default_symbol_bg)),
            'fg': getenv(
                'PBT_CAR_OS_SYMBOL_FG', getenv(
                    'PBT_CAR_OS_FG', default_symbol_fg)),
            'fm': getenv(
                'PBT_CAR_OS_SYMBOL_FM', getenv(
                    'PBT_CAR_OS_FM', default_symbol_fm)),
            'text': getenv(
                'PBT_CAR_OS_SYMBOL_TEXT', _get_os_symbol()),
        },
    }

    display = getenv('PBT_CAR_OS_DISPLAY', True)
    wrap = getenv('PBT_CAR_OS_WRAP', False)
    sep = getenv('PBT_CAR_OS_SEP', None)
