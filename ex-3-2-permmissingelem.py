import unittest
import random

INT_RANGE = (0, 100000)


def solution(A):
    """
    Find the missing element in a given permutation
    :param A: list of integers
    :return: the integer that is missing in O(n) time and O(1) space complexity
    """
    # An empty list so the missing element must be "1"
    if len(A) == 0:
        return 1

    return sum(range(1, len(A)+2)) - sum(A)


class TestExercise(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution([2,3,1,5]), 4)

    def test_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)

    def test_random(self):
        arr = [n for n in xrange(1, random.randint(*INT_RANGE))]
        missing =  random.randint(0, len(arr))
        arr.remove(missing)
        self.assertEqual(solution(arr), missing)
        print missing, arr

    def test_maximum(self):
        arr = [n for n in xrange(1, INT_RANGE[1]+1)]
        arr.pop()
        self.assertEqual(solution(arr), INT_RANGE[1])


if __name__ == '__main__':
    unittest.main()
