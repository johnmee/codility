"""
CountTriangles
Count the number of triangles that can be built from a given set of edges.

https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R].
In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12

There are four triangular triplets that can be constructed from elements of this
array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).
Which is: [10, 5, 8], [10, 5, 12], [10, 8, 12] and [5, 8, 12].

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the number of
triangular triplets in this array.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5     A[3] = 1    A[4] = 8    A[5] = 12

the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Copyright 2009–2024 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.

--------------------------
This problem is called the "triangle inequality theorem".  It
observes that a triangle cannot form unless all three sides are longer than the
other two sides combined.  Reseasrching this theorem might help understand the puzzle
domain better.

The brute force solution is very straight-forward: loop over every combination
and test it, increment if it passes the test.  For this solution you can get 63%.

For 100%, the trick is to sort the array before working on it.
With a sorted list we can make assumptions to reduce the number of loops we must complete.
The savings outweigh the cost of the sort.

There are three lengths, or sides, involved.  An outer loop visits every side in turn.
Then, inside that outer loop, a "caterpillar" walks through its options of second and third sides.

The inner loop presents all the sides which are longer than, ie to the right,
of the side provided by the outer loop.  Thus, we have an x side which does not change,
a y side which is determined by the inner loop, and a z side which starts with the candidate next longest to y,
and becomes incrementally longer.

Inside the inner loop, we test the length of the next side in the sequence for a triangle:
* If the third side is longer than both combined it cannot form a triangle, and we stop searching:
    - all the lengths to the right of this one are even longer so we know they will fail too
    - so let's move the tail of the caterpiller (advance the inner loop (y))
* But, if the third side is shorter than both combined, then we can form a triangle:
    - the next side might form a triangle as well
    - so let's move the head of the caterpillar (increment z)

Thus, the inner loop is a caterpillar over two longer sides which are combined with the shorter side from the outer loop.
And because the list is sorted we can stop and reset the caterpillar immediately that the test starts to fail.
So our performance boost is gained by skipping those longer lengths which we know cannot form triangles.

But what about working out the count?

We count the triangles every time the caterpillar is reset.  That is, when the inner loop increments, when the tail moves.

Whenever the caterpillar is extended, we have found triangles.  So before we reset, we see if the caterpillar
was 'stretched' at all. That is, if z is no longer the next in sequence after y, then we found triangles!
So we add the length of that 'stretch' in the caterpillar to the total, since it reflects how many triangles
we found.

It took me a very long time to understand exactly how this one works.  Many people
have posted solutions without any explanation.  I dare to question how many have copied
others without fully understanding how the 100% solution works.  I hope this explanation can shed light on
the solution for you.

Minor notes:
In the sorted solution we do not need to test all combinations of the sides because we know we are comparing
the sum of the two smaller sides against the longest side.  (a[x] + a[y] > a[z]).

When two sides are exactly the same length we do have a triangle (isoceles).
"""
import itertools
import unittest


def is_triangle(x, y, z):
    """True if x, y, z form a 'triangle'"""
    return x + y > z and x + z > y and z + y > x


def solution_brute(a: [int]) -> int:
    """Return a count of triangles.

    Brute force by looping over every combination.
    63% https://app.codility.com/demo/results/training9RDYDW-TEX/
    """
    result = 0
    a.sort()
    for points in itertools.combinations(a, 3):
        if is_triangle(*points):
            result += 1
        # print(points, is_triangle(*points), result)
    return result


def solution(a: [int]) -> int:
    """Return a count of triangles.

    100%  https://app.codility.com/demo/results/training2YH7B6-JD7/
    """
    a.sort()
    n = len(a)
    result = 0
    for x in range(n - 2):                          # for every side
        z = x + 2                                   # set the head of the caterpillar
        for y in range(x + 1, n - 1):               # set the tail of the caterpillar
            while z < n and a[x] + a[y] > a[z]:     # is this a triangle?
                z += 1                              # yes: inch the caterpillar forward
            result += z - y - 1                     # accumulate the 'stretch' of the caterpillars
    return result


def solution_verbose(a: [int]) -> int:
    """Return a count of triangles.

    100% but with print statements to try to see how it works.

    The horizontial line indicates which loop you are in:
        [1, 2, 5, 8, 10, 12]
        ‾--_-_-_‾--_-_‾-__-‾-_
         [1, 2, 5, 7, 9]
        ‾--_-_‾--_‾-_
         [1, 2, 2, 3, 3, 12]
        ‾-_--__-‾-__--‾-_-‾-
         [1, 2, 2, 3, 3]
        ‾-_--__‾-__-‾-_
         [1, 2, 3, 4, 5]
        ‾--_-_‾-_-_‾-_
         [1, 2, 3, 4, 5]
        ‾--_-_‾-_-_‾-_
         [1, 2, 3, 4, 5]
        ‾--_-_‾-_-_‾-_
         [1, 2, 2]
        ‾-_

    Snapshot of the count and the indexes before moving the caterpillars tail:
        0 | 0 1 2
        0 | 0 2 3
        0 | 0 3 4
        0 | 0 4 5
        0 | 1 2 3
        0 | 1 3 4
        0 | 1 4 5
        2 | 2 3 6
        3 | 2 4 6
        4 | 3 4 6
    """
    a.sort()
    n = len(a)
    result = 0
    # print("\n", a)
    for x in range(n - 2):
        # print(u'\u203e', end='')
        z = x + 2
        for y in range(x + 1, n - 1):
            # print("-", end='')
            while z < n and a[x] + a[y] > a[z]:
                # print("_", end='')
                z += 1
            result += z - y - 1
            print(result, '|', x, y, z)
    return result


solution = solution_verbose


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(4, solution([10, 2, 5, 1, 8, 12]))
        # self.assertEqual(1, solution([1, 2, 5, 7, 9]))
        # self.assertEqual(6, solution([1, 2, 2, 3, 3, 12]))
        # self.assertEqual(6, solution([1, 2, 2, 3, 3]))
        # self.assertEqual(3, solution([1, 2, 3, 4, 5]))
        # self.assertEqual(3, solution([5, 2, 3, 4, 1]))
        # self.assertEqual(3, solution([1, 2, 5, 4, 3]))
        # self.assertEqual(1, solution([1, 2, 2]))
        # self.assertEqual(0, solution([]))


if __name__ == "__main__":
    unittest.main()
