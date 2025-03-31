"""
This Python file contains solutions for various list-related problems.
Each solution is structured with proper comments and follows code hygiene.
"""

# Task 1: Separate even and odd numbers from a given list
def separate_even_odd(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    odd_numbers = [num for num in lst if num % 2 != 0]
    return even_numbers, odd_numbers

# Task 2: Count prime numbers and create a list of primes
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(lst):
    primes = [num for num in lst if is_prime(num)]
    return len(primes), primes

# Task 3: Count happy numbers in a list
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def count_happy_numbers(lst):
    return sum(1 for num in lst if is_happy(num))

# Task 4: Sum of first and last digit of an integer
def sum_first_last(n):
    num_str = str(abs(n))
    return int(num_str[0]) + int(num_str[-1])

# Task 5: Distribute mangoes to students with minimal difference
def distribute_mangoes(bags, students):
    bags.sort()
    min_diff = float('inf')
    for i in range(len(bags) - students + 1):
        min_diff = min(min_diff, bags[i + students - 1] - bags[i])
    return min_diff

# Task 6: Find duplicates in three lists
def find_duplicates(list1, list2, list3):
    return list(set(list1) & set(list2) & set(list3))

# Task 7: Find the first non-repeating element
def first_non_repeating(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    for num in lst:
        if count[num] == 1:
            return num
    return None

# Task 8: Find minimum element in a rotated and sorted list
def find_min_rotated(lst):
    return min(lst)

# Task 9: Find triplet whose sum is a given value
def find_triplet(lst, target):
    lst.sort()
    for i in range(len(lst) - 2):
        left, right = i + 1, len(lst) - 1
        while left < right:
            curr_sum = lst[i] + lst[left] + lst[right]
            if curr_sum == target:
                return lst[i], lst[left], lst[right]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return None

# Task 10: Check if a sublist has a sum of zero
def has_zero_sum_sublist(lst):
    seen = set()
    sum_so_far = 0
    for num in lst:
        sum_so_far += num
        if sum_so_far == 0 or sum_so_far in seen:
            return True
        seen.add(sum_so_far)
    return False

# Example usage
if __name__ == "__main__":
    numbers = [10, 501, 22, 37, 100, 999, 87, 351]
    print("Even & Odd Numbers:", separate_even_odd(numbers))
    print("Prime Count & List:", get_primes(numbers))
    print("Happy Numbers Count:", count_happy_numbers(numbers))
    print("Sum of First & Last Digit:", sum_first_last(1234))
    print("Minimum Difference in Mango Bags:", distribute_mangoes([10, 20, 30, 40, 50], 3))
    print("Duplicates in Three Lists:", find_duplicates([1, 2, 3], [2, 3, 4], [3, 4, 5]))
    print("First Non-Repeating Element:", first_non_repeating([4, 5, 4, 5, 3]))
    print("Minimum Element in Rotated Sorted List:", find_min_rotated([4, 5, 6, 7, 0, 1, 2]))
    print("Triplet Sum:", find_triplet([10, 20, 30, 9], 59))
    print("Sublist with Zero Sum Exists:", has_zero_sum_sublist([4, 2, -3, 1, 6]))
