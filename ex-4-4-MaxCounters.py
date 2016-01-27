"""
MaxCounters

Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all
counters to current maximum

You are given N counters, initially set to 0, and you have two possible operations on them:

    * increase(X) - counter X is increased by 1
    * max counter - all counters are set to the maximum value of any counter

A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:
    * if A[K] = X, such that 1 <= X <=  N, then operation K is increase(X)
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

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of
integers representing the values of the counters.

The sequence should be returned as:

        a structure Results (in C), or
        a vector of integers (in C++), or
        a record Results (in Pascal), or
        an array of integers (in any other programming language).

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for
        input arguments).

Elements of input arrays can be modified.


---

This one was tricksy.  The straight-forward solution, even though quite fast and elegant, involves updating all the
counters every time you get an update-all instruction.  This is the difference between a 60% score and a 100% score.

To avoid this hit you have to track the low and high water marks and refer to them as you update individual counters.
Then, before sending back the results, add a pass over the counters to ensure they are all up to the low-water mark.
"""

import unittest
import random

MAX_INT = 100000
INT_RANGE = (1, MAX_INT)


def solution(N, A):
    """
    :param N: integer - the number of counters
    :param A: a sequence of integers specifying which counter to increase
    :return: the list of counters' values
    """
    counters = [0] * (N + 1)   # make it one longer so the counter number works as an index without being off by one
    maximum = 0
    minimum = 0

    # step through the array of instructions
    for key in A:
        if key <= N:
            # align with the minimum
            if counters[key] < minimum:
                counters[key] = minimum
            # now increment it
            counters[key] += 1
            # update the maximum
            if counters[key] > maximum:
                maximum = counters[key]
        else:
            # an update-all instruction resets the minimum
            minimum = maximum

    # set any counters below the minimum to the minimum
    for key, value in enumerate(counters):
        if value < minimum:
            counters[key] = minimum

    return counters[1:]  # trim the zero array position off


class TestExercise(unittest.TestCase):

    def test_example(self):
        self.assertEqual(solution(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])

    def test_singles(self):
        self.assertEqual(solution(1, [1]), [1])
        self.assertEqual(solution(1, [1, 2]), [1])
        self.assertNotEqual(solution(1, [1,2,2]), [2])
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
        # ten thousand counters, 90 thousand operations
        arr = [random.randint(1, 9999) for _ in xrange(90000)]
        print solution(9999, arr)

"""
example
extreme_small: all max_counter operations
single: only one counter
small_random1: small random test 6 max_counter operations
small_random2: small random test, 10 max_counter operations
medium_random1: medium random test, 50 max_counter operations
medium_random2: medium random test, 500 max_counter operations
large_random1: large random test, 2120 max_counter operations
large_random2: large random test, 10000 max_counter operations
extreme_large: all max_counter operations
"""

if __name__ == '__main__':
    unittest.main()
