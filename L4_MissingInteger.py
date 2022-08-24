"""
# Missing Integer
Find the minimal positive integer not occurring in the given sequence.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0)
that does not occur in A.

For example, given:
  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2

the function should return 5.

Assume that:
    * N is an integer within the range [1..100,000]
    * each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].

Complexity:
    * expected worst-case time complexity is O(N)
    * expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
        arguments).

Elements of input arrays can be modified.
"""

import unittest
import random

N_RANGE = (1, 100000)
ELEMENT_RANGE = (-2147483648, 2147483647)


def solution(A):
    """
    :param A: non-empty list of integers
    :return: an integer - the smallest positive integer that is missing
    """
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing


def alternate_solution(A):
    """
    A 'Pidgeon Hole' solution:

    :param A: non-empty list of integers
    :return: an integer - the smallest positive integer that is missing
    """
    # dictionary of booleans indicating which ints we've seen
    roll = {}
    largest = 0

    # mark the roll
    for element in A:
        if element > 0:
            roll[element] = True
            # track the largest int
            if element > largest:
                largest = element

    # find the first missing element
    # NB: using `not in roll.keys()` contributes an O(N) loop which ruins time complexity on the codility platform
    counter = 1
    while counter <= largest:
        if counter in roll:
            counter += 1
        else:
            break

    return counter



class TestExercise(unittest.TestCase):

    def test_example(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_extreme_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([-1]), 1)

    def test_simple(self):
        self.assertEqual(solution([2,3,4,6,10,1000]), 1)
        self.assertEqual(solution([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000]), 7)
        self.assertEqual(solution([1000, -1, 10, 3, -5, 2, 11, 59, 1]), 4)

    def test_extreme_min_max_int(self):
        self.assertEqual(1, solution([ELEMENT_RANGE[0], ELEMENT_RANGE[1], -10]))

    def test_positive_only(self):
        arr = range(1, 101) + range(102, 201)
        random.shuffle(arr)
        self.assertEqual(solution(arr), 101)

    def test_negative_only(self):
        arr = range(-100, 0)
        random.shuffle(arr)
        self.assertEqual(solution(arr), 1)

    def test_no_gaps(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), 6)

    def test_duplicates(self):
        self.assertEqual(solution([1, 1, 1, 3, 3, 3]), 2)

    def test_large_2(self):
        # create big array of ints
        arr = range(1,100000)
        random.shuffle(arr)
        # remove one
        missing_idx = random.randint(1, len(arr))
        missing_int = arr[missing_idx]
        del arr[missing_idx]
        # run it
        self.assertEqual(solution(arr), missing_int)

    def test_monster_positive(self):
        arr = [random.randint(*ELEMENT_RANGE) for _ in xrange(1, N_RANGE[1])]
        random.shuffle(arr)
        print solution(arr), arr


if __name__ == '__main__':
    unittest.main()
