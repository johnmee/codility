# Codility Solutions

Solutions to the exercises and tests at http://codility.com/

https://codility.com/programmers/lessons/

## Test cases

So far, their test cases follow a predictable methodology :

* the examples provided are explicitly tested
* an empty or zero test case is devised and tested - the expected result is often not explicit or obvious, but will actually be there implicitly, such that you may not realise it is indeed specified until you work out what the answer should be.
* a minimal test case - using just one input, or whatever is the absolute minimal conceiveable input - again, probably not explicitly described, but there implicitly nonetheless
* edge cases - test cases written to root out those awkward -off-by-one- scenarios that inevitably suck up 80% of the time required to devise a solution
* a simple, or 'small' test case or two - just some basic, as you might reasonably anticipate, examples
* not always, as the problem dictates, some medium sized test cases
* always some large test cases which attempt to stress the algorithm
* worst case scenario is tested - the biggest numbers in the biggest resultset will be tested - with the intent to test the speed and space restraints

## Other notes

* you're pretty safe to assume they won't test, mark you down for, failing to guard against the explicit assumptions described. So if it says N is 0..1000, they won't feed in an N=1001 just to see if you protected against it.
* the "Open reading material", currently at the top of each lesson, is worth reading before attempting the exercises as they are short and focus exactly on what you'll need to solve the following puzzles
* during the actual interview testing/exam, the report sent to the candidate is much more sparesly detailed than the one sent to the company?!
* if you use the IDE provided in the browser to actually build your solution - your every edit and run is recorded and presented to the client
