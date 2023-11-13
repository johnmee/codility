"""
# Nesting
https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S is made only of the characters '(' and/or ')'.

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#---------------
# Solution
This is exactly the same problem and solution as "L7_Brackets", so I just cut/pasted
that solution and it worked perfectly.

Loop over the incoming chars.
If we get an opening bracket, push the closing bracket on to a stack.
If we get a closing bracket pop one off the stack, if it doesn't match: fail.
If we get a closing bracket and the stack is empty: fail.
If the string ends and the stack is empty: success.
O(N) https://app.codility.com/demo/results/trainingFVQXB8-TZB/
"""

import unittest


def solution(S: str) -> int:
    brackets = {"[": "]", "(": ")", "{": "}"}
    stack = []
    for char in S:
        if char in brackets.keys():
            stack.append(brackets[char])
        elif char in brackets.values():
            if len(stack) == 0 or stack.pop() != char:
                return 0
    return 1 if len(stack) == 0 else 0


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution("())"), 0)
        self.assertEqual(solution("(()(())())"), 1)


if __name__ == "__main__":
    unittest.main()
