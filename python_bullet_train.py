#!/usr/bin/python3

import sys
from importlib import import_module
from re import split as resplit
from os import getenv


def printTrain(cars):
    separator = getenv('PBT_SEPARATOR', '\ue0b0')
    prev_bg = None
    prev_display = True

    for car in cars:
        if prev_bg is not None and prev_display:
            sys.stdout.write(
                "%s%s" % (
                    car._color_start(
                        bg=car.model['root']['bg'],
                        fg=prev_bg,
                        text=separator),
                    car._color_end()
                )
            )

        sys.stdout.write(car.format())

        prev_bg = car.model['root']['bg']
        prev_display = car.display

    print()


def main():
    cars_str = getenv('PBT_CARS', "Status, Hostname, Time, Dir, Sign")
    cars_names = resplit('\s*,\s*', cars_str)
    cars = []

    for car in cars_names:
        try:
            cars.append(
                getattr(
                    import_module(
                        'pbt.cars.%s' % car),
                    '%sCar' % car)())
        except:
            pass

    printTrain(cars)


if __name__ == '__main__':
    main()
