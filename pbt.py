#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib import import_module
from os import getenv
from re import split as resplit
from sys import stderr, stdout, version_info
from traceback import print_exc

from pbt.core import BOOL_TRUE, SHELL


def print_train(cars):
    separator = getenv('PBT_SEPARATOR', '')
    prev_bg = None
    prev_display = True

    for car in cars:
        if car.display:
            if prev_bg is not None and prev_display:
                stdout.write(
                    car.elem_color(
                        fg=car.get_color(prev_bg, True),
                        bg=car.get_color(car.model['root']['bg']),
                        text=separator)
                )

            prev_bg = car.model['root']['bg']
            prev_display = car.display

            stdout.write(car.format())

    if SHELL == 'zsh':
        stdout.write("%{\x1b[0m%}")
    else:
        stdout.write("\001\x1b[0m\002")


def main():
    if version_info < (3, 0):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

    cars_str = getenv('PBT_CARS', "Status, Os, Hostname, Dir, Git, Sign")
    cars_names = resplit(r'\s*,\s*', cars_str)
    cars = []

    for car in cars_names:
        try:
            cars.append(
                getattr(
                    import_module(
                        'pbt.cars.%s' % car),
                    '%sCar' % car)())
        except Exception:
            stderr.write("ERROR: Cannot import module %sCar.\n" % car)

            if getenv('PBT_DEBUG', False) in BOOL_TRUE:
                print_exc(file=stderr)

    print_train(cars)


if __name__ == '__main__':
    main()
