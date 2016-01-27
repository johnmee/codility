"""
PermCheck

Check whether array A is a permutation.

A non-empty zero-indexed array A consisting of N integers is given.

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

    int solution(int A[], int N);

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

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

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""
import unittest
import random

ARR_RANGE = (1, 100000)
INT_RANGE = (1, 1000000000)


def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # an empty list is not a permutation
    if not len(A):
        return 0

    # track the hits with a dictionary
    hits = {}
    for item in A:
        # (quick exit) each element once and only once thanks
        if item in hits:
            return 0
        hits[item] = True

    # (quick exit again) each element once and only once
    if len(hits) != len(A):
        return 0

    # ok, see if they're all there
    for num in range(1, len(A) + 1):
        if num not in hits:
            return 0

    return 1


class TestExercise(unittest.TestCase):

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
        # full complement of numbers
        arr = range(*ARR_RANGE)
        random.shuffle(arr)
        self.assertEqual(solution(arr), 1)

        # full complement with one missing
        arr.remove(random.randint(1,len(arr)))
        self.assertEqual(solution(arr), 0)


# example1
# example2
# extreme_min_max = single element with min/max value
# single element
# double = two elements
# antiSum1 = total sum is correct but it is not a permutation, N <= 10
# small_permutation = permutation + one element occurs twice, N = ~100
# medium_permutation = permutation + few elements occur twice, N = ~10000
# antisum2 = total sum is correct but it is not a permutation, N = ~100000
# large_permutation: permutation + one element occurs twice, N = ~100000
# large_range: sequence 1,2,...,N  N=~100000
# extreme_values: all the same values, N=~100000


if __name__ == '__main__':
    unittest.main()
