#~ Comments
print("#~ Comments")
print("\n")
# Single line comments start with a '#'

"""
	Multiline strings can be written using three "s, and are often used
	as fuction and module comments
"""




#~ Variables
print("#~ Variables")
print("\n")

x = 2
y = x * 7
print(y) # => 14

x = "Hello, I'm "
y = x + "Python!"
print(y) # => Hello, I'm Python!
print("\n")



#~ Where's my Type?
print("#~ Where's my Type?")
print("\n")
"""
	Variables in Python are dynamically-typed: declared without an 
	type. However, objects have a type, so Python knows the type of a
	variable, even if you don't.
"""
print(type(1)) # => <class 'int'>
print(type("Hello")) # => <class 'str'>
print(type(None)) # => <class 'NoneType'>

print(type(int)) # => <class 'type'>
print(type(type(int))) # => <class 'type'>
print("\n")



#~ Numbers and Math
print("#~ Numbers and Math")
print("\n")
"""
	Python has two numeric types, int and float 
"""

print(type(3)) # => 3 (int)
print(type(3.0)) # => 3.0 (float)
print("\n")

print("7 / 3 = {}".format(7/3))
print("7.0 / 3.0 = {}".format(7.0/3.0))
print("\n")



#~ Booleans
print("#~ Booleans")
print("\n")
"""
	bool is a subtype of int, where True == 1 and False == 0
"""

print(not True) # => False
print(not 1 > 2) # => True
print(1 < 2 >= 3) # => False
print(True or False) # => True
print(1 == 1)
print("\n")



#~ Strings
print("#~ Strings")
print("\n")
"""
	No char in Python!
	Both ' and " create string literals
"""

greeting = 'Hello'
group = "wørld" # Unicode by default

print(greeting + ' ' + group + '!') # => 'Hello wørld!'
print("\n")



#~ Indexing
print("#~ Indexing")
print("\n")
"""
	Indexing starts from 0
"""

s='Arthur'
print(s[0]) # => 'A'
""" print(s[7]) # => IndexError: string index out of range """
print("\n")

for i in range(0,6):
	print(s[i])

print("\n")



#~ Negative Indexing
print("#~ Negative Indexing")
print("\n")
"""
	Negative indexing has -1 starting from the end
"""

s='Arthur'
print(s[-1]) # => 'r'
print("\n")

for i in range(-6, 0):
	print(s[i])

print("\n")

""" Spelling backwards with negative indexing """
for i in range(-5, 1):
	print(s[-i])

print("\n")



#~ Slicing
print("#~ Slicing")
print("\n")

s='Arthur'
print(s[0:2]) # => 'Ar'
print(s[3:6]) # => 'hur'
print(s[1:4]) # => 'rth'
print("\n")

print(s[:2]) # => 'Ar'  """ implicitly starts at 0 """
print(s[3:]) # => 'hur'  """ implicitly ends at end """
print("\n")

""" Can also pass a step size """
s='Arthur'
print(s[::2])
print(s[1:6:2]) # => 'rhr' (go from 1 to 6 picking every 2 char)
print(s[4::-2]) # => 'utA'
print("\n")

""" Reversing a string (proper version, not with for loop..) """
print(s[::-1]) # => 'ruhtrA'
print("\n")



#~ Converting Values
print("#~ Converting Values")
print("\n")

x = 45
print(x)
print(type(x))
y = str(x) # => "45"
print(y)
print(type(y))

""" Other converting functions """
int("42") # => 42
float("2.5") # => 2.5
float("1") # => 1.0

