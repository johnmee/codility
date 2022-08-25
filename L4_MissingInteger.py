"""
# Missing Integer
Find the smallest positive integer that does not occur in a given sequence.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random


def solution(A):
    """
    :param A: list[int] A non-empty list of integers.
    :return: [int] The smallest positive integer that is missing.

    Sort the array and walk through it until we find the missing item.
    I wonder if this is a mistake: allowing us to sort the array first?
    """
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing


N_RANGE = (1, 100000)
ELEMENT_RANGE = (-2147483648, 2147483647)


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_extreme_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([-1]), 1)

    def test_simple(self):
        self.assertEqual(solution([2, 3, 4, 6, 10, 1000]), 1)
        self.assertEqual(solution([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000]), 7)
        self.assertEqual(solution([1000, -1, 10, 3, -5, 2, 11, 59, 1]), 4)

    def test_extreme_min_max_int(self):
        self.assertEqual(1, solution([ELEMENT_RANGE[0], ELEMENT_RANGE[1], -10]))

    def test_positive_only(self):
        arr = list(range(1, 101)) + list(range(102, 201))
        random.shuffle(arr)
        self.assertEqual(solution(arr), 101)

    def test_negative_only(self):
        arr = list(range(-100, 0))
        random.shuffle(arr)
        self.assertEqual(solution(arr), 1)

    def test_no_gaps(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), 6)

    def test_duplicates(self):
        self.assertEqual(solution([1, 1, 1, 3, 3, 3]), 2)

    def test_large_2(self):
        # create big array of ints
        arr = list(range(1, 100000))
        random.shuffle(arr)
        # remove one
        missing_idx = random.randint(1, len(arr))
        missing_int = arr[missing_idx]
        del arr[missing_idx]
        # run it
        self.assertEqual(solution(arr), missing_int)

    def test_monster_positive(self):
        arr = [random.randint(*ELEMENT_RANGE) for _ in range(1, N_RANGE[1])]
        random.shuffle(arr)
        print(solution(arr), arr)


if __name__ == "__main__":
    unittest.main()
