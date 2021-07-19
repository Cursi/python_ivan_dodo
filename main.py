from functools import reduce

X = [1, 2, 3, 4, 5, 6]

# def myFilterFunction(currentElement):
#     return currentElement % 2

# Y = []

# for c in X:
#     Y.append(c ** 2)

# Z = [c ** 2 for c in X if c % 2 == 0]

# W = list(filter(myFilterFunction, X))

# T = list(filter(lambda x: x % 2, X))

print(X)
# print(Y)
# print(W)
# print(T)

# u = list(map(lambda x: x ** 3, X))

# print(u)

R = reduce(lambda m, n: m+n, X)

print(R)