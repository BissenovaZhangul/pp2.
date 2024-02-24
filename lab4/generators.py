#1
def generate_squares(N):
    for i in range(1, N+1):
        yield i * i
N = 6
squares_generator = generate_squares(N)
for i in squares_generator:
    print(i)

#2
def generate_evenNum(N):
    for i in range(0, N+1, 2):
        yield i 
N = 5
EvenNum_generator = generate_evenNum(N)
for i in EvenNum_generator:
    print(i)   

#3
def generate_divisible_by_3_and_4(N):
    for i in range(0, N+1):
        if i%3==0 and i%4==0:
            yield i 
N = 24
numbers_generator = generate_divisible_by_3_and_4(N)
for i in numbers_generator:
    print(i) 
    
#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = 3
b = 7
squares_generator = squares(a, b)
for square in squares_generator:
    print(square)

#5
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for num in countdown_generator(n):
    print(num)