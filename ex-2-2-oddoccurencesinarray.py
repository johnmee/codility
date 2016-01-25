import unittest
import random

# the largest length array we have to handle
MAX_LENGTH = 1000000


def solution(A):
    """
    Find the value that does not have a match in an odd sized array
    :param A: an array of integers with an odd number of elements
    :param N: length of the array
    :return: the one element which does not have a complementary element
    """
    # protect against crazy inputs
    if not isinstance(A, list):
        raise TypeError("Input must be a list of integers")
    if len(A) < 1:
        raise ValueError("Input list must not be empty")
    if len(A) > MAX_LENGTH:
        raise ValueError("Input list must not be longer than %s" % MAX_LENGTH)

    # dictionary of keys in need of a match
    unmatched = dict()

    # for every element
    for element in A:
        # try removing it's match
        try:
            del unmatched[element]
        except KeyError:
            # else add it
            unmatched[element] = True

    # if one unmatched item
    if len(unmatched) == 1:
        return unmatched.keys()[0]
    else:
        raise Exception("Expected one unmatched item, but have this: %s" % unmatched)


def gen_array(L, odd):
    """generate a list of sample data: random integers in pairs
    :param L: the length of the list is double this int
    :param odd: the odd integer out
    """
    arr = []
    for _ in xrange((L-1)/2):
        val = random.randint(1, MAX_LENGTH)
        arr.extend((val, val))
    arr.append(odd)
    random.shuffle(arr)
    return arr


class TestOddOccurencesInArray(unittest.TestCase):
    def test_sample_generation(self):
        print gen_array(5, 1)

    def test_example1(self):
        arr = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, solution(arr))

    def test_simple1(self):
        """simple test n=5"""
        arr = gen_array(5, 4)
        self.assertEqual(4, solution(arr))

    def test_simple2(self):
        """simple test n=11"""
        arr = gen_array(11, 4)
        self.assertEqual(4, solution(arr))

    def test_extreme_single_item(self):
        """list containing one item"""
        self.assertEqual(42, solution([42]))

    def test_small1(self):
        """small random test n=201"""
        arr = gen_array(201, 42)
        self.assertEqual(42, solution(arr))

    def test_small2(self):
        """small random test n=601"""
        arr = gen_array(601, 4242)
        self.assertEqual(4242, solution(arr))

    def test_medium1(self):
        """medium random test n=2001"""
        arr = gen_array(2001, 100)
        self.assertEqual(100, solution(arr))

    def test_medium2(self):
        """medium random test n=100,003"""
        arr = gen_array(100003, 500000)
        self.assertEqual(500000, solution(arr))

    def test_big1(self):
        """big random test n=999,999, multiple repetitions"""
        arr = gen_array(100003, 700)
        self.assertEqual(700, solution(arr))

    def test_big2(self):
        """big random test n=999,999"""
        arr = gen_array(999999, 5000111222)
        self.assertEqual(5000111222, solution(arr))


if __name__ == '__main__':
    unittest.main()

