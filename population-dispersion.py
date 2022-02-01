# population-dispersion.py
# Emily Granatino use the statistics module to calculate measures of disperson for population using 10 6-sided dice rolls (given)


import random

rolllist = [1,3,4,2,6,5,3,4,5,2]
 
import statistics
print('The population variance of the roll list',rolllist, 'is',statistics.pvariance(rolllist))

print('The population standard deviation of the roll list',rolllist, 'is',statistics.pstdev(rolllist))


# using 10 6-sided dice rolls as list to find population variance and population standard deviation

import random

roll_list = [random.randrange(1,7) for roll in range(10)]
 
import statistics
print('The population variance of the roll list',roll_list, 'is',statistics.pvariance(roll_list))

print('The population standard deviation of the roll list',roll_list, 'is',statistics.pstdev(roll_list))
