"""
Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.

An array A consisting of N integers is given.
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7)
and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which
the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#----
The (prescribed) solution works on the mothematical knowledge that if you step through the
list sequentially and proceed to remove pairs of neighbours which are not the
same value, this does not alter the 'dominator's balance of the list.

The stack-inspired solution

    Start with no dominator and a count of zero
    for every value
        if there is no dominator, make this the dominator
        elif this value matches the dominator, increment the count
        elif the count is positive, decrement the count
        else (count is zero), make this value the dominator
    count the number of times the dominator appears, record the position of one of them
    if more than half
        return the recorded position


My arguably simpler more pythonic solution passes through the list and maintains a count
of each value then, a pass over the recorded values reveals the dominator.  We
can only get away with this in python because codility does not record the 'in' operator as
a complete loop over all the possible dictionary keys.

    create an empty dictionary
    for every value
        if the value is not a dict key
            using the value as the key add a tuple containing 1 (the count) and the current position
        if the value is a dict key
            using the value as the key, increment the count in the tuple
    for every key in the dict
        if the count is greater than half the size of the input
            return the position

https://app.codility.com/demo/results/training3EXZ32-XQR/
"""
import unittest


def solution(A: list) -> int:

    # Count the values.
    counts = {}
    for pos, val in enumerate(A):
        if val not in counts.keys():    # Codility seems unsure if 'in' makes it O(N*log(N)) or O(N).
            counts[val] = (1, pos)
        else:
            counts[val] = (counts[val][0] + 1, counts[val][1])

    # Return the dominator, or not.
    result = -1
    half = len(A)//2
    for count, pos in counts.values():
        if count > half:
            result = pos
            break
    return result


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertIn(solution([3]), {0})
        self.assertIn(solution([3, 4]), {-1})
        self.assertIn(solution([4, 4]), {0, 1})
        self.assertIn(solution([3, 3, 4, 4]), {-1})
        self.assertIn(solution([3, 4, 3, 2, 3, -1, 3, 3]), {0, 2, 4, 6, 7})



if __name__ == "__main__":
    unittest.main()
