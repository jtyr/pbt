# -*- coding: utf-8 -*-

from os import getcwd, getenv, sep
from os.path import expanduser

from pbt.core import BOOL_TRUE, Car


def _get_dir():
    pwd = getenv('PWD', getcwd())
    dirsep = getenv('PBT_CAR_DIR_DIRSEP', sep)
    userdir_sign = getenv('PBT_CAR_DIR_HOMESIGN', '~')

    if userdir_sign:
        pwd = pwd.replace(expanduser('~'), userdir_sign)

    dirs = pwd.split(sep)
    depth = int(getenv('PBT_CAR_DIR_DEPTH', 1))

    if pwd == sep:
        ret = sep_repl
    elif pwd == '~':
        ret = pwd
    elif len(dirs) > 1:
        ret = dirsep.join(dirs[(-1 * depth):])
    else:
        ret = dirsep.join(dirs)

    return ret


class DirCar(Car):
    default_root_bg = getenv('PBT_CAR_BG', 'blue')
    default_root_fg = getenv('PBT_CAR_FG', 'light_gray')
    default_root_fm = getenv('PBT_CAR_FM', 'none')
    default_dir_bg = default_root_bg
    default_dir_fg = default_root_fg
    default_dir_fm = default_root_fm

    model = {
        'root': {
            'bg': getenv('PBT_CAR_DIR_BG', default_root_bg),
            'fg': getenv('PBT_CAR_DIR_FG', default_root_fg),
            'fm': getenv('PBT_CAR_DIR_FM', default_root_fm),
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
    wrap = getenv('PBT_CAR_DIR_WRAP', False)
    sep = getenv('PBT_CAR_DIR_SEP', None)
