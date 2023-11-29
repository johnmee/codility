"""
MaxDoubleSliceSum - Find the maximal sum of any double slice.

A non-empty array A consisting of N integers is given.
A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:
    def solution(A)
that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#---------------
This was an absolute bitch.  I spent a whole day and still couldn't work out the optimum solution; I spent most of that
time fiddling around with the ends of the array, trying to get the first and last values right. But ultimately my
fault was not that but the expectation that it could be solved linearly without need to use storage. Wrong.
I cheated in the end and googled it. As it seems many/most people have.
I digested those and rewrote adjusting it for my own golden flavour.
It all looks so simple in the end... could you not cry?!
"""
import unittest
import sys


def brute_solution(A):
    """O(N**3) 53%
    https://app.codility.com/demo/results/trainingWZRJA5-4TD/

    for every x, y and z:
        calculate the sum
        save if biggest
    return biggest
    """
    result = -sys.maxsize
    n = len(A)
    for x in range(0, n - 2):
        for y in range(x + 1, n - 1):
            for z in range(y + 1, n):
                val = sum(A[x + 1:y]) + sum(A[y + 1:z])
                result = max(result, val)
                print(val, f"({x}, {y}, {z})", A[x + 1:y], A[y + 1:z])
    return result


def disappointing_solution(A):
    """O(N ** 2) or O(N ** 4) or O(N ** 3) 46%
    https://app.codility.com/demo/results/training2K3FF9-JTU/

    Step from left to right using the previous (MaxSliceSum) solution to
    solve the left and right slices.  I had high hopes, but it creates lots of
    wasted cycles by recalculating the same slices repeatedly.
    """
    def max_slice(A):
        result = -2147483648
        max_ending = 0
        for a in A:
            max_ending = max(a, max_ending + a)
            result = max(max_ending, result)
        return max(result, 0)

    result = -sys.maxsize
    n = len(A)
    for x in range(1, n-1):
        left_slice, right_slice = A[1:x], A[x+1:-1]
        left_sum, right_sum = max_slice(left_slice), max_slice(right_slice)
        result = max(result, left_sum + right_sum)
        # print(f"{x}, {left_slice}={left_sum} {right_slice}={right_sum}, {result}")
    return result


def gold_solution(A):
    """O(N) 100%
    https://app.codility.com/demo/results/trainingWD47QG-7HE/

    First, create a prefix-sum for every position in the array with the max_slice looking right of each position.
    Now walk the list building the left max-slice.  As you go also add the left max-slice to the corresponding
     right max-slice from the list, and track the max-double-slice.

    for every value (going backwards)
        calculate, and record, the max slices from the right to left

    for every value (going forwards)
        calculate the max slices to the left
        add the left and right max-slices together
        keep the biggest number you see
    """
    # Create a list of max-slices to the right of each position in the array.
    right_sums = []
    right_sum = 0
    for a in reversed(A[1:-1]):
        right_sums += [right_sum]
        right_sum = max(0, right_sum + a)
    right_sums.reverse()

    # Combine the original array with the right max-slices above and step through both together.
    #   Calculating the max-slice to the left and the max-double-slice along the way
    max_double_sum = left_sum = 0
    for a, right_sum in zip(A[1:-1], right_sums):
        max_double_sum = max(max_double_sum, left_sum + right_sum)
        left_sum = max(0, left_sum + a)

    return max_double_sum


solution = gold_solution


class TestExercise(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(0, solution([4, 4, 4]))
        self.assertEqual(17, solution([3, 2, 6, -1, 4, 5, -1, 2]))
        self.assertEqual(0, solution([-4, -5, -1, -5, -7, -19, -11]))
        self.assertEqual(26, solution([6, 1, 5, 6, 4, 2, 9, 4]))


if __name__ == "__main__":
    unittest.main()
