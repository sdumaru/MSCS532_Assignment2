""" Understanding Merge Sort """

import timeit
import random
from memory_profiler import profile

# @profile
def merge(array, first, mid, last):
    """ Will merge the array by splitting them into 2 temporary arrays in the middle and comparing 
        them 1 element at a time and store the smallest one in the array """
    first_array_length = mid - first + 1                # Size for first temporary array
    second_array_length = last - mid                    # Size for second temporary array

    left_side = [0] * first_array_length                # Temporary First array that will store the left elements from mid
    right_side = [0] * second_array_length              # Temporary Second array that will store the right elements from mid

    for index in range(0, first_array_length):          # Copy first halves elements from the array to temp (left_side) array
        left_side[index] = array[first + index]
    for index in range(0, second_array_length):         # Copy second halves elements from the array to temp (right_side) array
        right_side[index] = array[mid + 1 + index]

    i = 0                                               # Initial index for first sub array (left_side)
    j = 0                                               # Initial index for second sub array (right_side)
    k = first                                           # Initial index for merged sorted array (array)

    # Compare the elements from 2 sub arrays from beginning till the end of either arrays
    # and store the smallest element in the merged array.
    while (i < first_array_length) and (j < second_array_length):
        if left_side[i] <= right_side[j]:
            array[k] = left_side[i]
            i += 1
        else:
            array[k] = right_side[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_side array if remaining
    while i < first_array_length:
        array[k] = left_side[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_side array if remaining
    while j < second_array_length:
        array[k] = right_side[j]
        j += 1
        k += 1

# @profile
def merge_sort(array, left, right):
    """ Function that will take array, leftmost index and rightmost index of array 
        as an input and return sorted array """
    if left < right:
        mid = (left + right) // 2

        # Divide-and-Conquer method
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

    return array

def print_execution_times(array_name):
    """ Function to print execution times """
    timer_stmt = '''merge_sort({0}, 0, len({0}) - 1)'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name), repeat=5, number=10000, globals=globals())
    print('Total execution time: ' + str(min(times)))

def huge_random_array():
    """ Function to return huge number of random integers for testing purpose """
    array = []
    max_numbers = 500
    for i in range(max_numbers):
        array.append(random.randint(0, max_numbers))
    return array

# Testing performance of algorithms on these arrays
randomized_array = [23, 65, 98, 1, 36, 47, 76, 28, 83, 15]
sorted_array = [1, 15, 23, 28, 36, 47, 65, 76, 83, 98]
reversed_sorted_array = [98, 83, 76, 65, 47, 36, 28, 23, 15, 1]

# Print execution times for the array
print_execution_times(randomized_array)
print_execution_times(sorted_array)
print_execution_times(reversed_sorted_array)
print_execution_times(huge_random_array())
