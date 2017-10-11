from os import getenv

from pbt.core import Car, run


def _is_git_dir():
    rc, _, _ = run(['git', 'rev-parse', '--git-dir'])

    return rc == 0


def _get_head():
    if not _DISPLAY:
        return '-'

    rc, out, _ = run(['git', 'symbolic-ref', 'HEAD'])

    if rc:
        rc, out, _ = run(
            ['git', 'describe', '--tags', '--exact-match', 'HEAD'])

        if rc:
            rc, out, _ = run(['git', 'rev-parse', '--short', 'HEAD'])

    return out.replace('refs/heads/', '')


def _is_dirty():
    _, out, _ = run(['git', 'status', '--porcelain'])

    return len(out) > 0


_DISPLAY = getenv('PBT_CAR_DIR_DISPLAY', _is_git_dir())


class GitCar(Car):
    default_root_bg = 'light_gray'
    default_root_fg = 'black'
    default_icon_bg = default_root_bg
    default_icon_fg = default_root_fg
    default_head_bg = default_root_bg
    default_head_fg = default_root_fg
    default_status_bg = default_root_bg
    default_status_fg = default_root_fg
    default_dirty_bg = default_root_bg
    default_dirty_fg = 'red'
    default_clean_bg = default_root_bg
    default_clean_fg = 'green'

    model = {
        'root': {
            'bg': getenv('PBT_CAR_GIT_BG', default_root_bg),
            'fg': getenv('PBT_CAR_GIT_FG', default_root_fg),
            'text': getenv(
                'PBT_CAR_GIT_FORMAT',
                ' {{ Icon }} {{ Head }} {{ Status }} '),
        },
        'Icon': {
            'bg': getenv(
                'PBT_CAR_GIT_ICON_BG', getenv(
                    'PBT_CAR_GIT_BG', default_icon_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_ICON_FG', getenv(
                    'PBT_CAR_GIT_FG', default_icon_fg)),
            'text': getenv('PBT_CAR_GIT_ICON_TEXT', ''),
        },
        'Head': {
            'bg': getenv(
                'PBT_CAR_GIT_HEAD_BG', getenv(
                    'PBT_CAR_GIT_BG', default_head_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_HEAD_FG', getenv(
                    'PBT_CAR_GIT_FG', default_head_fg)),
            'text': getenv('PBT_CAR_GIT_HEAD_TEXT', _get_head()),
        },
        'Status': {
            'bg': getenv(
                'PBT_CAR_GIT_STATUS_BG', getenv(
                    'PBT_CAR_GIT_BG', default_status_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_STATUS_FG', getenv(
                    'PBT_CAR_GIT_FG', default_status_fg)),
            'text': getenv(
                'PBT_CAR_GIT_STATUS_FORMAT',
                '{{ ' + ('Dirty' if _is_dirty() else 'Clean') + ' }}'),
        },
        'Dirty': {
            'bg': getenv(
                'PBT_CAR_GIT_DIRTY_BG', getenv(
                    'PBT_CAR_GIT_BG', default_dirty_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_DIRTY_FG', getenv(
                    'PBT_CAR_GIT_FG', default_dirty_fg)),
            'text': getenv('PBT_CAR_GIT_DIRTY_TEXT', '✘'),
        },
        'Clean': {
            'bg': getenv(
                'PBT_CAR_GIT_CLEAN_BG', getenv(
                    'PBT_CAR_GIT_BG', default_clean_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_CLEAN_FG', getenv(
                    'PBT_CAR_GIT_FG', default_clean_fg)),
            'text': getenv('PBT_CAR_GIT_CLEAN_TEXT', '✔'),
        },
    }

    display = _DISPLAY
