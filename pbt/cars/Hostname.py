from os import getenv, getuid, uname
from pwd import getpwuid

from pbt.core import Car


class HostnameCar(Car):
    default_root_bg = 'dark_gray'
    default_root_fg = '252'
    default_userhost_bg = default_root_bg
    default_userhost_fg = default_root_fg
    default_user_bg = default_root_bg
    default_user_fg = default_root_fg
    default_host_bg = default_root_bg
    default_host_fg = default_root_fg

    model = {
        'root': {
            'bg': getenv('PBT_CAR_HOSTNAME_BG', 'dark_gray'),
            'fg': getenv('PBT_CAR_HOSTNAME_FG', '252'),
            'text': getenv('PBT_CAR_HOSTNAME_FORMAT', ' {{ UserHost }} '),
        },
        'UserHost': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                    'PBT_CAR_HOSTNAME_BG', default_userhost_bg)),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                    'PBT_CAR_HOSTNAME_FG', default_userhost_fg)),
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
            'text': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_TEXT', uname()[1]),
        },
    }

    display = getenv('PBT_CAR_HOSTNAME_DISPLAY', True)
