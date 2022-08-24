a = int(input())
b = int(input())

# a = 472
# b = 385

first = str(b)[2]
second = str(b)[1]
third = str(b)[0]
# print(first, second, third)

print(str(a*int(first)))
print(str(a*int(second)))
print(str(a*int(third)))
print(str(a*int(first) + a*int(second)*10 + a*int(third)*100))