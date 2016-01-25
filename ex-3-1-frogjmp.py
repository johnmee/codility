import unittest
import random

INT_RANGE = (1, 1000000000)


def solution(X, Y, D):
    """
    Calculate the miminum number of jumps from X to Y
    :param X: start integer
    :param Y: minimum end integer
    :param D: size of the jump
    :return: minium number of jumps in O(1) time and space complexity
    """
    # assume X is less than Y
    assert X <= Y

    quot, rem = divmod(Y-X, D)
    return quot if rem == 0 else quot + 1


class TestFrogJump(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution(10, 85, 30), 3)

    def test_one(self):
        self.assertEqual(solution(0, 10, 1), 10)

    def test_big_steps(self):
        self.assertEqual(solution(0, 10, 20), 1)

    def test_even_steps(self):
        self.assertEqual(solution(10, 100, 10), 9)

    def test_equal_steps(self):
        self.assertEqual(solution(10, 10, 10), 0)

    def test_odd_steps(self):
        self.assertEqual(solution(9, 29, 10), 2)

if __name__ == '__main__':
    unittest.main()
