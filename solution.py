"""
Challenge: given an array of integer and a target,
return index of a pair where the sum of this pais is equalts to target.

Return when first pairs was found.
"""

import time
import random


def generate_list(list_size):
    list_numbers = []
    for i in range(list_size):
        list_numbers.append(random.randint(1, 30))
    return list_numbers


# Brute Force Solution
# Complexity = O(n^2)
def two_number_sum_brute_force(list_numbers, target):
    for i in range(len(list_numbers) - 1):
        for j in range(i + 1, len(list_numbers)):
            if list_numbers[i] + list_numbers[j] == target:
                return (i, j)


# Sorted solution
# Complexity = O(n log n) * n
def two_number_sum_order(list_numbers, target):
    list_numbers_sorted = sorted(list_numbers)
    last_index = len(list_numbers_sorted) - 1
    for i in range(len(list_numbers_sorted)):
        sum = list_numbers_sorted[i] + list_numbers_sorted[last_index]
        if sum == target:
            return (i, last_index)
        elif sum > target:
            last_index -= 1


# Using the completemnt
# Complexity: O(n)
def two_number_sum_n(list_numbers, target):
    map = {}
    for i in range(len(list_numbers)):
        comp = target - list_numbers[i]

        if comp in map:
            return (i, map[comp])

        map[list_numbers[i]] = i


if __name__ == "__main__":
    target = 30
    list_size = 100000
    list_numbers = generate_list(list_size)

    start = time.time()
    print(two_number_sum_brute_force(list_numbers, target))
    end = time.time()
    print(end - start)

    start = time.time()
    print(two_number_sum_order(list_numbers, target))
    end = time.time()
    print(end - start)

    start = time.time()
    print(two_number_sum_n(list_numbers, target))
    end = time.time()
    print(end - start)
