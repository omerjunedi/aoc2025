from enum import Enum
import sys
from math import prod
D = sys.stdin.read().splitlines()


def part1():
    homework: list[list[int] | list[str]] = [[] for _ in range(len(D))]

    for i, row in enumerate(D[:-1]):
        homework[i] = [int(c) for c in row.split()]

    homework[-1] = D[-1].split()

    homework.reverse()
    homework_t = [list(row) for row in zip(*homework)]

    res = 0
    for i in range(len(homework[0])):
        res += sum(homework_t[i][1:]) if homework_t[i][0] == '+' else prod(homework_t[i][1:])

    print(f"Part 1: {res}")


class Operation(Enum):
    ADD = 1
    MULT = 2


def part2():
    # Parse each line, need spaces to determine left and right alignment
    # Cannot use split() because of that

    res = 0
    homework: list[list[str]] = [[] for _ in range(len(D))]

    for i, row in enumerate(D):
        homework[i] = [c for c in row.split()]

    homework_t: list[list[str]] = [list(row) for row in zip(*homework)]
    lengths: dict[int, int] = {}

    for k in range(len(homework[0])):
        max_str = max(homework_t[k][:-1], key=len)
        max_len = len(max_str)
        lengths[k] = max_len

    curr_index = 0
    for j in range(len(homework[0])):
        len_t = lengths[j]
        job: list[str] = []
        for k in range(len(homework)):
            num = D[k][curr_index:curr_index + len_t]
            job.append(num)
        curr_index += (len_t + 1)
        operation = Operation.ADD if job[-1].strip() == '+' else Operation.MULT
        res += process_job(job[:-1], operation)

    print(f"Part 2: {res}")


# part 2 helper function
def process_job(nums: list[str], operation: Operation):
    nums_t = [int("".join(row)) for row in zip(*nums)]
    return sum(nums_t) if operation == Operation.ADD else prod(nums_t)


part1()
part2()
