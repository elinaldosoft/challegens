def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: list, oranges: list):
    """
        s: integer, starting point of Sam's house location.
        t: integer, ending location of Sam's house location.
        a: integer, location of the Apple tree.
        b: integer, location of the Orange tree.
        apples: integer array, distances at which each apple falls from the tree.
        oranges: integer array, distances at which each orange falls from the tree.
    """
    interval = list(range(s, t + 1))
    apples = list(map(lambda x: x + a, apples))
    oranges = list(map(lambda y: y + b, oranges))
    qty_apples = 0
    qty_oranges = 0

    for apple in apples:
        if apple in interval:
            qty_apples += 1

    for orange in oranges:
        if orange in interval:
            qty_oranges += 1

    return qty_apples, qty_oranges
