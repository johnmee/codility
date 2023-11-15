"""
MaxProfit - Given a log of stock prices compute the maximum possible earning. - Maximum slice problem.

An array A consisting of N integers is given.
It contains daily prices of a stock share for a period of N consecutive days.
If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N,
then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P].
Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048.
If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354.
Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

    def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days,
returns the maximum possible profit from one transaction during this period.
The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..400,000];
        each element of array A is an integer within the range [0..200,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#---------------
The "Maximum Slice" reading notes present the logic and solution for this one.
Applying it by rote works perfectly, as seen in my "clumsy" solution.

But if we stop to work out what is actually going on here, we can rewrite it
to be much simpler and easier to understand.  In fact we are simply looking
for the lowest value closing of the market, and highest closing it has after that day.
So by capturing the lowest value, and comparing each subsequent close against that
its pretty easy to determine the max profit...

https://app.codility.com/demo/results/trainingMN7WGM-K5H/
"""
import unittest


def clumsy_but_O_N_solution(A: list) -> int:
    if len(A) < 2:
        return 0
    max_todate = max_slice = 0
    close_yesterday = A[0]
    for close_today in A[1:]:
        change = close_today - close_yesterday
        max_todate = max(0, max_todate + change)
        max_slice = max(max_slice, max_todate)
        close_yesterday = close_today
    return max_slice


def solution(A: list) -> int:
    """
    As you go, remember the lowest close seen todate.
    If the max possible profit was to buy at the lowest and sell today,
    then capture the max_profit as today.
    """
    max_profit = 0
    lowest_close = 200000
    for close in A:
        lowest_close = min(close, lowest_close)
        max_profit = max(close - lowest_close, max_profit)
    return max_profit


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([23171]), 0)
        self.assertEqual(solution([100, 99]), 0)
        self.assertEqual(solution([100, 101]), 1)
        self.assertEqual(solution([100, 99, 101]), 2)
        self.assertEqual(solution([98, 99, 101]), 3)

        self.assertEqual(solution([23171, 21011, 21123, 21366, 21013, 21367]), 356)



if __name__ == "__main__":
    unittest.main()
