"""
# MaxCounters

Calculate the values of counters after applying all alternating operations:
increase counter by 1; set value of all counters to current maximum.

You are given N counters, initially set to 0, and you have two possible
operations on them:

    * increase(X) - counter X is increased by 1,
    * max counter - all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given.
This array represents consecutive operations:

    * if A[K] = X, such that 1 <= X <=  N, then operation K is increase(X),
    * if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

    def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
---

# My Notes

The straight-forward solution, of updating all the counters every time
there is a 'max counter' instruction, only gets you a 60% score. If every
instruction is a max-counter it will pass over the whole counter array M
times! O(n*m)

For 100%, optimize the max-counter operation by, to use a tidal analogy,
tracking the "low" and "high" "water" marks across all the counters.

With each counter update, check the low-water mark and, if necessary,
raise this counter to it. Now increment. And, before you leave, if necessary,
reset the high water mark.  This way, you maintain context of what is happening
in all the counters, without needing to visit them repeatedly.

Before sending back the results, a final pass over the counters is necessary to
ensure the low-water mark applies to any counters which have not been in focus
since it last changed.

Thus the solution requires just two passes over the whole array of counters. O(n+m)
"""
import unittest
import random


def solution(N, A):
    """
    :param N: [int] The number of counters.
    :param A: list[int] A sequence of instructions.
    :return: list[int] The list of final counter values.

    Create the list of counters and two marker values for max high and min low.
    For every operation
      if a "raise counter" operation, then
          first, raise that counter to the "low water" mark
          next, increment the counter
          finally, update the "high water", if necessary
      if a "max counter" operation then
          raise the "low water" mark to the "high water" mark
    For every counter
      raise any counter below the "low water" mark to the "low water" mark.
    """

    counters = [0] * (N + 1)
    high_water = low_water = 0

    for index in A:
        if index > N:   # 'Max-Counter' operation
            low_water = high_water
        else:          # 'Increase-Counter' operation
            counters[index] = max(counters[index], low_water)
            counters[index] += 1
            high_water = max(counters[index], high_water)

    for index, value in enumerate(counters):
        counters[index] = max(low_water, value)

    return counters[1:]  # Trim away the extraneous counter for zero values.


class TestExercise(unittest.TestCase):
    """
    example: given
    single: only one counter
    small_random1: small random test 6 max_counter operations
    small_random2: small random test, 10 max_counter operations
    medium_random1: medium random test, 50 max_counter operations
    medium_random2: medium random test, 500 max_counter operations
    large_random1: large random test, 2120 max_counter operations
    large_random2: large random test, 10000 max_counter operations
    extreme_small: all max_counter operations
    extreme_large: all max_counter operations
    """

    def test_example(self):
        self.assertEqual(solution(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])

    def test_singles(self):
        self.assertEqual(solution(1, [1]), [1])
        self.assertEqual(solution(1, [1, 2]), [1])
        self.assertNotEqual(solution(1, [1, 2, 2]), [2])
        self.assertEqual(solution(1, [1, 1, 2, 1, 1]), [4])

    def test_doubles(self):
        self.assertEqual(solution(2, [1, 1, 1, 2]), [3, 1])
        self.assertEqual(solution(2, [1, 1, 1, 3]), [3, 3])
        self.assertEqual(solution(2, [3, 1, 1, 1]), [3, 0])
        self.assertEqual(solution(2, [3, 1, 1, 2]), [2, 1])
        self.assertEqual(solution(2, [1, 2, 3, 1, 2]), [2, 2])
        self.assertEqual(solution(2, [1, 1, 3, 1, 1]), [4, 2])
        self.assertEqual(solution(2, [1, 1, 3, 2, 2]), [2, 4])

    def test_extreme(self):
        # Ten thousand counters, 90 thousand operations.
        arr = [random.randint(1, 9999) for _ in range(90000)]
        print(solution(9999, arr))


if __name__ == "__main__":
    unittest.main()
