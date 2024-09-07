""" Understanding Quick Sort """

import timeit
from memory_profiler import profile

def partition(array, first, last):
    """ Split the array into 2 parts """

    pivot = array[last]
    low_index = first - 1

    for index in range(first, last):
        if array[index] < pivot:
            low_index += 1
            array[low_index], array[index] = array[index], array[low_index]

    array[low_index + 1], array[last] = array[last], array[low_index + 1]

    return (low_index + 1)

# @profile
def quick_sort(array, first, last):
    if first < last:
        partition_index = partition(array, first, last)

        quick_sort(array, first, partition_index - 1)
        quick_sort(array, partition_index + 1, last)

def print_execution_times(array_name):
    """ Function to print execution times """

    timer_stmt = '''quick_sort({0}, 0, len({0}) - 1)'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name), repeat=5, number=10000, globals=globals())
    print('Quick sort time for array: ' + str(min(times)))

# Testing performance of algorithms on these arrays
randomized_array = [23, 65, 98, 1, 36, 47, 76, 28, 83, 15]
sorted_array = [1, 15, 23, 28, 36, 47, 65, 76, 83, 98]
reversed_sorted_array = [98, 83, 76, 65, 47, 36, 28, 23, 15, 1]

print_execution_times(randomized_array)
print_execution_times(sorted_array)
print_execution_times(reversed_sorted_array)
