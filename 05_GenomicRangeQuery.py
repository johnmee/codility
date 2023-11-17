"""
# GenomicRangeQuery

Find the minimal nucleotide from a range of sequence DNA.

## Problem Description

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which
correspond to the types of successive nucleotides in the sequence. Each nucleotide has an _impact
factor_, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4,
respectively. You are going to answer several queries of the form: What is the minimal impact factor of
nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The
K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the
DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
        whose impact factors are 3 and 2 respectively, so the answer is 2.

        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor
        is 4, so the answer is 4.

        The part between positions 0 and 6 (the whole string) contains all nucleotides, in
        particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q
consisting of M integers, returns an array consisting of M integers specifying the consecutive answers
to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P and Q is an integer within the range [0..N - 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
---

## The problem

I find this descripton hard to digest.  In my own words they're saying:

We'll give you a string, and a list of slices (array indexes) for that string;
What is the "smallest" character in each slice. Change the character to a
known value (A=1, C=2, G=3, T=4) before returning it.

So, it's just a min-value problem, but with a lot of distracting words.
"Find the minimum value in these subsets of a sequence of values."

## The Solutions

The naive solution is to step though every query, pull out the sliced
sequence, sort the string, and the value we need is the first char;
convert it to its number; collect all the results. Done.

Note: the numerical values assigned to the characters, fortunately, sort in
the same order as their character values. We can sort for the
'smallest' character, before converting into their respective integers.

If you're happy with 62%, see the "slow_solution" below. O(N * M)
https://app.codility.com/demo/results/trainingWUE2T7-GUD/

So, how to speed things up?

The naive solution is revisiting slices of the input repeatedly.  If we collect
some metadata, we remove the need for re-visits.

Let's do a "pre-pass" of the sequence, collecting the data we need to answer the
queries quickly.  Enter the "prefix sum" concept...

For the "prefix sum", we step through the char sequence, keeping a count of the
characters we have seen to that point.  For "CAGCCTA" that looks like:

    A = [0,0,1,1,1,1,1,2]
    C = [0,1,1,1,2,3,3,3]
    G = [0,0,0,1,1,1,1,1]
    T = [0,0,0,0,0,0,1,1]

Now, when we can ask "Are there any 'C' types between index 1 and 3?" we can
lookup two values (1=1 & 3=1) in C for the answer (No), without looping over
the actual sequence.

See 'fast_solution'. Score 100/100. O(N+M).
https://codility.com/demo/results/trainingH6PA4P-5V7/
"""
import unittest
import random

# maximum number of neucleotides in a sequence
MAX_N = 100000
# maximum number of queries
MAX_M = 50000

# impact factor of each neucleotide
IMPACT = {"A": 1, "C": 2, "G": 3, "T": 4}


def slow_solution(S, P, Q):
    """
    An easy to implement and understand solution: O(N * M)

    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    """
    # For every query, sort the slice into alphabetical order and the first char
    # is the minimal-factor.
    result = []
    for p, q in zip(P, Q):
        slice = sorted(S[p: q + 1])
        result.append(IMPACT[slice[0]])
    return result


def fast_solution(S, P, Q):
    """
    A faster, but more difficult to implement and understand, solution: 0(N + M)

    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    """
    # Pass 1: Create prefix sums.
    sums = {"A": [0], "C": [0], "G": [0], "T": [0]}
    for nucleotide in S:
        for nucl in sums.keys():
            count = sums[nucl][-1]  # The previous count.
            if nucl != nucleotide:
                sums[nucl].append(count)  # Copy the previous count.
            else:
                sums[nucl].append(count + 1)  # Increment the previous count.

    # Pass 2: Evaluate the queries.
    impacts = []
    for start, end in zip(P, Q):
        for key in "ACGT":  # In order of impact.
            if sums[key][end + 1] > sums[key][start]:  # Is this key is in the slice?
                impacts.append(IMPACT[key])
                break
    return impacts


solution = fast_solution


class TestExercise(unittest.TestCase):
    """
    example: example test
    extreme_sinlge: single character string
    extreme_double: double character string
    simple: simple tests
    small_length_string: small length simple string
    small_random: small random string, length = ~300
    almost_all_same_letters: GGGGGG..??..GGGGGG..??..GGGGGG
    large_random: large random string, length
    extreme_large: all max ranges
    """
    def test_example(self):
        self.assertEqual(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]), [2, 4, 1])
        self.assertEqual(slow_solution("CAGCCTA", [2, 5, 0], [4, 5, 6]), [2, 4, 1])

    def test_random(self):
        seq = [random.choice("ACGT") for _ in range(1, 5000)]
        P_array, Q_array = [], []
        for _ in range(0, len(seq)):
            P = random.randint(0, len(seq) - 1)
            Q = random.randint(P, len(seq) - 1)
            P_array.append(P)
            Q_array.append(Q)
        solution(seq, P_array, Q_array)

    def test_extreme(self):
        S = "T" * MAX_N
        P = [0] * MAX_M
        Q = [MAX_N - 1] * MAX_M
        self.assertEqual(solution(S, P, Q), [4] * MAX_M)


if __name__ == "__main__":
    unittest.main()
