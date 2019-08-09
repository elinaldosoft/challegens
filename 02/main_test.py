from main import solution_01


class TestMain:
    def setup(self):
        self.fixtures = [[1, 3, 6, 4, 1, 2], [1, 2, 3], [-1, -3], [9, 7, 6, 1,4]]

    def test_01(self):
        assert solution_01(self.fixtures[0]) == 5

    def test_02(self):
        assert solution_01(self.fixtures[1]) == 4

    def test_03(self):
        assert solution_01(self.fixtures[2]) == 1

    def test_04(self):
        assert solution_01(self.fixtures[2]) == 1

    def test_05(self):
        assert solution_01(self.fixtures[3]) == 2
