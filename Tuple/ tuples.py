#creating tuple 
my_tup = ('test',)

#slicing the tuple
my_tup = ('Python', 'Julia', 1, 3.1415)
print(my_tup[:-3])
# -ve sign indicates -ve indexing. So start from right and skip 2 elements
print(my_tup[::-2])


#Concatenation, Repetition and Membership in Tuple 

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b' , 'c' ,'d' , 'e')
# Tuple Concatentation
tuple1 + tuple2

# Tuple Repetition
tuple1 * 2

# Membership operator, returns true if member of tuple
'a' in tuple2

#Nested Tuple 

list1 = ['Python', 'Julia', 1, 3.1415]
# List of tuples is possible too!
list2 = [('a', 'b'), ('c', 'd')]
tuple1 = (1, 2, 3, 4, 5)
# Concatenating the list and converting to tuple. 
# Then adding two tuples and storing it in another tuple
tuple2 = tuple(list1 + list2)+ tuple1
tuple2

Built-in Tuple Functions and Methods

tuple1.count(3)      #tuple.count()

tuple1.index(3)      #tuple.index()