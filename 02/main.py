def solution_01(lst: list):
    lst.sort()
    smallest = 1
    for i in lst:
        if i == smallest:
            smallest += 1
    return smallest