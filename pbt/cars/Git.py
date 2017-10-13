from os import getenv

from pbt.core import Car, run


def _is_git_dir():
    rc, _, _ = run(['git', 'rev-parse', '--git-dir'])

    return rc == 0


def _get_head(display):
    if not display:
        return ''

    # Get branch name
    rc, out, _ = run(['git', 'symbolic-ref', 'HEAD'])

    if rc:
        # Get tag name
        rc, out, _ = run(
            ['git', 'describe', '--tags', '--exact-match', 'HEAD'])

        if rc:
            # Get commit ID
            rc, out, _ = run(['git', 'rev-parse', '--short', 'HEAD'])

    return out.replace('refs/heads/', '')


def _is_dirty(display):
    if not display:
        return False

    _, out, _ = run(['git', 'status', '--porcelain'])

    return len(out) > 0


def _compare_remote(display, ahead):
    if not display:
        return False

    ret = False

    # Get branch name
    rc, branch, _ = run(['git', 'symbolic-ref', 'HEAD'])

    if not rc:
        branch = branch.replace('refs/heads/', '')

        if ahead:
            direction = 'origin/%s..HEAD' % branch
        else:
            direction = 'HEAD..origin/%s' % branch

        rc, out, _ = run(['git', 'rev-list', direction])

        if not rc and len(out) > 0:
            ret = True

    return ret


class GitCar(Car):
    default_root_bg = 'light_gray'
    default_root_fg = 'black'
    default_root_fm = 'none'
    default_icon_bg = default_root_bg
    default_icon_fg = default_root_fg
    default_icon_fm = default_root_fm
    default_head_bg = default_root_bg
    default_head_fg = default_root_fg
    default_head_fm = default_root_fm
    default_status_bg = default_root_bg
    default_status_fg = default_root_fg
    default_status_fm = default_root_fm
    default_dirty_bg = default_root_bg
    default_dirty_fg = 'red'
    default_dirty_fm = default_root_fm
    default_clean_bg = default_root_bg
    default_clean_fg = 'green'
    default_clean_fm = default_root_fm
    default_ahead_bg = default_root_bg
    default_ahead_fg = default_root_fg
    default_ahead_fm = default_root_fm
    default_behind_bg = default_root_bg
    default_behind_fg = default_root_fg
    default_behind_fm = default_root_fm

    display = getenv('PBT_CAR_GIT_DISPLAY', _is_git_dir())

    model = {
        'root': {
            'bg': getenv('PBT_CAR_GIT_BG', default_root_bg),
            'fg': getenv('PBT_CAR_GIT_FG', default_root_fg),
            'fm': getenv('PBT_CAR_GIT_FM', default_root_fm),
            'text': getenv(
                'PBT_CAR_GIT_FORMAT',
                ' {{ Icon }} {{ Head }} {{ Status }}{{ Ahead }}{{ Behind }} '),
        },
        'Icon': {
            'bg': getenv(
                'PBT_CAR_GIT_ICON_BG', getenv(
                    'PBT_CAR_GIT_BG', default_icon_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_ICON_FG', getenv(
                    'PBT_CAR_GIT_FG', default_icon_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_ICON_FM', getenv(
                    'PBT_CAR_GIT_FM', default_icon_fm)),
            'text': getenv('PBT_CAR_GIT_ICON_TEXT', ''),
        },
        'Head': {
            'bg': getenv(
                'PBT_CAR_GIT_HEAD_BG', getenv(
                    'PBT_CAR_GIT_BG', default_head_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_HEAD_FG', getenv(
                    'PBT_CAR_GIT_FG', default_head_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_HEAD_FM', getenv(
                    'PBT_CAR_GIT_FM', default_head_fm)),
            'text': getenv('PBT_CAR_GIT_HEAD_TEXT', _get_head(display)),
        },
        'Status': {
            'bg': getenv(
                'PBT_CAR_GIT_STATUS_BG', getenv(
                    'PBT_CAR_GIT_BG', default_status_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_STATUS_FG', getenv(
                    'PBT_CAR_GIT_FG', default_status_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_STATUS_FM', getenv(
                    'PBT_CAR_GIT_FM', default_status_fm)),
            'text': getenv(
                'PBT_CAR_GIT_STATUS_FORMAT',
                '{{ ' + ('Dirty' if _is_dirty(display) else 'Clean') + ' }}'),
        },
        'Dirty': {
            'bg': getenv(
                'PBT_CAR_GIT_DIRTY_BG', getenv(
                    'PBT_CAR_GIT_BG', default_dirty_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_DIRTY_FG', getenv(
                    'PBT_CAR_GIT_FG', default_dirty_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_DIRTY_FM', getenv(
                    'PBT_CAR_GIT_FM', default_dirty_fm)),
            'text': getenv('PBT_CAR_GIT_DIRTY_TEXT', '✘'),
        },
        'Clean': {
            'bg': getenv(
                'PBT_CAR_GIT_CLEAN_BG', getenv(
                    'PBT_CAR_GIT_BG', default_clean_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_CLEAN_FG', getenv(
                    'PBT_CAR_GIT_FG', default_clean_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_CLEAN_FM', getenv(
                    'PBT_CAR_GIT_FM', default_clean_fm)),
            'text': getenv('PBT_CAR_GIT_CLEAN_TEXT', '✔'),
        },
        'Ahead': {
            'bg': getenv(
                'PBT_CAR_GIT_AHEAD_BG', getenv(
                    'PBT_CAR_GIT_BG', default_ahead_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_AHEAD_FG', getenv(
                    'PBT_CAR_GIT_FG', default_ahead_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_AHEAD_FM', getenv(
                    'PBT_CAR_GIT_FM', default_ahead_fm)),
            'text': getenv(
                'PBT_CAR_GIT_AHEAD_TEXT',
                getenv('PBT_CAR_GIT_BEHIND_SYMBOL', ' ⬆') if (
                    _compare_remote(display, True)
                ) else ''),
        },
        'Behind': {
            'bg': getenv(
                'PBT_CAR_GIT_BEHIND_BG', getenv(
                    'PBT_CAR_GIT_BG', default_behind_bg)),
            'fg': getenv(
                'PBT_CAR_GIT_BEHIND_FG', getenv(
                    'PBT_CAR_GIT_FG', default_behind_fg)),
            'fm': getenv(
                'PBT_CAR_GIT_BEHIND_FM', getenv(
                    'PBT_CAR_GIT_FM', default_behind_fm)),
            'text': getenv(
                'PBT_CAR_GIT_BEHIND_TEXT',
                getenv('PBT_CAR_GIT_BEHIND_SYMBOL', ' ⬇') if (
                    _compare_remote(display, False)
                ) else ''),
        },
    }
