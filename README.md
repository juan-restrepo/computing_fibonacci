computing_fibonacci
===================

Python code that when executed computes the requested fibonacci number blazingly fast. For example, it computes the 500000th fibonacci, which has 104494 digits, in 0.090457 seconds.

It uses fast exponentiation to make the time logarithmic instead of linear (or even exponential if Dynamic Programming isn't used), which improves the traditional recursive approach. However, for small indices there are no gains, as the arithmetic is much more involved.
