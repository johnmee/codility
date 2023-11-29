"""
MaxSliceSum - Find a maximum sum of a compact subsequence of array elements.

A non-empty array A consisting of N integers is given.
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0

the function should return 5 because:

        (3, 4) is a slice of A that has sum 4,
        (2, 2) is a slice of A that has sum −6,
        (0, 1) is a slice of A that has sum 5,
        no other slice of A has sum greater than (0, 1).

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..1,000,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000];
        the result will be an integer within the range [−2,147,483,648..2,147,483,647].

Copyright 2009–2023 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
#---------------
The solution is provided in the lesson notes: https://codility.com/media/train/7-MaxSlice.pdf

"""
import unittest


def brute_solution(A):
    """
    O(N**3) - 69%
    https://app.codility.com/demo/results/trainingUNFVBA-ZJ7/
    """
    n = len(A)
    result = -2147483648
    for p in range(n):
        for q in range(p, n):
            sum = 0
            for i in range(p, q + 1):
                sum += A[i]
            result = max(result, sum)
    return result


def less_brute_solution(A):
    """
    O(N**3) - 69%
    https://app.codility.com/demo/results/trainingHB34PG-KWS/
    """
    n = len(A)
    result = -2147483648
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result = max(result, sum)
    return result


def solution(A):
    """
    O(N) - 100%
    https://app.codility.com/demo/results/training4V9GS5-FV2/

    This covers all possibilities in a recursive way:
    as we progress down the line, there are only 3 possible candidates for the
    maximum:
     a) this number alone, or
     b) the max we've seen so far plus this number, or
     c) the best slice so far (which is the better of (b), or what we have)
    """
    max_slice = -2147483648
    max_ending = 0
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_ending, max_slice)
    return max_slice


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(-10, solution([-10]))
        self.assertEqual(-2, solution([-2, -2]))
        self.assertEqual(1, solution([-2, 1]))
        self.assertEqual(5, solution([3, 2, -6, 4, 0]))
        self.assertEqual(4, solution([4]))



if __name__ == "__main__":
    unittest.main()
