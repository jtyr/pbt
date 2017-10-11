from os import getenv
from os.path import basename
from re import compile as recompile, match as rematch
from subprocess import Popen, PIPE


SHELL = getenv('PBT_SHELL', basename(getenv('SHELL', 'zsh')))
BOOL_TRUE = [True, '1', 'yes', 'Yes', 'YES', 'true', 'True', 'TRUE']


def run(args):
    rc = 1
    out = ''
    err = ''

    try:
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
    except OSError as e:
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
    model = {}
    display = True

    def __init__(self):
        if self.display is True or self.display in BOOL_TRUE:
            self.display = True
        else:
            self.display = False

    def format(self):
        if not self.display:
            return ''

        pattern = recompile(r'{{\s*(\w+)\s*}}')
        text = ("%s%s" % (
            self.elem_color('root'),
            self.model['root']['text']))

        # Allow element nesting to the depth of 10
        for _ in range(10):
            match = pattern.search(text)

            if match:
                text = pattern.sub(self._elem_replace, text)
            else:
                break

        return text

    def _elem_replace(self, matchobj):
        if matchobj.group(1) not in self.model:
            return matchobj.group(0)

        return ("%s%s" % (
            self.elem_color(matchobj.group(1)),
            self.elem_color('root')))

    def elem_color(self, element=None, bg='', fg='', fm='', text=''):
        if element is not None:
            e = self.model[element]

            if 'text' in e and element != 'root':
                text = e['text']
            else:
                text = ''

            bg = self.get_color(e['bg'], 'bg')
            fg = self.get_color(e['fg'], 'fg')

            if 'fm' in e:
                fm = self.get_format(e['fm'])

        return '%s%s%s%s' % (bg, fg, fm, text)

    def get_color(self, name, bgfg):
        if SHELL == 'zsh':
            ret = self._get_color_zsh(name, bgfg)
        else:
            ret = self._get_color_bash(name, bgfg)

        return ret

    def _get_color_zsh(self, name, bgfg):
        if bgfg == 'fg':
            kind = 'F'
        else:
            kind = 'K'

        if name == 'default':
            # Default
            seq = '%%%s' % kind.lower()
        else:
            if name in self.colors:
                # Named color
                seq = '%%%s{%s}' % (kind, self.colors[name])
            elif rematch(r'^\d{1,3}$', name):
                # Color number
                seq = '%%%s{%s}' % (kind, name)
            else:
                # If anything else, use default
                seq = '%%%s' % kind.lower()

        return "%%{%s%%}" % seq

    def _get_color_bash(self, name, bgfg):
        if bgfg == 'fg':
            kind = 3
        else:
            kind = 4

        if name == 'default':
            # Default
            seq = '\x1b[%s9m' % kind
        else:
            if name in self.colors:
                # Named color
                seq = '\x1b[%s8;5;%sm' % (kind, self.colors[name])
            elif rematch(r'^\d{1,3}$', name):
                # Color number
                seq = '\x1b[%s8;5;%sm' % (kind, name)
            elif (
                    rematch(r'^\d{1,3};\d{1,3};\d{1,3}$', name) and
                    SHELL != 'zsh'):
                # RGB color
                seq = '\x1b[%s8;2;%sm' % (kind, name)
            else:
                # If anything else, use default
                seq = '\x1b[%s9m' % kind

        return "\001%s\002" % seq

    def get_format(self, name):
        if SHELL == 'zsh':
            ret = self._get_format_zsh(name)
        else:
            ret = self._get_format_bash(name)

        return ret

    def _get_format_zsh(self, name):
        ret = ''

        if 'bold' in name:
            ret += "%{%B%}"
        if 'underlined' in name:
            ret += "%{%U%}"
        if ret == '':
            ret = "%{%b%}%{%u%}"

        return ret

    def _get_format_bash(self, name):
        ret = ''

        if 'bold' in name:
            ret += "\001\x1b[1m\002"
        if 'underlined' in name:
            ret += "\001\x1b[21m\002"
        if ret == '':
            ret = "\001\x1b[21m\002\001\x1b[24m\002"

        return ret
