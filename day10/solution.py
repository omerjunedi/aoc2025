import itertools
import math
import sys
import numpy as np
from numpy import typing as npt
D = sys.stdin.readlines()


def parse_light(light: str) -> list[int]:
    return [1 if x == '#' else 0 for x in light[1:-1]]


def parse_buttons(buttons: str) -> list[list[int]]:
    return [[int(y) for y in x[1:-1].split(',')] for x in buttons]


def parse_joltages(joltages: str) -> list[int]:
    return [int(x) for x in joltages[1:-1].split(',')]


def parse(machine: str) -> tuple[list[int], list[list[int]], list[int]]:
    things = machine.split()
    light, buttons, joltages = parse_light(things[0]), parse_buttons(things[1:-1]), parse_joltages(things[-1])
    return light, buttons, joltages

def push_buttons(buttons: list[list[int]], target: list[int]) -> int:

    L = len(target)
    boolean_array = [[0] * L for _ in range(len(buttons))]

    for k in range(len(buttons)):
        for b in buttons[k]:
            boolean_array[k][b] = 1


    res = boolean_array[0]
    for button in boolean_array[1:]:
        res = [x ^ y for x, y in zip(button, res)]


    return len(buttons) if res == target else 0


def part1():
    ans = 0
    for machine in D:
        res = math.inf
        target, buttons, _ = parse(machine)
        for k in range(1, len(buttons)):
            for combo in itertools.combinations(buttons, k):
                if (a := push_buttons(combo, target)):
                    res = min(res, a)

        ans += res

    print(ans)


def part2():

    # represent this as a system of equations
    # the solution is a linear combination of the buttons
    # rows of the matrix are the buttons
    # Ax = b
    # x is column vector of number of times each button is pressed
    # b is column vector of the wanted joltages

    ans = 0


    for machine in D:
        _, buttons, joltages = parse(machine)

        L = len(joltages)
        boolean_array = [[0] * L for _ in range(len(buttons))]

        for k in range(len(buttons)):
            for b in buttons[k]:
                boolean_array[k][b] = 1

        A: npt.NDArray[np.int_] = np.array(boolean_array)
        b: npt.NDArray[np.int_] = np.array(joltages)

        # TODO: solve the system of equations, if possible



    print(ans)

part1()
