"""
MinAvgTwoSlice

Find the minimal average of any slice containing at least two elements.

https://codility.com/programmers/task/min_avg_two_slice/


----------------
# My Analysis

This problem doesn't even need prefix-sums, so that was a big red-herring. Well mostly.
 The 'trick' is not in the coding at all, but in a realisation about the nature of the problem...

You're looking for the smallest average of a series of numbers.  At first it looks like you
 have to permutate over an ever increasing collection of averages of various lengths.
 But, at some point, you'll realize that a small number will always pull the average down,
 no matter what numbers are around it.

Thus, given that it, takes a minimum of two numbers to make an average, you're really only looking for that pair
 of numbers which combine to provide the smallest total.
 To verify this pressumption, consider the slope that the curve of graphing the moving average
 of the pair would make. Irrespective of the size of the average, the gradient will always tilt
 down, however slightly, when you come across a small number.

Coding a two-point average is dead simple: just walk through the sequence from left to right adding each pair
 together and tracking the position of the smallest pair.

I couldn't believe it would be this easy, but couldn't resist, and gave it a run... 50%.

After a run the report tells you which tests it failed and I couldn't help but notice it failed
 for 3 point moving averages.  That was perplexing because I couldn't see how to create a three
 point average that would change the results over a two point average!  So I googled it.

The explanation is sequences with an odd number of integers... namely 3.
 For example: [-8, -6, -10]
 In this sequence the two-point averages are -7 and -8, so the answer would be index point 1 (the -6).
 But note that the three poit average is also -8, and commences one point earlier, on index point 0.
 So the correct answer is 0.

And we're back questioning whether this scenario will play out for sequences of length 4, 5, 6 and beyond.
 Will it?

Well, consider a sequence of 4 values. [1,2,2,1]. It has three two-point averages. [1,2],[2,2],[2,1].
 Which evaluate to [1.5, 2, 1.5].  The four-point average is 1.5.
 How about [1,-1, 1,-1]?  The two-points averages are [0,0,0] and the four-point average is[0].
 You can play this out all day, only to find that a four-point average can never be less than one
 of the two-point averages within it.

Ok, then why do we need the three point average?
 Consider [1, -1, 1, -1]? The two-point averages all come to 0.  And we've already established that
 a four-point average (of 0) can never best the two-point averages.
 But the three-point averages are 0.33 and -0.33.
 So the correct answer is index point 1.

And a 5-point sequence?
 Ok, [-1, 1, -1, 1, -1].
 Two points = [0, 0, 0, 0] (best answer is 0)
 Three points = [-0.33, 0.33, -0.33] (better answer is 1)
 Four points = [0, 0] (just like the two points)
 Five points = [-0.33] (same as three points answer).

By this point my understanding is that the two and three-point averages act like a factorial of all the
longer length averages.  They may be able to match one or other, but will never beat them.

Thus we can confidently write some trivial code to do a single pass solution which considers just
 the two and three-point averages.

-------------------
# Problem Description

A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q),
such that 0 <= P < Q < N, is called a slice of array A (notice that the slice contains at least
two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided
by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers, returns the starting
position of the slice with the minimal average. If there is more than one slice with a minimal
average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Assume that:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [-10,000..10,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the
          storage required for input arguments).

Elements of input arrays can be modified.
"""


import unittest
import random


RANGE_A = (2, 100000)
RANGE_N = (-10000, 10000)


def solution(A):
    """
    :param A: array of integers
    :return: an integer
    """
    # the lowest average we've ever seen
    lowest_avg = RANGE_N[1]
    # the starting point of the lowest average seen
    lowest_idx = 0
    # the value we saw two iterations ago
    second_last = None
    # the value we saw last iteration
    last = None

    # for every number in the sequence
    for idx, this in enumerate(A):

        # if we have seen three numbers calculate the three-point average
        # and, if necessary, keep it.
        if second_last is not None:
            three_avg = (second_last + last + this) / 3.0
            if three_avg < lowest_avg:
                lowest_avg = three_avg
                lowest_idx = idx - 2

        # if we have seen two numbers calculate the two-point average
        # and, if necessary, keep it.
        if last is not None:
            two_avg = (last + this) / 2.0
            if two_avg < lowest_avg:
                lowest_avg = two_avg
                lowest_idx = idx - 1

        # print idx, second_last, last, this, '\t\t', two_avg, three_avg, '\t\t', lowest_avg, lowest_idx

        second_last = last
        last = this

    return lowest_idx


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]), 1)
        self.assertEqual(solution([5, 2, 2, 100, 1, 1, 100]), 4)
        self.assertEqual(solution([11, 2, 10, 1, 100, 2, 9, 2, 100]), 1)

    def test_three(self):
        # self.assertEqual(solution([-3, -5, -8, -4, -10]), 2)
        # self.assertEqual(solution([-8, -6, -10]), 0)
        self.assertEqual(solution([1, -1, 1, -1]), 1)

    def test_random(self):
        A = [random.randint(*RANGE_N) for _ in xrange(2, 10)]
        print A
        print solution(A)

    def test_large_ones(self):
        """Numbers from -1 to 1, N = ~100000"""
        # how to test?

    def test_extreme(self):
        A = [RANGE_N[1]] * (RANGE_A[1] / 3) + [RANGE_N[0]] * (RANGE_A[1] / 3)
        idx = solution(A)
        print idx, A[idx-3:idx+3]

if __name__ == '__main__':
    unittest.main()
