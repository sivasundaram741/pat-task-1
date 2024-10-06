#1
numbers=[10,501,22,37,100,999,87,351]
even_numbers=[num for num in numbers if num%2==0]
odd_numbers=[num for num in numbers if num%2!=0]
print("even",even_numbers)
print("odd",odd_numbers)
#2
numbers=[10,501,22,37,100,999,87,351]
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
prime_numbers=[num for num in numbers if is_prime(num)]
prime_count=len(prime_numbers)
print("prime numbers:",prime_numbers)
print("count of prime numbers:",prime_count)
#3
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in numbers if is_happy_number(num)]

print("Happy numbers in the list:", happy_numbers)
#4
def sum_first_last_digit(n):
    num_str = str(n)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit+last_digit
number =12345
result = sum_first_last_digit(number)
print(f"The sum of the first and last digit of {number} is {result}")
#5
def min_difference(mangoes, m):
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - m + 1):
        current_diff = mangoes[i + m - 1] - mangoes[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff
mangoes = [10, 501, 22, 37, 100, 999, 87, 351]
m = 3
result = min_difference(mangoes, m)
print(f"The minimum difference between the maximum and minimum number of mangoes in any subset of {m} bags is {result}")
#6
def find_duplicates(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = set1 & set2 & set3
    return list(common_elements)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 8, 9, 10, 4]

duplicates = find_duplicates(list1, list2, list3)
print(f"Duplicates in the three lists are: {duplicates}")
#7
def first_non_repeating_element(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    

    for num in lst:
        if count_dict[num] == 1:
            return num
        
    return None 
numbers = [4, 5, 1, 2, 0, 4, 1, 2]
result = first_non_repeating_element(numbers)
if result is not None:
    print(f"The first non-repeating element is {result}")
else:
    print("There is no non-repeating element in the list")
#8
def find_minimum(sorted_list):
    
    return sorted_list[0]


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minimum_element = find_minimum(sorted_list)
print(f"The minimum element in the sorted list is {minimum_element}")
#9
def find_triplet_with_sum(lst, target_sum):

    lst.sort()
    n = len(lst)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            
            if current_sum == target_sum:
                return (lst[i], lst[left], lst[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    
    return None

numbers = [10, 20, 30, 9]
target_sum = 59
result = find_triplet_with_sum(numbers, target_sum)

if result:
    print(f"Triplet found: {result}")
else:
    print("No triplet found with the given sum")
#10
def has_zero_sum_sublist(lst):
    
    cumulative_sum_set = set()
    cumulative_sum = 0
    
    for num in lst:
        cumulative_sum += num
        
        
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True
        
        
        cumulative_sum_set.add(cumulative_sum)
    
    return False


numbers = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(numbers)

if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
