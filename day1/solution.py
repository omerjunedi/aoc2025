
class ThreadSafeDictionary:

    def __init__(self) -> None:
        pass

    def __hash__(self) -> int:
        return 0

    def __repr__(self) -> str:
        return ""



def part1():
    res = 0
    lock = 50
    with open("example", "r") as file:
        lines = file.readlines()
        for line in lines:
            left = line[0] == 'L'
            steps = int(line[1:])
            lock += (-steps) if left else steps
            lock %= 100
            if lock == 0:
                res += 1

        print(res)

def part2():
    res = 0
    lock = 50
    with open("input", "r") as file:
        lines = file.readlines()
        for line in lines:
            left = line[0] == 'L'
            steps = int(line[1:])
            for _ in range(steps):
                if left:
                    lock = (lock - 1 + 100) % 100
                else:
                    lock = (lock + 1) % 100
                if lock == 0:
                    res += 1

    print(res)

part1()
part2()
