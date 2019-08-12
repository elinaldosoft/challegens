from main import solution_01, solution_02, solution_03


class TestMain:
    def setup(self):
        self.fixtures = [
            [1],
            [1, 3, 6, 4, 1, 2],
            [1, 2, 3],
            [-1, -3],
            [9, 7, 6, 1, 4],
            [9, 7, 6, 1, 4, 12, 34, 10, 11, 11, 10, 5, 21, 32, 32],
        ]

    def test_01(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[0]) == 2

    def test_02(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[1]) == 5

    def test_03(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[2]) == 4

    def test_04(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[3]) == 1

    def test_05(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[4]) == 2

    def test_06(self):
        for func in [solution_01, solution_02, solution_03]:
            assert func(self.fixtures[5]) == 2
