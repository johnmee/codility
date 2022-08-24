import unittest
import random

N_RANGE = (2, 100000)
ELEMENT_RANGE = (-1000, 1000)


def solution(A):
    """
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
    :param A: non-empty list of integers
    :return: an integer - the index value where the smallest difference occurs
    """
    # array must be more than 2 elements
    assert len(A) > 1

    # establish the tallys
    best = None
    before = 0
    after = sum(A)

    # adjust and test at every split
    for P in xrange(0, len(A) - 1):
        before += A[P]
        after -= A[P]
        difference = abs(before - after)
        if best is None or difference < best:
            best = difference

    return best


class TestExercise(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_simple(self):
        self.assertEqual(solution([1,2]), 1)

    def test_double(self):
        self.assertEqual(solution([-1000, 1000]), 2000)

    def test_random(self):
        N = random.randint(*N_RANGE)
        arr = [random.randint(*ELEMENT_RANGE) for _ in xrange(N)]
        print N, solution(arr), arr

    def test_maximum(self):
        arr = [random.randint(*ELEMENT_RANGE) for _ in range(100000)]
        print 100000, solution(arr), arr


if __name__ == '__main__':
    unittest.main()
