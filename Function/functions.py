#Functions

#A function is a reusable block of code or programming statements designed to perform a certain task.

#Declaring and Calling a Function

# syntax

# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()

#Example:

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

#Function Returning a Value - Part 1

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#Function with Parameters

#Single Parameter: If our function takes a parameter we should call our function with an argument
 
# syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  function_name(parameter)

#Example:

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050

#Two Parameter: A function may or may not have a parameter or parameters. A function may have two or more parameters. If our function takes parameters we should call it with arguments. Let's check a function with two parameters:
  
# syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(arg1, arg2)

#Example:

def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2019, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

#Passing Arguments with Key and Value

# syntax

# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
function_name(para1='John', para2='Doe') # the order of arguments does not matter here

#Example:

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname='Asabeneh', lastname='Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2=3, num1=2) # Order does not matter

#Function Returning a Value - Part 2

#Returning a string: 

#Example:

def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

#Returning a number:

#Example:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))

#Returning a boolean: 

#Example:

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

#Returning a list:

#Example:

def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

#Function with Default Parameters

# syntax

# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)

#Example:

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2019):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1819))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

#Arbitrary Number of Arguments

# syntax

# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)

#Example:

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5))

#Default and Arbitrary Number of Parameters in Functions

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

#Function as a Parameter of Another Function

def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))





