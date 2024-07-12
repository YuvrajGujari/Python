#Loops

#While Loop

  # syntax
while condition:
    code goes here
  
#Example:

count = 0
while count < 5:
    print(count)
    count = count + 1

# syntax
while condition:
    code goes here
else:
    code goes here
  
#Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


#Break and Continue - Part 1

# syntax
while condition:
    code goes here
    if another_condition:
        break
#Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# syntax

while condition:
    code goes here
    if another_condition:
        continue
#Example:

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1


#For Loop

#For loop with list

# syntax
for iterator in lst:
    code goes here

#Example:

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

#For loop with string

# syntax
for iterator in string:
    code goes here

#Example:

language = 'Python'
for letter in language:
    print(letter)

#For loop with tuple

# syntax
for iterator in tpl:
    code goes here

#Example:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

#For loop with dictionary 

# syntax
for iterator in dct:
    code goes here

#Example:

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

#Loops in set

# syntax
for iterator in st:
    code goes here

#Example:

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


#Break and Continue - Part 2

#Break: We use break when we like to stop our loop before it is completed.

# syntax
for iterator in sequence:
    code goes here
    if condition:
        break

#Example:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

#Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

# syntax
for iterator in sequence:
    code goes here
    if condition:
        continue

#Example:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


#Range Function 


lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# syntax
for iterator in range(start, end, increment):

#Example:

for number in range(11):
    print(number)   # prints 0 to 10, not including 11


#Nested For Loop

# syntax
for x in y:
    for t in s:
        print(t)

#Example:

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#For Else

#If we want to execute some message when the loop ends, we use else.

# syntax
for iterator in range(start, end, increment):
    do something
else:
    print('The loop ended')

#Example:

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


#Pass

#In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.

Example:

for number in range(6):
    pass

