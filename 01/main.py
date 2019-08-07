"""
s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
"""

def count_apples_and_oranges_01(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    interval = list(range(s, t + 1))
    qty_apples = 0
    qty_oranges = 0

    for apple in apples:
        apple += a
        if apple in interval:
            qty_apples += 1

    for orange in oranges:
        orange += b
        if orange in interval:
            qty_oranges += 1
    return qty_apples, qty_oranges

def count_apples_and_oranges_02(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    qty_apples = 0
    qty_oranges = 0
    while apples or oranges:
        if apples:
            apple = apples.pop() + a
            if t >= apple >= s:
                qty_apples += 1
        if oranges:
            orange = oranges.pop() + b
            if t >= orange >= s:
                qty_oranges += 1
    return qty_apples, qty_oranges

def count_apples_and_oranges_03(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    return sum([1 for apple in apples if t >= apple + a >= s]), sum([1 for orange in oranges if t >= orange + b >= s])

def count_apples_and_oranges_04(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    return sum(t >= apple + a >= s for apple in apples), sum(t >= orange + b >= s for orange in oranges)