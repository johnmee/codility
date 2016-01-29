# Codility Solutions

Solutions to the exercises and tests at http://codility.com/

https://codility.com/programmers/lessons/

## Test cases

So far, their test cases follow a predictable methodology :

* the examples provided are explicitly tested

### Correctness tests
* an empty or zero test case is devised and tested - the expected result is often not explicit or obvious, but will actually be there implicitly, such that you may not realise it is indeed specified until you work out what the answer should be.
* a minimal test case - using just one input, or whatever is the absolute minimal conceiveable input - again, probably not explicitly described, but there implicitly nonetheless
* edge cases - test cases written to root out those awkward -off-by-one- scenarios that inevitably suck up 80% of the time required to devise a solution
* a simple, or 'small' test case or two - just some basic, as you might reasonably anticipate, examples

### Performance tests

* worst case scenario is tested - the biggest possible numbers in the biggest resultsets - with the intent to test the speed and space restraints
* not always, as the problem dictates, some medium sized test cases eg: ~100 - ~5000 length arrays
* always some 'extreme' test cases typically involving generating maximal random datasets

## Other notes

* you're safe to assume they won't test, mark you down for, failing to guard against the explicit assumptions described. So if it says N is 0..1000, they won't feed in an N=1001 just to see if you protected against it.
* the "Open reading material", currently at the top of each lesson, is worth reading before attempting the exercises as they are short and focus exactly on what you'll need to solve the following puzzles
* during the actual interview testing/exam, the report sent to the candidate is much more sparesly detailed than the one sent to the company?!
* if you use the browser to actually build your solution - every edit and run is recorded and presented to the client
* if you are given multiple tasks, you are permitted to read them, and commence them, and submit them in any order.
* if there seems to be a lack of specificity in every puzzle around what is the correct response to error conditions; look, read, look again, as
   after seeing the solution that apparent lack always seems like a debateably reasonable assumption implied by the specs.
   For example:
    * "MissingInteger" (Lesson 4) does not specify the correct response if the input sequence is [-1,-2,-3]:
   there are no positive integers so what is the correct response? The 'minimal positive integer' is 1.
    * Similarly, it does not explicitly state that if the input set is _full_ (no integers are missing) then return 
   the largest value—plus one.  Again, seems perfectly reasonable in hindsight, but a source of uncertainty in the moment
* before submitting your solution, there is no feedback regarding it's efficiency; but it does affect your score and report
* if it tells you the solution is O(1) you know to go looking for a formulaic solution; O(n) has no loops inside loops, etc.
* the python `in` operator is a list loop and could contribute an O(N) all on it's own
    * `foo in bar` is fine
    * `foo in bar.keys()` impacts your time complexity
