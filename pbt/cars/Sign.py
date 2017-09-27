from os import getenv, getuid

from pbt.core import Car


class SignCar(Car):
    model = {
        'root': {
            'bg': getenv('PBT_CAR_SIGN_BG', 'default'),
            'fg': getenv('PBT_CAR_SIGN_FG', 'default'),
            'format': getenv('PBT_CAR_SIGN_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                    'PBT_CAR_SIGN_BG', 'default')),
            'fg': getenv(
                'PBT_CAR_SIGN_SYMBOL_FG', getenv(
                    'PBT_CAR_SIGN_FG', 'default')),
            'text': getenv(
                'PBT_CAR_SIGN_SIGN_FORMAT',
                '{{ %s }}' % ('Root' if getuid() == 0 else 'User')),
        },
        'User': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', 'default'))),
            'fg': getenv('PBT_CAR_SIGN_USER_FG', 'light_green'),
            'text': getenv('PBT_CAR_SIGN_USER_FORMAT', '$'),
        },
        'Root': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', 'default'))),
            'fg': getenv('PBT_CAR_SIGN_ROOT_FG', 'red'),
            'text': getenv('PBT_CAR_SIGN_ROOT_TEXT', '#'),
        },
    }
