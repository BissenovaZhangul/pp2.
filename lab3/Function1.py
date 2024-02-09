#1
def grams_to_ounces(x):
	return 28.3495231 * x
grams = 10
ounces = grams_to_ounces(grams)
print (ounces)


#2
def fahrenheit_to_centigrade(f):
    return (5/9) * (f - 32)
f = 95
c = fahrenheit_to_centigrade(f)
print ((f, c))


#3
def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        totallegs = (numchickens * 2) + (numrabbits * 4)
        if totallegs == numlegs:
            return numchickens, numrabbits
    return "No solution found"
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"Number of chickens: {result[0]}, Number of rabbits: {result[1]}")


#4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_prime(numbers)
print(filtered_numbers)


#5
from itertools import permutations
def print_permutations(string):
    permutations_list = list(permutations(string))
    for permutation in permutations_list:
        print(''.join(permutation))
user_input = input("Enter a string: ")
print_permutations(user_input)


#6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Reversed sentence:", reversed_sentence)


#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))  


#8
def spy_game(nums):
    flag = [0, 0, 7]
    for num in nums:
        if num == flag[0]:
            flag.pop(0)
        if not flag:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0])) 


#9
def calculate_sphere_volume(radius):
    pi=3.14
    volume = (4/3) * pi * (radius ** 3)
    return volume
radius = 5
volume = calculate_sphere_volume(radius)
print("The volume of the sphere is:", volume)


#10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
my_list = [1, 2, 3, 3, 4, 4, 5]
result = unique_elements(my_list)
print(result)


#11
def is_palindrome(word):
    word = word.lower().replace(" ", "") 
    reversed_word = word[::-1]  
    return word == reversed_word
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")


#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])


#13
import random
def guess_the_number(name):
    secret_number = random.randint(1, 20)
    cnt=0
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess :) ")
    while True:
        guess=int(input())
        cnt+=1
        if guess == secret_number:
            print("Good job, " + name + "! You guessed my number in 3 guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again")
        else:
            print("Your guess is too high. Try again")
name=input("Hello, what is your name?")
guess_the_number(name)


#14
def histogram(numbers):
    for num in numbers:
        print('*' * num)
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    if word == word[::-1]:
        return True
    else:
        return False
print("Palindrome check for 'madam':", is_palindrome("madam"))
histogram([4, 9, 7])






