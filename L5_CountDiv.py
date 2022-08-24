"""
CountDiv

Compute number of integers divisible by k in range [a..b].

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A <= i <= B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A <= B.

Complexity:

        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).
"""
import unittest
import random


MAX_INT = int(2e9)
INT_RANGE = (1, MAX_INT)


def solution(A, B, K):
    """
    :param A: start integer
    :param B: end integer
    :param K: divisor integer
    :return: count of integers A..B divisible by K
    """
    # just depends whether A is part of the count itself, or not
    if A % K == 0:
        return B//K - A//K + 1
    else:
        return B//K - A//K


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution(6, 11, 2), 3)

    def test_small(self):
        self.assertEqual(solution(5, 11, 2), 3)
        self.assertEqual(solution(6, 12, 2), 4)
        self.assertEqual(solution(5, 12, 2), 4)
        self.assertEqual(solution(5, 13, 2), 4)

    def test_edges(self):
        self.assertEqual(solution(0, 0, 1), 1)
        self.assertEqual(solution(0, 1, 1), 2)
        self.assertEqual(solution(1, 1, 2), 0)
        self.assertEqual(solution(10, 20, 10), 2)
        self.assertEqual(solution(9, 21, 10), 2)

    def test_max_min(self):
        self.assertEqual(solution(0, MAX_INT, 1), MAX_INT + 1)


"""
example
simple (11, 345, 17)
minimal: A = B in {0,1}, K=11
extreme_ifempty: A=10, B=10, K in {5,7,20}
extreme_endpoints: verify handling of range endpoints, multiple runs

big_values: (100, 123e6, K=10e3)
big_values2: (101, 123M+, 10K)
big_values3: (0, maxint, k in {1, maxint}
big_values4: A, B, K in {1,maxint}
"""

if __name__ == '__main__':
    unittest.main()
