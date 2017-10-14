# -*- coding: utf-8 -*-

from os import getenv
from time import time as ttime

from pbt.core import Car


def _get_time():
    precision = int(getenv('PBT_CAR_EXECTIME_PRECISION', 0))
    now = ttime()
    execs = now - float(getenv('PBT_CAR_EXECTIME_SECS', now))

    if precision > 0:
        subsecs = ".%s" % int((execs - int(execs)) * 10**precision)
        subsecs += '0' * (precision - len(subsecs) + 1)
    else:
        subsecs = ''

    hours = int(execs/3600)
    mins = int((execs - hours)/60)
    secs = int(execs - hours*3600 - mins*60)

    exectime = "%.2d:%.2d:%02d%s" % (hours, mins, secs, subsecs)

    return exectime


class ExecTimeCar(Car):
    default_root_bg = 'light_gray'
    default_root_fg = 'black'
    default_root_fm = 'none'
    default_exectime_bg = default_root_bg
    default_exectime_fg = default_root_fg
    default_exectime_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_EXECTIME_BG', default_root_bg),
            'fg': getenv('PBT_CAR_EXECTIME_FG', default_root_fg),
            'fm': getenv('PBT_CAR_EXECTIME_FG', default_root_fm),
            'text': getenv('PBT_CAR_EXECTIME_FORMAT', ' {{ Time }} '),
        },
        'Time': {
            'bg': getenv(
                'PBT_CAR_EXECTIME_TIME_BG', getenv(
                    'PBT_CAR_EXECTIME_BG', default_exectime_bg)),
            'fg': getenv(
                'PBT_CAR_EXECTIME_TIME_FG', getenv(
                    'PBT_CAR_EXECTIME_FG', default_exectime_fg)),
            'fm': getenv(
                'PBT_CAR_EXECTIME_TIME_FM', getenv(
                    'PBT_CAR_EXECTIME_FM', default_exectime_fm)),
            'text': getenv('PBT_CAR_EXECTIME_TIME_TEXT', _get_time()),
        },
    }

    display = getenv('PBT_CAR_EXECTIME_DISPLAY', True)
