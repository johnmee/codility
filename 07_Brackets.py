"""
# Brackets

Determine whether a given string of parentheses (multiple types) is properly nested.

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0,
as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
---
# Solution

Loop over the incoming chars.
If we get an opening bracket, push the closing bracket on to a stack.
If we get a closing bracket pop one off the stack, if it doesn't match: fail.
If we get a closing bracket and the stack is empty: fail.
If the string ends and the stack is empty: success.
O(N) https://app.codility.com/demo/results/training9SF7XT-JNZ/
"""
import unittest


def solution(S):
    """Brackets.

    :param S: list[str]
    :return: [int] 1 if valid else 0
    """
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
    example1: example test 1
    example2: example test 2
    negative_match: invalid structures
    empty: empty string
    simple_grouped: simple grouped positive and negative test, length=22
    large1: simple large positive test, 100K ('s followed by 100K )'s + )(
    large2: simple large negative test, 10K+1 ('s followed by 10K )'s + )( + ()
    large_full_ternary_tree: tree of the form T=(TTT) and depth 11, length=177K+
    multiple_full_binary_trees: sequence of full trees of the form T=(TT),
                                depths [1..10..1], with/without some brackets at the end, length=49K+
    broad_tree_with_deep_paths: string of the form [TTT...T] of 300 T's,
                                each T being '{{{...}}}' nested 200-fold, length=120K+
    """

    def test_examples(self):
        self.assertEqual(solution("{[()()]}"), 1)
        self.assertEqual(solution("([)()]"), 0)
        self.assertEqual(solution(""), 1)
        self.assertEqual(solution("{[(V)(W)]}"), 1)
        self.assertEqual(solution("[{V}[W]]"), 1)
        self.assertEqual(solution("[{V(W)]"), 0)
        self.assertEqual(solution(")"), 0)


if __name__ == "__main__":
    unittest.main()
