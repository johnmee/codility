"""
Distinct

Compute number of distinct values in an array.

https://codility.com/programmers/task/distinct/

----------------
# My Analysis

Bit easy in Python.  Just add each value as the key to a dictionary and return a count of the keys.

-------------------
# Problem Description

Write a function

    def solution(A)

that, given a zero-indexed array A consisting of N integers, returns the number of distinct values in array A.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [-1,000,000..1,000,000].

For example, given array A consisting of six elements such that:
A[0] = 2    A[1] = 1    A[2] = 1
A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""

import unittest
import random


RANGE_A = (-1000000, 1000000)
RANGE_N = (0, 100000)


def solution(A):
    """
    :param A: array of integers
    :return: an integer
    """
    # count the number of keys created
    distinct = {}
    # update the dictionary using the value as the key
    for val in A:
        distinct[val] = True
    # return the number of keys
    return len(distinct.keys())


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([2, 1, 1, 2, 3, 1]), 3)

    def test_simple(self):
        self.assertEqual(solution([0, 1, 2, 3, 4]), 5)

    def test_edges(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([0]), 1)
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([0, 1]), 2)
        self.assertEqual(solution([-1, 1]), 2)
        self.assertEqual(solution([RANGE_A[0], RANGE_A[1]]), 2)

    def test_medium(self):
        self.assertEqual(solution([1] * 500), 1)
        self.assertEqual(solution([x for x in xrange(-250, 250)]), 500)
        self.assertEqual(solution([x for x in xrange(-500, 500, 2)]), 500)
        self.assertEqual(solution([x for x in xrange(-500, 500, 2)] * 2), 500)

    def test_random(self):
        A = [random.randint(*RANGE_A) for _ in xrange(*RANGE_N)]
        print solution(A), A

    def test_extreme(self):
        A = [x for x in xrange(*RANGE_N)]
        self.assertEqual(solution(A), RANGE_N[1])


if __name__ == '__main__':
    unittest.main()
