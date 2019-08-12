def solution_01(lst: list) -> int:
    lst.sort()
    smallest = 1
    for i in lst:
        if i == smallest:
            smallest += 1
    return smallest


def solution_02(lst: list) -> list:
    lst.sort()
    smallest = 1
    last = 0
    for i in lst:
        diff = i - abs(last)
        if diff > 1:
            diff += last
            while diff > (last + 1):
                diff -= 1
            return diff
        elif i == smallest:
            smallest += 1
        last = i
    return smallest


def solution_03(lst: list) -> list:
    """
    By Anderson
    """
    for i in range(1, len(lst) + 1):
        try:
            lst.index(i)
        except ValueError:
            return i
    return i + 1
