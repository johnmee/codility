# Codility Solutions

Python solutions to the training exercises and tests at http://codility.com/

https://codility.com/programmers/lessons/

## Test cases

The test cases follow a predictable methodology :

* The examples provided in the problem description are explicitly tested.

### Correctness tests
* An empty or zero test case is tested - the result is often not explicitly described, but will actually be there implicitly.
* A minimum test case - using just one input, or whatever is the absolute minimal conceiveable input.
* A simple, or 'small' test case or two - just some basic, as you might reasonably anticipate, examples.
* Edge cases - test cases written to root out those awkward -off-by-one- scenarios that inevitably suck up 80% of the time required to devise a solution.

### Performance tests

* Not always, as the problem dictates, some medium sized test cases eg: ~100 - ~5000 length arrays.
* Always some 'extreme' test cases typically involving generating maximal random datasets.
* Worst case scenario is tested - the biggest possible numbers in the biggest resultsets - with the intent to test the speed and space restraints.

## Notes

* You are safe to assume they won't test, mark you down for, failing to guard against the explicit assumptions described. 
  * So if it says N is 0..1000, they won't feed in an N=1001 just to see if you protected against it.
* The "Open reading material", at the top of each lesson, is worth reading before attempting the exercises as they are 
 short and focus exactly on what you'll need to solve the following puzzles.
* During the actual interview testing/exam:
  * The report sent to the company is much more detailed than the one sent to the candidate: every edit and run
    is recorded and presented to the company (if you use the browser to build your solution).
  * If you are given multiple tasks, you are permitted to read them, and commence them, and submit them in any order.
  * Before submitting your solution, there is no feedback regarding it's efficiency; but it does affect your score, and report!

* The python `in` operator is a list loop and could contribute an O(N) all on it's own. ie:
    * `foo in bar` is cheap if bar is a dictionary but potentially expensive if bar is a list.
    * `foo in bar.keys()` is a nested loop—sequentially visiting every item in the list of keys.
* Coming up with reasonable test cases, and determining the correct answers, is half the puzzle! 
  * Passing the examples given is not enough. Every puzzle is subjected to:
    * 'simple' tests, not unlike the ones provided, and 
    * 'medium' tests, which involve arrays/values of more significant size/length, and 
    * 'maximal' tests which present inputs of the maximum size and complexity. 
  * To be certain of 100%, it is wise to devise tests, and the correct answers, for these.

* O factors are no longer provided in the descriptions, but still useful to understand and keep in mind...  

  Understanding the O factors reveals the nature of the optimal solution:
   * O(1) there is a formulaic solution 
   * O(n) the solution has no nested loops and all happens in a single pass
   * O(n+m) the solution has no nested loops, and passes over n and m only once
   * O(n+n) the solution has no nested loops, but you can pass over the sequence twice
   * O(n*log(n)) the solution has a loop through n and a nested loop which does not always visit every possible n
   * O(n*n) the solution has a loop through n nested inside a loop through n
* Codility does update the python version occasionally, and I always mirror the current
  version.  So puzzles solved in 2018 used Python 3.7.13. In 2023 we are on 3.8.10 or 3.10.x.
  It's not really relevant, because all the puzzles are intended for solving in a lot of
  different languages and tend to only use integers and simple for loops; none of them
  rely on specific language features, although sometimes you may encounter quirks
  which impact the performance.
* This next complaint appears to be fixed now, as Codility rewrote the description:

  If there seems to be a lack of clarity in a puzzle regarding the correct response to error conditions: 
  look, read, and look again because, after seeing the solution, that apparent lack will become a (debatably) 
  reasonable assumption implied in the specs.
  For example in "MissingInteger" (Lesson 4):
    * What is the correct response if there are no positive integers, say, [-1,-2,-3]?
      * The words do mention returning the 'minimal positive integer', which is '1', so that answer is '1'.
    * What if the input set is _full_ (no integers are missing)?
      * The 'minimal positive integer that does not occur in A' is what it says, so the answer is 'the largest value 
      in the array—plus one'.
      * Whilst not explicitly stated, the answer is specified but implicitly–so be prepared for some uncertainty with
      some outputs; don't let it undermine your time and confidence in the moment.

## How to approach coding challenges

* Read the puzzle over and over; soak up all the reading material
* Focus on the inputs and the outputs of the routine
* Ignore the edge cases (to start)
* Work through the most basic examples on paper before you code:
  * the single input base case... 
  * the two input simple case... 
  * in a different order... 
  * now three... etc.
* Break it down to the pieces 
* Think through all the tactics you know (stacks, prefix sums, sorts, slices) and see if they can help
* Build up a model solution, on paper, to where you have an idea how to solve it
* Draw a flowchart diagram
* Tough call to decide whether to go for the brute force solution first then optimize, or hope to save-not waste-time, 
  by going directly for the optimal solution.
* Now, code and test the most basic example: one/most simple/minimal input case
* Then, gradually less simple examples: if you get confused, go back to the paper
* Finally, work in the edge cases


## Tactics & Tricks

Prime and Factors of numbers
: Find factors of numbers, and primes.

* If you have the product, you only need find one factor to determine the other.
* You only need to search 1..sqrt() of possible numbers to find one factor.

Euclidean Algorithm
: The greatest common divisor of two positive integers

* A recursive algorithm to quickly find the greatest common denominator.
