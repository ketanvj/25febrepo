# The not Operation
# Sometimes we want to know the opposite boolean value for something.
# To do this, we use the unary operators not:

print(not True) # will lead to False
print(not False) # will lead to True

# The or Operation
# The boolean or operator works the same way that the bitwise OR operator did
# if we are only considering one bit.
# The bit of 1 is equivalent to True and 0 is equivalent to False
#
print(True or True) # will lead to True
print(True or False) # will lead to True
print(False or False) # will lead to False
print(False or True) # will lead to True

# The and Operation
# The and operator is the opposite of or,
# and both of the operands need to be true.
#
print(True and True) # will lead to True
print(True and False) # will lead to False
print(False and False) # will lead to False
print(False and True) # will lead to False

name = "John"
age = 24
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# Bit Value #
# All the code we see around us in today’s world is actually made up of bits.
# Combinations of 1s and 0s form the foundation of programming.
# # In bit terms, the value of True is 1. False corresponds to 0:
print(10 * True) # 10
print(10 * False) # 0