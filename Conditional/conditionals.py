#Conditionals


#If Condition
# syntax

if condition:
    this part of code runs for truthy conditions

#Example:

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number


#If Else 
# syntax

if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions

#Example:

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#If Elif Else
# syntax

if condition:
    code
elif condition:
    code
else:
    code

#Example:

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Short Hand
# syntax

code if condition else code

#Example:

a = 3
print('A is positive') if a > 0 else print('A is negative') 
# first condition met, 'A is positive' will be printed


#Nested Conditions (Conditions can be nested)

# syntax
if condition:
    code
    if condition:
    code

#Example:

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


#If Condition and Logical Operators
# syntax

if condition and condition:
    code
#Example:

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 != = 0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
  
  
#If and Or Logical Operators
# syntax

if condition or condition:
    code

#Example:

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


  
