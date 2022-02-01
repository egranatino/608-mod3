# bonus.py
# using 1000 random rolls (1-100) as list to find population variance and population standard deviation - Emily Granatino

import random

# creating a randomized dataset for average age of death
avgage = [random.randrange(1,101) for roll in range(1000)]
 
import statistics
print(avgage,'The population variance of the 1,000 random ages of death is',statistics.pvariance(avgage))

print(avgage,'The population standard deviation of the 1,000 random ages of death is',statistics.pstdev(avgage))