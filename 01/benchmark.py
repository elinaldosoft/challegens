import cProfile, pstats, io
import copy
from main import (
    count_apples_and_oranges_01,
    count_apples_and_oranges_02,
    count_apples_and_oranges_03,
    count_apples_and_oranges_04,
)

values = {
    "s": 7,
    "t": 10,
    "a": 4,
    "b": 12,
    "apples": [2, 3, -4],
    "oranges": [3, -2, -4],
}

# cProfile.run("[count_apples_and_oranges_01(**values) for _ in range(10000)]")
# cProfile.run("[count_apples_and_oranges_02(**values) for _ in range(10000)]")
# cProfile.run("[count_apples_and_oranges_03(**values) for _ in range(10000)]")
# cProfile.run("[count_apples_and_oranges_04(**values) for _ in range(10000)]")
