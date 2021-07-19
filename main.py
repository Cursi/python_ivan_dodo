from functools import reduce

x = [1, 2, 3, 4, 5, 6]

# y = []

# def myfilterFunction(currentElement):
#     return currentElement % 2 == 1

# for c in x:
#     y.append(c ** 2)

# z=[c ** 2 for c in x if c % 2 == 0]

# W=list(filter(myfilterFunction, x))
# T=list(filter(lambda x: x % 2, x))
# print(W)

print(x)
# print(y)
# print(z)
# print(T)

# u = list(map(lambda x: x ** 3, x))
# print(u)

R = reduce(lambda m,n: m+n, x)

print(R)