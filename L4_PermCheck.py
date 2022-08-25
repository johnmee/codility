"""
# PermCheck
Check whether array A is a permutation.

A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random


def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)

    One-by-one, add each value to a set.
        Abort if the value is not valid for the permutation
        Abort if the value is a duplicate
    It is a permutation.
    """
    if not len(A):
        return 0  # An empty list is not a permutation.

    collection = set()
    length = 0
    for item in A:
        if item > len(A):
            return 0  # Item is too big for the permutation.
        collection.add(item)
        length += 1
        if len(collection) != length:
            return 0  # Length of set did not increase, so item is a duplicate.
    return 1


class TestExercise(unittest.TestCase):
    """
    example1
    example2
    single element
    double = two elements
    antiSum1 = total sum is correct but it is not a permutation, N <= 10
    small_permutation = permutation + one element occurs twice, N = ~100
    medium_permutation = permutation + few elements occur twice, N = ~10000
    antisum2 = total sum is correct but it is not a permutation, N = ~100000
    large_permutation: permutation + one element occurs twice, N = ~100000
    large_range: sequence 1,2,...,N  N=~100000
    extreme_min_max = single element with min/max value
    extreme_values: all the same values, N=~100000
    """
    def test_example1(self):
        self.assertEqual(solution([4, 1, 3, 2]), 1)
        self.assertEqual(solution([4, 1, 3]), 0)

    def test_bottom_edge(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([2]), 0)
        self.assertEqual(solution([1, 2]), 1)
        self.assertEqual(solution([2, 1]), 1)
        self.assertEqual(solution([2, 2]), 0)
        self.assertEqual(solution([1, 1]), 0)
        self.assertEqual(solution([1, 2, 3]), 1)
        self.assertEqual(solution([3, 2, 1]), 1)
        self.assertEqual(solution([5, 2, 1]), 0)
        self.assertEqual(solution([3, 1]), 0)

    def test_duplicates(self):
        self.assertEqual(solution([3, 3, 3, 3, 2, 1]), 0)

    def test_extreme(self):
        arr_range = (1, 100000)

        # full complement of numbers
        arr = list(range(*arr_range))
        random.shuffle(arr)
        self.assertEqual(solution(arr), 1)

        # full complement with one missing
        arr.remove(random.randint(1, len(arr)))
        self.assertEqual(solution(arr), 0)


if __name__ == '__main__':
    unittest.main()
