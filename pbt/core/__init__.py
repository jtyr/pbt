import re


class Car:
    fg = {
        'default': 39,
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'light_gray': 37,
        'dark_gray': 90,
        'light_red': 91,
        'light_green': 92,
        'light_yellow': 93,
        'light_blue': 94,
        'light_magenta': 95,
        'light_cyan': 96,
        'white': 97,
    }
    bg = {
        'default': 49,
        'black': 40,
        'red': 41,
        'green': 42,
        'yellow': 43,
        'blue': 44,
        'magenta': 45,
        'cyan': 46,
        'light_gray': 47,
        'dark_gray': 100,
        'light_red': 101,
        'light_green': 102,
        'light_yellow': 103,
        'light_blue': 104,
        'light_magenta': 105,
        'light_cyan': 106,
        'white': 107,
    }
    display = True

    def format(self):
        if not self.display:
            return ''

        pattern = re.compile('{{\s*(\w+)\s*}}')
        text = ("%s%s%s" % (
            self._color_start('root'),
            self.model['root']['format'],
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
            fg = e['fg']
            bg = e['bg']
            text = e['text'] if 'text' in e else ''

        return ('\x1b[%s;%sm%s' % (
                self._get_fg(fg),
                self._get_bg(bg),
                text))

    def _color_end(self):
        return '\x1b[0m'

    def _get_fg(self, name):
        return self.fg[name] if name in self.fg else name

    def _get_bg(self, name):
        return self.bg[name] if name in self.bg else name
