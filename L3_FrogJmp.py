"""
# FrogJmp

Count minimal number of jumps from position X to Y.

A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position
 greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its
 target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from
position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest


def solution(X, Y, D):
    """Calculate the miminum number of jumps from X to Y.

    :param X: [int] Start position.
    :param Y: [int] End position.
    :param D: [int] Size of the jump.
    :return: Minium number of jumps in O(1) time and space complexity.

    * Integer divide the difference between the start and end position by the jump size.
    * If there is a remainder, froggy needs one more hop to get past the end.
    * Otherwise froggy landed right on it!  Yay for frog.
    """
    quot, rem = divmod(Y - X, D)
    return quot + 1 if rem != 0 else quot


class TestFrogJump(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution(10, 85, 30), 3)

    def test_one(self):
        self.assertEqual(solution(0, 10, 1), 10)

    def test_big_steps(self):
        self.assertEqual(solution(0, 10, 20), 1)

    def test_even_steps(self):
        self.assertEqual(solution(10, 100, 10), 9)

    def test_equal_steps(self):
        self.assertEqual(solution(10, 10, 10), 0)

    def test_odd_steps(self):
        self.assertEqual(solution(9, 29, 10), 2)


if __name__ == "__main__":
    unittest.main()
