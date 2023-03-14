
My entry takes 284,000ms (4.8m) for 1000 items.

Estimating for 1,000,000 items:

Putting in some incremental output, I see it taking about a second per rotation.

It should need 499,999,500,000 rotations to finish. That's 15,854 years.

The time it takes to do a rotation should be proportional to the remaining items to sort.

So, they'll average to half a second over the run. 7,927 years to sort 1,000,000 items.

----------

## [Submission Here](https://forms.gle/eFRiWrimKQRLTCyu5)

> or just fork repo

# Slow Sorting Algorithm Challenge:

>The coder must write a sorting algorithm that sorts a list of integers in ascending order.

>The algorithm must be intentionally designed to be as slow as possible without any manual slowdowns of the code. ex: 
> - Adding deliberate wait times or sleep functions to the code.
> - Adding unnecessary loops or iterations to the code.
> - No redundant variables, operations, loops etc.

> The algorithm must not use any built-in sorting functions or libraries.

> The algorithm must not use any external resources or libraries.

> The algorithm must be implemented in a language of the coder's choice.

> The algorithm must be able to handle lists of any length (tho the given inputs are of length 50, 1k, 10k and 1m).

> The algorithm must be deterministic, meaning that given the same input, it should produce the same output every time.

> Time complexity analysis and an explanation of the design choices made to intentionally slow down the algorithm are welcome [(example)](https://github.com/cs-ubbcluj-ro/slow-sort-submission/blob/main/README.md)

> Extra smiles for well-documented [(example)](https://github.com/cs-ubbcluj-ro/slow-sort-submission/blob/main/README.md) and readable code (don't use single letter variable names please)

> The algorithm must be functional and able to correctly sort a list of integers in ascending order.

> The winner will be determined based on the slowest sorting algorithm that still meets all of the above criteria.

# Input format

> ```cpp
> n // size of list
> A1 // list of numbers
> A2
> ...
> An
> ``` 
>
> constraints: 
> -size <= An <= size


## Participation

> - You can implement your algorithm in ```slow_sort.py``` ```slow_sort()``` function
> - You can verify the correctness of your algorithm by running ```verifier.py```
> - You can compare your algorithm to Bubble Sort by running ```compare.py``` (This can take long!)
> - Solutions can be submitted [here](https://forms.gle/eFRiWrimKQRLTCyu5) (or just fork repo)
