"""
# Number of Disc Intersections

Compute the number of intersections in a sequence of discs.

https://codility.com/programmers/task/number_of_disc_intersections/

## Problem Description

We draw N discs on a plane. The discs are numbered from 0 to N - 1. A zero-indexed array A of N non-negative
integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0)
and radius A[J].

We say that the J-th disc and K-th disc intersect if J <> K and the J-th and K-th discs have at least one common
point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

https://codility-frontend-prod.s3.amazonaws.com/media/task_static/number_of_disc_intersections/static/images/auto/0eed8918b13a735f4e396c9a87182a38.png

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of
intersecting discs. The function should return -1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

---
In other words:
With every value in the array,
draw a circle with its center on the x-axis where the index lies,
and a radius of its value.
Count the number of intersections between all the circles.

## Solution

The brute-force solution visits every circle with every other circle.
It is: O(N**2) 50% (100% correct, 12% performance)
https://app.codility.com/demo/results/trainingYTV8B5-MTB/

The "fast" solution  considers where the openings and closings occur, but
abandons their individual pairings.  Thus, we have points on a line, which
are either an "opening" or a "closing" of a circle.  Sort the two lists then
step through all the "closing" points and count the number of "opening" points
which have not yet been closed.
Aside from the sort, O(log(N)), we can achieve the answer in single pass O(N).

 * collect all the "openings" and "closings" into two lists.
 * sort both lists
 * for every closing
    * for every opening between this closing and the last
      * mark an intersection
 * that's our answer

It is: O(N*log(N)) 100%.
https://app.codility.com/demo/results/trainingQKGBMA-DQ7/
"""
import itertools
import unittest

MAX_INTERSECTIONS = 10000000  # Runaway breakpoint.


def brute_solution(A):
    """Brute force - visit and test every combination."""
    # Create tuples of the x coordinates where each circle opens and closes.
    minmax = []
    for k, v in enumerate(A):
        minmax.append([k - v, k + v])

    # Sort them by their opening coordinate.
    minmax.sort()

    def intersect(ja, jb, ka, kb):
        """True if J intersects with K."""
        return ka <= jb or jb >= ka or (ka >= ja and kb <= jb)

    # Count all the intersections of all the combinations of circles.
    count = 0
    for j, k in itertools.combinations(minmax, 2):
        if intersect(*(j + k)):
            count += 1
    return count


def fast_solution(A):
    """Intervals on a line solution."""
    # Create lists of the opening and closing points; sort them.
    openings, closings = [], []
    for point, radius in enumerate(A):
        openings.append(point - radius)
        closings.append(point + radius)
    openings.sort()
    closings.sort()

    # Every time a disc closes, add the discs that opened since the last close.
    intersections = 0
    iopen = 0
    for iclose in range(len(closings)):  # As every disc closes,
        while iopen < len(openings) and openings[iopen] <= closings[iclose]:
            iopen += 1  # Count the discs that are open.
        intersections += iopen - iclose - 1
        if intersections > MAX_INTERSECTIONS:  # Capture runaway monsters.
            return -1
    return intersections


solution = fast_solution


class TestExercise(unittest.TestCase):
    """
    example1: example test
    simple1
    simple2
    simple3
    extreme_small: empty and [10]
    small1
    small2
    small3
    overflow: arithmetic overflow tests
    medium1
    medium2
    medium3
    medium4
    10M_intersections: 10.000.000 intersections
    big1
    big2
    big3: [0]*100.000
    """

    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([10]), 0)
        self.assertEqual(solution([1, 1]), 1)

    def test_extreme_large(self):
        A = [10000000] * 100000
        self.assertEqual(solution(A), -1)


if __name__ == "__main__":
    unittest.main()
