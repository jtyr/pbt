#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from importlib import import_module
from os import getenv
from re import split as resplit
from sys import exit, stderr, stdout, version_info
from traceback import print_exc

from pbt import VERSION
from pbt.core import BOOL_TRUE, Car, SHELL


def print_train(cars, right):
    if right:
        separator = getenv('PBT_RSEPARATOR', '')
    else:
        separator = getenv('PBT_SEPARATOR', '')

    prev_bg = None
    prev_display = True

    if not right and getenv('PBT_BEGINNING_TEXT', ''):
        fake_car = Car()

        stdout.write(
            fake_car.elem_color(
                bg=fake_car.get_color(getenv('PBT_BEGINNING_BG', 'default')),
                fg=fake_car.get_color(getenv('PBT_BEGINNING_FG', 'default')),
                fm=fake_car.get_color(getenv('PBT_BEGINNING_FM', 'none')),
                text=getenv('PBT_BEGINNING_TEXT')))

    for car in cars:
        if car.display:
            if prev_bg is not None and prev_display:
                if car.wrap:
                    bg = car.get_color('default')
                    fg = car.get_color('default', True)
                else:
                    bg = car.get_color(car.model['root']['bg'])
                    fg = car.get_color(car.model['root']['bg'], True)

                if right:
                    stdout.write(
                        car.elem_color(
                            bg=car.get_color(prev_bg),
                            fg=fg,
                            text=separator if car.sep is None else car.sep))
                else:
                    stdout.write(
                        car.elem_color(
                            bg=bg,
                            fg=car.get_color(prev_bg, True),
                            text=separator if car.sep is None else car.sep))

                if car.wrap:
                    stdout.write("\n")

            prev_bg = car.model['root']['bg']
            prev_display = car.display

            stdout.write(car.format())

    if SHELL == 'zsh':
        stdout.write("%{\x1b[0m%}")
    else:
        stdout.write("\001\x1b[0m\002")


def main():
    # Read the command line options
    parser = ArgumentParser(
        description='Highly configurable prompt decoration for ZSH and Bash.')
    parser.add_argument(
        '-v', '--version',
        help='show version and exit',
        action='store_true')
    parser.add_argument(
        '-r', '--right',
        help='build right hand side prompt',
        action='store_true')
    parser.add_argument(
        'RC',
        nargs='?',
        help='return code of the executed command')
    args = parser.parse_args()

    if args.version:
        print("PBT v%s" % VERSION)
        exit(0)

    if version_info < (3, 0):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

    if args.right:
        cars_str = getenv('PBT_RCARS', "Time")
    else:
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

    print_train(cars, args.right)


if __name__ == '__main__':
    main()
