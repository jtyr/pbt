# -*- coding: utf-8 -*-

from os import getcwd, getenv, sep
from os.path import expanduser

from pbt.core import BOOL_TRUE, Car


def _get_dir():
    pwd = getenv('PWD', getcwd())
    sep_repl = getenv('PBT_CAR_DIR_SEP', sep)

    if getenv('PBT_CAR_DIR_HOME', True) in BOOL_TRUE:
        pwd = pwd.replace(expanduser('~'), '~')

    dirs = pwd.split(sep)
    depth = int(getenv('PBT_CAR_DIR_DEPTH', 1))

    if pwd == sep:
        ret = sep_repl
    elif pwd == '~':
        ret = pwd
    elif len(dirs) > 1:
        ret = sep_repl.join(dirs[(-1 * depth):])
    else:
        ret = sep_repl.join(dirs)

    return ret


class DirCar(Car):
    default_root_bg = 'blue'
    default_root_fg = 'light_gray'
    default_root_fm = 'none'
    default_dir_bg = default_root_bg
    default_dir_fg = default_root_fg
    default_dir_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_DIR_BG', default_root_bg),
            'fg': getenv('PBT_CAR_DIR_FG', default_root_fg),
            'fm': getenv('PBT_CAR_DIR_FG', default_root_fm),
            'text': getenv('PBT_CAR_DIR_FORMAT', ' {{ Dir }} '),
        },
        'Dir': {
            'bg': getenv(
                'PBT_CAR_DIR_DIR_BG', getenv(
                    'PBT_CAR_DIR_BG', default_dir_bg)),
            'fg': getenv(
                'PBT_CAR_DIR_DIR_FG', getenv(
                    'PBT_CAR_DIR_FG', default_dir_fg)),
            'fm': getenv(
                'PBT_CAR_DIR_DIR_FM', getenv(
                    'PBT_CAR_DIR_FM', default_dir_fm)),
            'text': getenv('PBT_CAR_DIR_DIR_TEXT', _get_dir()),
        },
    }

    display = getenv('PBT_CAR_DIR_DISPLAY', True)
