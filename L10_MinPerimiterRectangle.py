"""
MinPerimeterRectangle - Find the minimal perimeter of any rectangle whose area equals N.

An integer N is given, representing the area of some rectangle.
The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
The goal is to find the minimal perimeter of any rectangle whose area equals N.
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Write a function:
    def solution(N)
that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#
https://app.codility.com/demo/results/trainingWAMZPR-DH7/
"""
import math
import sys

import unittest


def solution(n: int) -> int:
    """
    For all the integer factors of n
        calculate the perimeter
    return the smallest perimeter
    """
    min_perim = sys.maxsize

    for A in range(1, int(math.sqrt(n)) + 1):
        if n % A == 0:
            B = n // A
            perimeter = 2 * (A + B)
            min_perim = min(min_perim, perimeter)
    return min_perim


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(1), 4)
        self.assertEqual(solution(2), 6)
        self.assertEqual(solution(3), 8)
        self.assertEqual(solution(4), 8)
        self.assertEqual(solution(5), 12)

        self.assertEqual(solution(30), 22)


if __name__ == "__main__":
    unittest.main()
