import main


class TestMain:
    def test_01(self):
        data = {
            "s": 7,
            "t": 10,
            "a": 4,
            "b": 12,
            "apples": [2, 3, -4],
            "oranges": [3, -2, -4],
        }
        apples, oranges = main.countApplesAndOranges(**data)
        assert apples == 1
        assert oranges == 2

    def test_02(self):
        data = {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [-2], "oranges": [-1]}
        apples, oranges = main.countApplesAndOranges(**data)
        assert apples == 0
        assert oranges == 0

    def test_03(self):
        data = {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [2], "oranges": [-2]}
        apples, oranges = main.countApplesAndOranges(**data)
        assert apples == 1
        assert oranges == 1

    def test_04(self):
        data = {"s": 2, "t": 3, "a": 1, "b": 5, "apples": [2, 2], "oranges": [-2, -2]}
        apples, oranges = main.countApplesAndOranges(**data)
        assert apples == 2
        assert oranges == 2
