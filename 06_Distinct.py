"""
Distinct

Compute number of distinct values in an array.

https://codility.com/programmers/task/distinct/

## Problem Description

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
----------------
## Notes

Too easy in Python...
Add each value to a set and return the length of the set. O(N).
https://app.codility.com/demo/results/trainingJBRJSP-9E7/
"""
import unittest
import random


def solution(A):
    """
    :param A: list[int] A list of integers.
    :return: [int] The number of distinct values in A.
    """
    distinct = set()
    for val in A:
        distinct.add(val)
    return len(distinct)


RANGE_A = (-1000000, 1000000)
RANGE_N = (0, 100000)


class TestExercise(unittest.TestCase):
    """
    example1: example test, positive answer
    extreme_empty: empty sequence
    extreme_single: sequence of one element
    extreme_two_elems: sequence of three distinct elements
    extreme_one_value: sequence of 10 equal elements
    extreme_negative: sequence of negative elements, length=5
    extreme_big_values: sequence with big values, length=5
    medium1: chaotic sequence of value sfrom [0..1K], length=100
    medium2: chaotic sequence of value sfrom [0..1K], length=200
    medium3: chaotic sequence of values from [0..10], length=200
    large1: chaotic sequence of values from [0..100K], length=10K
    large_random1: chaotic sequence of values from [-1M..1M], length=100K
    large_random2: another chaotic sequence of values from [-1M..1M], length=100K
    """

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
        self.assertEqual(solution([x for x in range(-250, 250)]), 500)
        self.assertEqual(solution([x for x in range(-500, 500, 2)]), 500)
        self.assertEqual(solution([x for x in range(-500, 500, 2)] * 2), 500)

    def test_random(self):
        A = [random.randint(*RANGE_A) for _ in range(*RANGE_N)]
        print(solution(A), A)

    def test_extreme(self):
        A = [x for x in range(*RANGE_N)]
        self.assertEqual(solution(A), RANGE_N[1])


if __name__ == "__main__":
    unittest.main()
