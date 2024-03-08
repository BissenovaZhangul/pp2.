#1
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7))) 


#2
def count_upper_lower_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1 
    return upper_count, lower_count
input_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower_letters(input_string)
print('Number of uppercase letters:', upper_count)
print('Number of lowercase letters:', lower_count)


#3
string_to_check = input("Enter a string")
if string_to_check == string_to_check[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")


#4
import math
def sqrt(x,y):
    print(f"Square root of {x} after {y} milisesonds is" , math.sqrt(x))
    
x = int(input())
y = int(input())
sqrt(x,y)

#5
def check_all_true(input_tuple):
    return all(input_tuple)
test_tuple1 = (True, True, True)
test_tuple2 = (True, False, True)
print(check_all_true(test_tuple1))  
print(check_all_true(test_tuple2))