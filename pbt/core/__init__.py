from os import getenv
from os.path import basename
from re import compile, match
from subprocess import Popen, PIPE


SHELL = getenv('PBT_SHELL', basename(getenv('SHELL', 'zsh')))


def run(args):
    rc = 1
    out = ''
    err = ''

    try:
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
    except Exception as e:
        proc = None
        err = e

    if proc is not None:
        out, err = proc.communicate()
        rc = proc.returncode

    return rc, out.decode('utf-8').strip(), err.decode('utf-8').strip()


class Car:
    colors = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'light_gray': 7,
        'dark_gray': 8,
        'light_red': 9,
        'light_green': 10,
        'light_yellow': 11,
        'light_blue': 12,
        'light_magenta': 13,
        'light_cyan': 14,
        'white': 15,
    }

    def __init__(self):
        bool_true = [True, '1', 'yes', 'Yes', 'YES', 'true', 'True', 'TRUE']

        if self.display is True or self.display in bool_true:
            self.display = True
        else:
            self.display = False

    def format(self):
        if not self.display:
            return ''

        pattern = compile('{{\s*(\w+)\s*}}')
        text = ("%s%s%s" % (
            self._color_start('root'),
            self.model['root']['text'],
            self._color_end()))

        # Allow element nesting to the depth of 10
        for n in range(10):
            match = pattern.search(text)

            if match:
                text = pattern.sub(self._elemrepl, text)
            else:
                break

        return text

    def _elemrepl(self, matchobj):
        if matchobj.group(1) not in self.model:
            return matchobj.group(0)

        return ("%s%s%s%s" % (
            self._color_end(),
            self._color_start(matchobj.group(1)),
            self._color_end(),
            self._color_start('root')))

    def _color_start(self, element=None, bg=None, fg=None, text=None):
        if element is not None:
            e = self.model[element]
            text = e['text'] if 'text' in e and element != 'root' else ''

            fg = self._get_color(e['fg'], True)
            bg = self._get_color(e['bg'], False)

        if SHELL == 'zsh':
            return '%%{%s%%}%%{%s%%}%s' % (fg, bg, text)
        else:
            return '%s%s%s' % (fg, bg, text)

    def _color_end(self):
        return '' if SHELL == 'zsh' else '\x1b[00m'

    def _get_color(self, name, fg):
        if fg:
            if SHELL == 'zsh':
                kind = 'F'
            else:
                kind = 3
        else:
            if SHELL == 'zsh':
                kind = 'K'
            else:
                kind = 4

        if name == 'default':
            # Default
            if SHELL == 'zsh':
                seq = '%%%s' % kind.lower()
            else:
                seq = '\x1b[%s9m' % kind
        else:
            if name in self.colors:
                # Named color
                if SHELL == 'zsh':
                    seq = '%%%s{%s}' % (kind, self.colors[name])
                else:
                    seq = '\x1b[%s8;5;%sm' % (kind, self.colors[name])
            elif match(r'^\d{1,3}$', name):
                # Color number
                if SHELL == 'zsh':
                    seq = '%%%s{%s}' % (kind, name)
                else:
                    seq = '\x1b[%s8;5;%sm' % (kind, name)
            elif (
                    match(r'^\d{1,3};\d{1,3};\d{1,3}$', name) and
                    SHELL != 'zsh'):
                # RGB color
                seq = '\x1b[%s8;2;%sm' % (kind, name)
            else:
                # If anything else, use default
                if SHELL == 'zsh':
                    seq = '%%%s' % kind.lower()
                else:
                    seq = '\x1b[%s9m' % kind

        return seq
