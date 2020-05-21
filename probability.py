#Returns the permutation of selecting k different items from n number of items
def permutation (n, k):
    return (factorial (n) / factorial(n-k))

#Returns the combination of selecting k different items from n number of items
def combination (n, k):
    return (factorial (n) / (factorial (k) * factorial (n-k)))

#Returns the number of different ways of grouping n different items, or the number
#of different ways of adding whole numbers up to a number n.
def getNumberOfGroups (n):
    return 2 ** (n-1)

  