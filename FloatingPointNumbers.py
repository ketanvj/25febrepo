
# Not all decimal numbers that we write out can be represented by a computer as a float.
# The reason for this is that floats are stored on computer hardware as binary fractions,
# and not all decimal (base 10 numbers) can be represented as binary fractions.
# This leads to the floating-point numbers that we work with
# actually being approximations of the binary fraction representation.

# An example of this is the decimal number 0.1 which has no binary fraction equivalent.
# Depending on the machine, the exact approximation used behind the scenes may be different.
# But since Python 3.1, the representation that is returned to the user
# is the clean number even though the number used behind the scenes is
# something like 0.1000000000000000055511151231257827021181583404541015625.

# All of this is to say that sometimes floating-point math doesn't work the way that we expect it to.