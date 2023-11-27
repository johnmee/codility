"""
Equileader
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.


A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ...,
A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#----------------

The basis solution is provided in the lesson. See 'get_leader' below.
Even though we pass over the entire list a number of times, that is ok because
it is an ordinal number of times, so counts as O(N).

To find a leader there are two passes:
1. to identify the most frequent number
2. to count how many of those there are
Then just compare that to the number of numbers in the list.

This puzzle expands on that algorithm by searching for leaders both before,
and after, the index point.

The naive solution is to step through and solve for leaders on either side as
you go.

The performant solution is to first solve for the leader, then step through
the list keeping track of how many times the leader is before/after the index,
and comparing that to the count of items before/after the index.
"""
import unittest


def get_leader(A: list) -> int:
    """Return the leader of list, or None."""
    # First pass determines the most frequently seen number.
    n = len(A)
    size = 0
    value = None
    for k in range(n):
        if size == 0:
            size = 1
            value = A[k]
        else:
            size = size + 1 if value == A[k] else size - 1

    # 2nd pass counts the number of occurences of the most frequent number.
    leader = -1
    candidate = -1
    count = 0
    if size > 0:
        candidate = value
    for k in range(n):
        if A[k] == candidate:
            count += 1

    # If count is more than half, then the most frequent number is a leader.
    if count > n//2:
        leader = candidate

    return leader


def slow_solution(A: list) -> int:
    """Correct, but non-performant solution.

    O(N ** 2)
    For each point in the array,
        find the left and right leaders
        increment the count if they are the same number.
    """
    result = 0
    for n in range(1, len(A)):
        left_leader = get_leader(A[:n])
        right_leader = get_leader(A[n:])
        if left_leader == right_leader:
            result += 1
    return result


def solution(A: list) -> int:
    """
    O(N)

    I was a bit frustrated by codility with this one because list operations
    were slow.  I initially used a stack for the first pass, which was O(N),
    but failed one of the performance tests (88%). Then I was also using a list
    comprehension for the second pass, which failed the same performance test.

    I also got stuck in a mental cloud trying to solve is_right_leader: the
    0-based index gave me a headache, but I couldn't get myself to settle and
    just nut it out; instead I kept banging away with +-1 variations believing
    that I would not have to think it through, but just get lucky eventually.

    https://app.codility.com/demo/results/trainingYU9XHJ-63H/
    """
    # First pass finds the most frequent number.
    candidate, count = None, 0
    for val in A:
        if count == 0:
            candidate, count = val, 1
        elif val == candidate:
            count += 1
        else:
            count -= 1

    # Second pass to count occurences of the most frequent number.
    occurences = 0
    for v in A:
        if v == candidate:
            occurences += 1

    # Third pass to compare counts left and right.
    result = 0
    left, right = 0, occurences
    for idx, val in enumerate(A):
        if candidate == val:
            left += 1
            right -= 1
        is_left_leader = left * 2 > idx + 1
        is_right_leader = right * 2 > len(A) - (idx + 1)
        if is_left_leader and is_right_leader:
            result += 1

    return result


class TestExercise(unittest.TestCase):
    """
    """
    def test_leader(self):
        self.assertEqual(get_leader([4]), 4)
        self.assertEqual(get_leader([4, 0]), -1)
        self.assertEqual(get_leader([4, 3]), -1)
        self.assertEqual(get_leader([4, 4]), 4)
        self.assertEqual(get_leader([4, 3, 4]), 4)
        self.assertEqual(get_leader([1, 3, 4]), -1)

    def test_examples(self):
        self.assertEqual(0, solution([4,3]))
        self.assertEqual(1, solution([4,4]))
        self.assertEqual(2, solution([4,3,4,4,4,2]))


if __name__ == "__main__":
    unittest.main()
