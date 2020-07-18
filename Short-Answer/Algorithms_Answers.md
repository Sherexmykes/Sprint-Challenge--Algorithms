#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
# The runtime is O(1+n*1) == O(n)
# O(n). I would say that it is O(n) because as n increases, the number of operations scales linearly. If n = 2, the while loop will run 2 times. If n = 5, the while loop will run 5 times, and so on.


b) 
# The run time is O(1+n*(1+log(n)*(1+1))) == O(nlog(n))
# while j < n has O(log n) complexity because the control variable j is alway multiplied by 2

# So ....O(1+n*(1+log(n)*(1+1))) == O(nlog(n))

c) 
# The run time is O(1+1+n) == O(n)
# I think that the the function will recurse n times until n=0.

## Exercise II

# Base case:
# Go to the ground  floor
# Find the middle floor between the start point and the top floor (n)
# run until floor f:
# drop the egg
# if the egg breaks:
# move to the middle point between current location and the ground
# otherwise:
 # move to the middle point between current location and the top floor
# return floor f
# floor f is the highest floor where the egg doesn't break
# Binary search so runtime complerxity I beleive would be O(n)