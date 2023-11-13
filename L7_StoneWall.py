"""
# StoneWall - Cover "Manhattan skyline" using the minimum number of rectangles."

https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#---------------
# Solution
https://app.codility.com/demo/results/trainingJB7TMF-6RY/

The worst case is: you have a series of columns, all one cell wide,
because the height of the wall is all over the place.
But that's not actually likely as, somewhere no matter how far apart, the height
of the wall will be the same at two different points. So from that column to
the next can be a "block" and then you just have to work out how many little
blocks sit on top of that.
Focus on the points where the wall is at the same height, then that we do
a bit of recursion for the number of blocks above that.
Now reflect that we're looking for an integer output.  How do we get there?
When do we increment that?

We know there is almost certainly a stack involved.
So start with a stack.
Push the height onto the stack.
If the next number is at the same height! great we can extend the block - do nothing.
If the next number is higher, then push that onto the stack.
When the next number is lower, pop the stack and count that as a "block".
Basically, we push higher, not equal, numbers onto a stack, then when they come
off the stack we count that as a "block". Don't forget to clear the stack at the end.
Thus:

    while more
        if stack is empty
            push, next
        elif this one is equal to top of stack
            next
        elif this one is higher than top of the stack
            push, next
        else (lower)
            pop, increment counter
            not next, but continue with this one
    add size of the stack to counter
    return counter
"""
import unittest


def solution(H: list) -> int:
    blocks = 0
    i = 0
    stack = list()
    while i < len(H):
        if not len(stack):
            stack.append(H[i])
        elif H[i] == stack[-1]:
            i += 1
        elif H[i] > stack[-1]:
            stack.append(H[i])
            i += 1
        else:   # this is lower than stack
            stack.pop()
            blocks += 1
    else:
        blocks += len(stack)
    return blocks


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([1, 1]), 1)
        self.assertEqual(solution([2, 1]), 2)
        self.assertEqual(solution([1, 2]), 2)
        self.assertEqual(solution([2, 2]), 1)
        self.assertEqual(solution([1, 2, 1]), 2)
        self.assertEqual(solution([2, 1, 2]), 3)
        self.assertEqual(solution([1, 2, 2, 1]), 2)
        self.assertEqual(solution([1, 2, 1, 2]), 3)
        self.assertEqual(solution([2, 1, 1, 2]), 3)
        self.assertEqual(solution([8, 8, 5, 7, 9, 5, 7, 4, 8]), 7)



if __name__ == "__main__":
    unittest.main()
