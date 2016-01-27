"""
Frog River One

Find the earliest time when a frog can jump to the other side of a river.

A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get
to position X. Leaves fall from a tree onto the surface of the river.

You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves. A[K]
represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only
when leaves appear at every position across the river from 1 to X. You may assume that the speed of the current in
the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the
river.

Write a function:

    def solution(X, A)

that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the
frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return -1.

For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Assume that:

        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).


Elements of input arrays can be modified.
"""
import unittest
import random

N_RANGE = (1, 100000)


def solution(X, A):
    """
    :param X: an integer. the frogs destination
    :param A: non-empty list of integers
    :return: an integer - the earliest time, or -1
    """
    # count unique leaf positions and stop when there are enough
    leaves = {}
    for second in range(0, len(A)):
        leaves[A[second]] = True
        if len(leaves) == X:
            return second
    return -1


class TestExercise(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)

    def test_extreme_single(self):
        self.assertEqual(solution(1, [1]), 0)
        self.assertEqual(solution(0, [2]), -1)
        self.assertEqual(solution(2, [2]), -1)
        self.assertEqual(solution(2, [2,1]), 1)
        self.assertEqual(solution(2, [1, 2]), 1)
        self.assertEqual(solution(2, [1, 1]), -1)
        self.assertEqual(solution(2, [2, 2]), -1)
        self.assertEqual(solution(3, [1, 2]), -1)

    def test_simple(self):
        self.assertEqual(solution(3, [1, 2, 3]), 2)
        self.assertEqual(solution(3, [2, 3, 1]), 2)
        self.assertEqual(solution(3, [3, 2, 1]), 2)
        self.assertEqual(solution(4, [3, 2, 1]), -1)
        self.assertEqual(solution(3, [3, 2, 2]), -1)
        self.assertEqual(solution(3, [3, 3, 3, 1, 1, 2]), 5)

    def test_extreme_max(self):
        X = 100000
        A = range(1, X)
        random.shuffle(A)
        A.append(X)
        self.assertEqual(solution(X, A), X-1)


# extreme_frog - frog never crosses
# small_random1 - 3 random permutation X=50
# small_random2 - 5 random permutation X=60
# extreme_leaves = all leaves in the same place
# medium_random = 6 and 2 random permutations, X = ~5000
# medium_range = arithmetic sequences X = 5000
# large_random = 10 and 100 random permutation, X = ~10000
# large_permutation = permutation tests (2)
# large_range = arithmetic sequences X=30000


if __name__ == '__main__':
    unittest.main()
