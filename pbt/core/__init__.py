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
        fm_end = ''

        if element is not None:
            e = self.model[element]

            if 'text' in e and element != 'root':
                text = e['text']
            else:
                text = ''

            bg = self.get_color(e['bg'])
            fg = self.get_color(e['fg'], True)
            fm = self.get_format(e['fm'])

            if fm != self.get_format('empty'):
                fm_end = self.get_format(e['fm'], True)
            else:
                fm = ''

        return '%s%s%s%s%s' % (bg, fg, fm, text, fm_end)

    def get_color(self, name, is_fg=False):
        if is_fg:
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
            elif rematch(r'^\d{1,3};\d{1,3};\d{1,3}$', name):
                # RGB color
                seq = '\x1b[%s8;2;%sm' % (kind, name)
            else:
                # If anything else, use default
                seq = '\x1b[%s9m' % kind

        if SHELL == 'zsh':
            ret = "%%{%s%%}" % seq
        else:
            ret = "\001%s\002" % seq

        return ret

    def get_format(self, name, end=False):
        seq = ''
        c = ''

        if end:
            c = '2'

        if 'bold' in name:
            seq += "\x1b[%s1m" % c

        if 'underline' in name:
            seq += "\x1b[%s4m" % c

        if 'blink' in name:
            seq += "\x1b[%s5m" % c

        if SHELL == 'zsh':
            ret = "%%{%s%%}" % seq
        else:
            ret = "\001%s\002" % seq

        return ret
