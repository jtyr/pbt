from os import getcwd, getenv, sep
from os.path import expanduser

from pbt.core import Car


def _getDir():
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
    model = {
        'root': {
            'bg': getenv('PBT_CAR_SIGN_BG', 'blue'),
            'fg': getenv('PBT_CAR_SIGN_FG', 'light_gray'),
            'format': getenv('PBT_CAR_SIGN_FORMAT', ' {{ Dir }} '),
        },
        'Dir': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_BG', 'blue')),
            'fg': getenv(
                'PBT_CAR_SIGN_USER_FG', getenv(
                    'PBT_CAR_SIGN_FG', 'light_gray')),
            'text': getenv('PBT_CAR_SIGN_USER_FORMAT', _getDir()),
        },
    }
