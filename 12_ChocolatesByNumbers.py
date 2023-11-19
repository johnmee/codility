"""
ChocolatesByNumbers - There are N chocolates in a circle. Count the number of chocolates you will eat.

Two positive integers N and M are given.
Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates.
After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0.
Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.
More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:
    def solution(N, M)
that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:
        N and M are integers within the range [1..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#----------------
This is an easy problem _only if you know Euclides Algorithm_ for how to determine the Greatest Common Denominator,
_and_ can you work out how to apply it to the puzzle.  So, it's not at all easy to get the optimal solution, if you don't.

By example, if we have 50 chocolates and eat the 51st chocolates, we do a full circuit of the circle plus one,
and eat all the chocolates in the order of 0,1,2,3... etc.

Similarly for 49. We can eat all the chocolates by 0, 49, 48, 47,... etc.
The greatest common divisor (GCD) between 50 and 51 is 1! And the GCD between 50 and 49 is also 1.
50 chocs divided by 1 is 50! So anytime there is no common denominator (other than 1) we can eat all 50 chocolates.
Interesting.

What about the even numbers on either side of 50? Like 2 and 52? What are the GCDs for 2 and 48?
The GCD for both is 2.  So we can only eat every second chocolate, by either going forward or 'reverse' (loop around)
and eating every second chocolate.

The same happens for 53 and 54. The GCD is 1 and 2 respectively, and we can eat all, or half, the available chocolates,
before hitting upon a number, a *modulus*, that we have seen already.

So 5 and 55? How many chocolates can we eat?  We don't need to think about it, many will know inuitively that
the answer for 5 is 50/5=10.  What about 55? Well its the same, but we just went around the circle to get there.
So, is it about that modulus? The remainder after completing the circle?
55 mod 50 is 5: we don't need to work out the answer to 55 because we know it will be the same as 5.

Now we're getting closer to Euclides.

Euclides is credited as the first person to appreciate that the GCD does not change when you use multiples of the
same numbers. The GCDs for (50,5) and (50,55) are the same as the GCDs of (50,95) and (50, 105): we can substitute
smaller numbers for larger ones without changing the result.

How does that help us with the chocolates?
By removing the complexity of going around and around the circle multiple times.

So resuming the example, the GCD between 50 and whatever other number they give us, M, reduces the problem to a simple
division: 50 divided by the GCD of 50 and M.  The GCD of (50,5) or (50,55) or (50,95) or (50,105) is all 5. 50//5 is 10.
We get to each 10 chocolates no matter how many times we have to go around the circle, because they all reduce to the
same common divisor.

So the answer is to the puzzle is: N // gcd(N,M)

But what is the answer to the GCD?

The Euclides algorithm for GCD repeatedly reduces either of the numbers until we arrive at a situation whereby one of
them can divide the other evenly.  For primes that other number is 1.

The 'reduction' I mentioned is the difference between the two numbers: we reduce the larger of the numbers by the difference between them.
Then repeat. When one of the numbers reaches zero, the GCD of the two must be the other, non-zero, number.

QED?  It is so non-intuitive that we're still talking about Euclides 2300 years after he wrote it down.

https://app.codility.com/demo/results/trainingC5DX6M-P79/
"""
import unittest


def solution(n: int, m:int) -> int:
    """
    """
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    return n // gcd(n, m)


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(10, 4), 5)
        self.assertEqual(solution(1,1), 1)
        self.assertEqual(solution(12,2), 6)
        self.assertEqual(solution(12, 13), 12)
        self.assertEqual(solution(50, 50), 1)
        self.assertEqual(solution(50, 1), 50)
        self.assertEqual(solution(50, 51), 50)
        self.assertEqual(solution(50, 49), 50)
        self.assertEqual(solution(50, 2), 25)
        self.assertEqual(solution(50, 48), 25)
        self.assertEqual(solution(50, 3), 50)
        self.assertEqual(solution(50, 47), 50)
        self.assertEqual(solution(50, 4), 25)
        self.assertEqual(solution(50, 46), 25)
        self.assertEqual(solution(50, 5), 10)
        self.assertEqual(solution(50, 45), 10)

if __name__ == "__main__":
    unittest.main()
