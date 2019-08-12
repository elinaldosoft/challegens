import cProfile, pstats, io
from main import solution_01, solution_02, solution_03

values = [9, 7, 6, 1, 4, 12, 34, 10, 11, 11, 10, 5, 21, 32, 32]

# cProfile.run("[solution_01(values) for _ in range(10000)]")
# cProfile.run("[solution_02(values) for _ in range(10000)]")
# cProfile.run("[solution_03(values) for _ in range(10000)]")