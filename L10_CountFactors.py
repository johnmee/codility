"""
CountFactors - Count factors of given number n.

A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:
    def solution(N)
that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24.
There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#----------------
The solution is given to you in the notes:
https://codility.com/media/train/8-PrimeNumbers.pdf
"""
import unittest


def solution(n: int) -> int:
    """
    For every int, i, from 1 to N
        if i divides n evenly
            increment the count

    Now, observe that if we know one divisor, we can trivially determine the other.
    Also, observe that one of those two must be less then the square root of N.
    Thus we only need to loop up to root N, then double that count... if we take care to count the square itself only once.
    """
    i = 1
    result = 0
    while i * i < n:
        if n % i == 0:
            result += 2
        i += 1
    if i * i == n:
        result += 1
    return result


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(24), 8)


if __name__ == "__main__":
    unittest.main()
