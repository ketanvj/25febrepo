# One thing to note is that when a variable, first,
# is assigned to another variable, second,
# its value is copied into second.
# Hence, if we later change the value of first,
# second will remain unaffected:
first = 20
second = first
first = 35  # Updating 'first'

print(first, second)  # 'second' remains unchanged

num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)


