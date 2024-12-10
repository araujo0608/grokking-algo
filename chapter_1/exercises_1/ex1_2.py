'''
Suppose you double the size of the list. What’s the maximum 
number of steps now?
'''

# How many 2s do we multiply together to get 128*2? Just use logarithm 
# log_2 256 = 8

import math
print(math.log(256, 2))