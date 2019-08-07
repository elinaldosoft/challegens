import copy
from main import (
    count_apples_and_oranges_01,
    count_apples_and_oranges_02,
    count_apples_and_oranges_03,
    count_apples_and_oranges_04,
)


class TestMain:
    def setup(self):
        self.fixtures = [
            {
                "s": 7,
                "t": 10,
                "a": 4,
                "b": 12,
                "apples": [2, 3, -4],
                "oranges": [3, -2, -4],
            },
            {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [-2], "oranges": [-1]},
            {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [2], "oranges": [-2]},
            {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [2, 2], "oranges": [-2, -2]},
        ]

    def test_01(self):
        for func in [
            count_apples_and_oranges_01,
            count_apples_and_oranges_02,
            count_apples_and_oranges_03,
            count_apples_and_oranges_04,
        ]:
            values = copy.deepcopy(self.fixtures[0])
            apples, oranges = func(**values)
            assert apples == 1
            assert oranges == 2

    def test_02(self):
        for func in [
            count_apples_and_oranges_01,
            count_apples_and_oranges_02,
            count_apples_and_oranges_03,
            count_apples_and_oranges_04,
        ]:
            values = copy.deepcopy(self.fixtures[1])
            apples, oranges = func(**values)
            assert apples == 0
            assert oranges == 0

    def test_03(self):
        for func in [
            count_apples_and_oranges_01,
            count_apples_and_oranges_02,
            count_apples_and_oranges_03,
            count_apples_and_oranges_04,
        ]:
            values = copy.deepcopy(self.fixtures[2])
            apples, oranges = func(**values)
            assert apples == 1
            assert oranges == 1

    def test_04(self):
        for func in [
            count_apples_and_oranges_01,
            count_apples_and_oranges_02,
            count_apples_and_oranges_03,
            count_apples_and_oranges_04,
        ]:
            values = copy.deepcopy(self.fixtures[3])
            apples, oranges = func(**values)
            assert apples == 2
            assert oranges == 2
