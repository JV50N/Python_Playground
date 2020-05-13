# Declaring a Variable
x = 1           # casted as an INT by default
y = 2.5         # casted as a FLOAT by default
name = 'Jason'  # casted as a STR by default
is_cool = True  # casted as a BOOL as default

# Multiple Assignment
x, y, name, is_cool = (1, 2.5, "Jason", True) # This line does the same as above, except more compact

# print -- print()
print('Hello World!')
print(name, x, y, is_cool)

# basic math
a = x + y
print(a)

# check type of VARIABLE -- type()
print(type(x))

# cast a different type to a value
x = str(x) # changes x which is an INT into a STR

# Concatenate a String
print('Hello, my name is ' + name)

# Concatenate an int into a string (not the prefered way)
age = 31
print('And my age is ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F- Strings (python 3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# capitalize String
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
