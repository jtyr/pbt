from os import getenv, getuid

from pbt.core import Car


class SignCar(Car):
    default_root_bg = 'default'
    default_root_fg = 'default'
    default_symbol_bg = default_root_bg
    default_symbol_fg = default_root_fg
    default_user_bg = default_root_bg
    default_admin_bg = default_root_bg

    model = {
        'root': {
            'bg': getenv('PBT_CAR_SIGN_BG', 'default'),
            'fg': getenv('PBT_CAR_SIGN_FG', 'default'),
            'text': getenv('PBT_CAR_SIGN_FORMAT', ' {{ Symbol }} '),
        },
        'Symbol': {
            'bg': getenv(
                'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                    'PBT_CAR_SIGN_BG', default_symbol_bg)),
            'fg': getenv(
                'PBT_CAR_SIGN_SYMBOL_FG', getenv(
                    'PBT_CAR_SIGN_FG', default_symbol_fg)),
            'text': getenv(
                'PBT_CAR_SIGN_SIGN_FORMAT',
                '{{ %s }}' % ('Admin' if getuid() == 0 else 'User')),
        },
        'User': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', default_user_bg))),
            'fg': getenv('PBT_CAR_SIGN_USER_FG', 'light_green'),
            'text': getenv('PBT_CAR_SIGN_USER_TEXT', '$'),
        },
        'Admin': {
            'bg': getenv(
                'PBT_CAR_SIGN_USER_BG', getenv(
                    'PBT_CAR_SIGN_SYMBOL_BG', getenv(
                        'PBT_CAR_SIGN_BG', default_admin_bg))),
            'fg': getenv('PBT_CAR_SIGN_ROOT_FG', 'red'),
            'text': getenv('PBT_CAR_SIGN_ROOT_TEXT', '#'),
        },
    }

    display = getenv('PBT_CAR_SIGN_DISPLAY', True)
