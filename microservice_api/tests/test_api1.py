

def square(num):
    return num * num


def cube(num):
    return num * num * num


class TestExample:
    num = 5
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2


    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3