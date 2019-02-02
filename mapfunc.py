#!/usr/bin/python
"""
map(function_to_apply, list_of_inputs)
Most of the times we want to pass all the list elements to a function one-by-one and
then collect the output. For instance:
"""
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print (squared)

"""
Map allows us to implement this in a much simpler and nicer way. Here you go:
"""
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print (squared)

"""
Most of the times we use lambdas with map so I did the same. Instead of a list of inputs
we can even have a list of functions!

"""
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
funcs = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


"""
filter creates a list of elements for which a function returns
true. Here is a short and concise example:
"""
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# Output: [-5, -4, -3, -2, -1]
#The filter resembles a for loop but it is a builtin function and faster.

"""
Reduce is a really useful function for performing some computation on a list and returning
the result. For example, if you wanted to compute the product of a list of
integers.
"""
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print (product)
