"""
Triangle

Determine whether a triangle can be built from a given set of edges.

https://codility.com/programmers/task/triangle/

A zero indexed array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given a zero-indexed array A consisting of N integers, returns 1 if there
exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage
        (not counting the storage required for input arguments).

Elements of input arrays can be modified.
----------------

# Solution

The obvious solution is quick to code, but scores only 75% (100, 33).
It has to permutate through all the combinations: O(N**3)
https://app.codility.com/demo/results/training9XK8VG-FDF/

The smart solution, you might say is tricksy, because it leverages a not-so-obvious
observation three numbers that are nearest each other are your best chance of
identifying a 'triangle' early.  So sort the list first, then traverse it.
The sort of O(log(N)) plus a single pass O(N)) => O(N * log(N))
https://app.codility.com/demo/results/trainingNTADKG-3S3/

eg: input: [10, 2, 5, 1, 8, 20]
    sorted = [1, 2, 5, 8, 10, 20]
    [1,2,5] = 3 > 5 = 0
    [2,5,8] = 7 > 8 = 0
    [5,8,10] = 13 > 10 = 1!
Third attempt, versus many tests without the sort.

eg: input: [10, 50, 5, 1]
    sorted = [1, 5, 10, 50]
    [1,5,10] = 6 > 10 = 0
    [5,10,50] = 15 > 50 = 0
Worst case, no triangle, you do visit them all.
"""
import unittest
import itertools


def brute_solution(A):
    """Visit every combination.

    :param A: list[int]
    :return: [int]
    """
    for P, Q, R in itertools.combinations(A, 3):
        if (P + Q > R) and (Q + R > P) and (R + P > Q):
            return 1
    return 0


def better_solution(A):
    """Sort before traverse.

    :param A: list[int]
    :return: [int] 1 if there is a triangle, otherwise 0
    """
    is_triangle = lambda P, Q, R: (P + Q > R) and (Q + R > P) and (R + P > Q)

    A.sort()

    for i in range(len(A) - 2):
        if is_triangle(A[i], A[i+1], A[i+2]):
            return 1
    return 0


solution = better_solution


RANGE_A = (-2147483648, 2147483647)
RANGE_N = (0, 100000)


class TestExercise(unittest.TestCase):
    """
    example - positive answer
    example1 - zero answer
    extreme_empty - empty sequence
    extreme_single - 1 element sequence
    extreme_two_elems - 2 element sequence
    extreme_negative1 - three equal negative numbers
    extreme_arith_overflow1 - overflow test, 3 maxints
    extreme_arith_overflow2 - overflow test, 10 and 2 minints
    extreme_arith_overflow3 - overflow test, 0 and 2 maxints
    medium1 - chaotic sequence of values [0..100K] length 30
    medium2 - chaotic sequence of values [0..1K] length 50
    medium3 - chaotic sequence of values [0..1K] length 100
    large1 - chaotic sequence of values [0..100K] length 10K
    large2 - 1 followed by ascending sequence ~50K elements [0..100K] length ~50K
    large_random - chaotic sequence [0..1M] length 100K
    large_negative - chaotic sequence of negative values [-1M..-1] length 100K
    large_negative2 - chaotic sequence of negative values [-10..-1], length 100K
    large_negative3 - sequence of -1 values, length 100K
    """

    def test_example(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)
        self.assertEqual(solution([10, 50, 5, 1]), 0)

    def test_lowballs(self):
        self.assertEqual(0, solution([]))
        self.assertEqual(0, solution([0]))
        self.assertEqual(0, solution([0, 1]))

    def test_simple(self):
        A = [5, 3, 3]
        self.assertEqual(1, solution(A))

    def test_large_negative(self):
        self.assertEqual(0, solution([-1] * RANGE_N[1]))


if __name__ == '__main__':
    unittest.main()
