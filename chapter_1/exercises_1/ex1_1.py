'''
Suppose you have a sorted list of 128 names, and you’re searching 
through it using binary search. What’s the maximum number of 
steps it would take?
'''

# How many 2s do we multiply together to get 128? Just use logarithm 
# log_2 128 = 7

import math
print(math.log(128, 2))