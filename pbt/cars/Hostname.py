from os import getenv, getuid, uname
from pwd import getpwuid

from pbt.core import Car


class HostnameCar(Car):
    model = {
        'root': {
            'bg': getenv('PBT_CAR_HOSTNAME_BG', 'white'),
            'fg': getenv('PBT_CAR_HOSTNAME_FG', 'black'),
            'format': getenv('PBT_CAR_HOSTNAME_FORMAT', " {{ UserHost }} "),
        },
        'UserHost': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                    'PBT_CAR_HOSTNAME_BG', 'white')),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                    'PBT_CAR_HOSTNAME_FG', 'black')),
            'text': getenv(
                'PBT_CAR_HOSTNAME_USERHOST_TEXT', '{{ User }}@{{ Host }}'),
        },
        'User': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_USER_BG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                        'PBT_CAR_HOSTNAME_BG', 'white'))),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_USER_FG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                        'PBT_CAR_HOSTNAME_FG', 'black'))),
            'text': getenv(
                'PBT_CAR_HOSTNAME_USER_FORMAT', getpwuid(getuid())[0]),
        },
        'Host': {
            'bg': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_BG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_BG', getenv(
                        'PBT_CAR_HOSTNAME_BG', 'white')),),
            'fg': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_FG', getenv(
                    'PBT_CAR_HOSTNAME_USERHOST_FG', getenv(
                        'PBT_CAR_HOSTNAME_FG', 'black'))),
            'text': getenv(
                'PBT_CAR_HOSTNAME_HOSTNAME_TEXT', uname()[1]),
        },
    }
