import os
from os.path import join
import pandas as pd
import numpy as np

X = np.arange(1,11,1)
print("X:", X)
data = {'X': X}
df = pd.DataFrame(data)
print(df.head())

# Python Debugger example
def add(a, b):
	return a + b
add(1,2)
import pdb
# Basic commands: n = next line, p = print
# pdb.set_trace()
# add(1, 'err')


# List comprehension 
fruits = [
	{'name': 'apple', 'price': 20},
	{'name': 'orange', 'price': 15}, 
	{'name': 'lemon', 'price': 12}
]

print(fruits)
# Print list names
print("\nList names:")
print([fruit['name'] for fruit in fruits])

# Filter with conditional
print("\nList filetring:")
print([fruit['name'] for fruit in fruits if fruit['name'][0] == 'l'])

# Dicts comprehension
print("\nDict entries:")
print(
	{fruit['name']: fruit['price'] for fruit in fruits}
	)

# Lamda nethod
print("\nlambda method:")
l_add = lambda x, y: x + y

print("add(1, 2):", add(1, 2))
print("l_add(1, 2):", l_add(1, 2))

nums = [1, 3, 5, 7]
higher_than_one = filter(lambda x: x > 1, nums)
print("\nLamda filter:", list(higher_than_one))