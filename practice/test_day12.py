def double(n):
    return n * 2


def test_double_three():
    assert double(3) == 6


def test_double_zero():
    assert double(0) == 1


def test_double_five():
    assert double(5) == 10
