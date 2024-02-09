#1
class StringInput:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Enter a string: ")
    def printString(self):
        print(self.string.upper())


#2
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length*self.length
aSquare= Square(5)
print (aSquare.area())


#3
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def area(self):
        return self.length*self.width
aRectangle = Rectangle(3,8)
print (aRectangle.area())


#4
def show(self):
    print(f"Coordinates: ({self.x}, {self.y})")
def move(self, new_x, new_y):
    self.x = new_x
    self.y = new_y
def dist(self, other_point):
    distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    return distance


#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdrawal amount exceeds available balance.")
account = Account("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500) 
print("Account balance:", account.balance)


#6
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)


