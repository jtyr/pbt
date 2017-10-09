#!/usr/bin/python3

from importlib import import_module
from os import getenv
from os.path import basename
from re import split as resplit
from sys import stdout

from pbt.core import SHELL


def printTrain(cars):
    separator = getenv('PBT_SEPARATOR', '')
    prev_bg = None
    prev_display = True

    if SHELL == 'zsh':
        stdout.write("%{%f%k%b%}")

    for car in cars:
        if car.display:
            if prev_bg is not None and prev_display:
                stdout.write(
                    "%s%s" % (
                        car._color_start(
                            fg=car._get_color(prev_bg, True),
                            bg=car._get_color(car.model['root']['bg'], False),
                            text=separator),
                        car._color_end()
                    )
                )

            prev_bg = car.model['root']['bg']
            prev_display = car.display

            stdout.write(car.format())


def main():
    cars_str = getenv('PBT_CARS', "Status, Os, Hostname, Time, Dir, Git, Sign")
    cars_names = resplit('\s*,\s*', cars_str)
    cars = []

    for car in cars_names:
        try:
            cars.append(
                getattr(
                    import_module(
                        'pbt.cars.%s' % car),
                    '%sCar' % car)())
        except Exception as e:
            print("Cannot import module %sCar: %s" % (car, e))

    printTrain(cars)


if __name__ == '__main__':
    main()
