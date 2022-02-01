# built-in-min-max.py
# Emily Granatino - this defines the maximum and minimum function and uses it

# creating maximum funcition
def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
            max_value = value2
    if value3 > max_value:
            max_value = value3
    return max_value

print('The max of 12, 27, 36 is',maximum(12,27,36))
print('The max of 12.3, 45.6, 9.7 is',maximum(12.3,45.6,9.7))
print('The max of yellow, red, orange is',maximum('yellow','red','orange'))
        
# creating minimum funcition
def minimum(value1, value2, value3, value4):
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value:
            min_value = value2
    if value3 < min_value:
            min_value = value3
    if value4 < min_value:
            min_value = value4
    return min_value

print('The min of 15,9,27,14 is',minimum(15,9,27,14))

# use built in functions to confirm
print('Using the built in min/max functions:')
print('The max of 12, 27, 36 is',max(12,27,36))
print('The max of 12.3, 45.6, 9.7 is',max(12.3,45.6,9.7))
print('The max of yellow, red, orange is',max('yellow','red','orange'))       
print('The min of 15,9,27,14 is',min(15,9,27,14))
 
          