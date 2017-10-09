from os import getcwd, getenv, sep
from os.path import expanduser

from pbt.core import Car


def _get_dir():
    pwd = getcwd()
    dirs = pwd.split(sep)

    if len(dirs) == 2:
        ret = sep
    elif pwd == expanduser('~'):
        ret = '~'
    elif len(dirs) > 1:
        ret = dirs[-1]

    return ret


class DirCar(Car):
    default_root_bg = 'blue'
    default_root_fg = 'light_gray'
    default_dir_bg = default_root_bg
    default_dir_fg = default_root_fg

    model = {
        'root': {
            'bg': getenv('PBT_CAR_DIR_BG', default_root_bg),
            'fg': getenv('PBT_CAR_DIR_FG', default_root_fg),
            'text': getenv('PBT_CAR_DIR_FORMAT', ' {{ Dir }} '),
        },
        'Dir': {
            'bg': getenv(
                'PBT_CAR_DIR_DIR_BG', getenv(
                    'PBT_CAR_DIR_BG', default_dir_bg)),
            'fg': getenv(
                'PBT_CAR_DIR_DIR_FG', getenv(
                    'PBT_CAR_DIR_FG', default_dir_fg)),
            'text': getenv('PBT_CAR_DIR_DIR_TEXT', _get_dir()),
        },
    }

    display = getenv('PBT_CAR_DIR_DISPLAY', True)
