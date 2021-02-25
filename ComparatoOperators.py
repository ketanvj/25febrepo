# allow us to know if two items are equivalent, or if one is great than the other.
a=10
b =15
b=10
print(a is b)
# The Greater Than and Less Than Operators. These comparison operators always return a boolean value.

print(1 < 2) # True
print(2 > 1) # True
print(2 < 1) # False
print(1 <= 1) # True
print(2.0 >= 3) # False

# We can compare numeric types to one other,
# so we can compare floats with integers.


# strings can also work with these comparison operators:

print('a' > 'b') # False
print('b' > 'a') # True
print('bb' >= 'ba') # True
print('a' <= 'c') # True

# When comparing strings, each character is compared with the character at the same index in the other string
# to determine which one is larger.
# Behind the scenes, each character as a numeric value that we can find using the [ord] function,
# and these are used to do the comparisons.

# Once again, if we try to compare types that aren't comparable,
# then we'll receive an error indicating such:
#
# print('a' <= 1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<=' not supported between instances of 'str' and 'int'

# The Equals Operators
# use a double equals sign ==:

print(1 == 1) # True
print(1.0 == 1) # True
print(2 == 1.0) # False
print('a' == 2) # False
print('a' == 'a') # True

# this checks equivalence, so comparing an equivalent float and integer will return True.
# Additionally, we're able to compare two completely different types
# without receiving an error because they're not equivalent.
#
# If we want to know if two objects aren't equivalent,
# then we can use the not equal operators !=.
# This will return True only if the items aren't equivalent:
#
print(1 != 1) # False
print(1.0 != 1) # False
print(2 != 1.0) # True
print('a' != 2) # True
print('a' != 'a') # False

# The Identity Operators
# If we want to know if two objects are or are not exactly the same object,
# then we can use the identity operators.
# The identity operator is the keyword is and the opposite is is not (with a space).
#
print(1 is 1) # True
print(1 is 1.0) # False
print('a' is 'a') # True
print('a' is not 'b') # True
print('a' is not 'a') # False

# The identity operators work based on the id of the object,
# and most of the basic types in Python are immutable (meaning they cannot be changed),
# so every time that we reference a specific literal it will point to the same item in memory.
# We can check the id of an object by using the id function (your return values will be different):
#
print(id('a')) # 4444195248
print(id('a')) # 4444195248
print(id('a') == id('a')) # True

# Not all objects are immutable,
# so you'll run into situations
# where you can compare two objects that look the same using "is"
# and have False returned. Here are two list literals (which aren't immutable):
#
print([] is []) # False



# additional examples

num1 = 5
num2 = 10
num3 = 10
print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 is num3)  # Both have the same value
print(num3 is not num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

