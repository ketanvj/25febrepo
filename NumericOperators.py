
x = 5
y = 6
x + y   # sum of x and y
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

x - y   # difference of x and y

print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)


x * y   # product of x and y

print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)

print(10.2 * 3)


x / y   # quotient of x and y. Converts the result to a float even when evenly divided.

print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)

x // y  # floored quotient of x and y, also called integer division

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

# For above the resultant value is a whole integer,
# though the result’s type is not necessarily int.
# The result is always rounded towards minus infinity:
# 1//2 is 0, (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0.

x % y   # remainder of x / y as int

print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication
# paranthesis
print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))




-x  # x negated

+x  # x unchanged

abs(x)  # absolute value or magnitude of x

int(x)  # x converted to integer

float(x)    # x converted to floating point


divmod(x, y)    # the pair (x // y, x % y)

pow(x, y)   # x to the power y
x ** y  # x to the power y
# i++ = i = i + 1 - not supported by Python


my_binary = 0b1010