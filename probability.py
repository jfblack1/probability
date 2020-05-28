from math import log
from math import ceil

#Returns the permutation of selecting k different items from n number of items
def permutation (n, k):
    assert (isinstance(n, int))
    assert (isinstance(k, int))
    assert (n>0)
    assert (k>0)
    assert (k<=n)
    return (factorial (n) / factorial(n-k))

#Returns the combination of selecting k different items from n number of items
def combination (n, k):
    assert (isinstance(n, int))
    assert (isinstance(k, int))
    assert (n>0)
    assert (k>0)
    assert (k<=n)
    return (factorial (n) / (factorial (k) * factorial (n-k)))

#Returns the factorial of a number n
def factorial (n):
    assert (isinstance(n, int))
    assert (n >= 0)
    k=n
    total=k
    if (k == 0):
        total = 1
    k=k-1
    while (k>0):
        total=total*k
        k=k-1
    return total

#Returns the number of different ways of grouping n different items, or the number
#of different ways of adding whole numbers up to a number n.
def getNumberOfGroups (n):
    assert (isinstance (n, int))
    assert (n>=0)
    return 2 ** (n-1)

#Returns all the different ways of grouping n different items, or the
#different ways of adding whole numbers up to a number n.
def getGroups (n):
    assert (isinstance (n, int))
    assert (n>0)
    assert (n < 32) #This is an arbitrary number that limits the value of the input to prevent long processing times.
    k=0
    l=getNumberOfGroups (n)
    result=[]
    if (n == 1):
        result.append ([1])
    else:
        while (k < l):
            binaryArray=toBinaryArray (k, n - 1)
            l=[]
            l.append (1)
            for digit in binaryArray:
                if (digit == 1):
                    a = l.pop ()
                    a += 1
                    l.append(a)
                if (digit == 0):
                    l.append (1)
            result.append (l)
            k+=1
    return result
        

#Converts a number, k, into a binary array of length n.
#It is assumed that n is at least as large as the binary representation
#of k.
def toBinaryArray (k, n):
    assert (isinstance (k, int))
    assert (isinstance (n, int))
    assert (k >= 0)
    assert (n > 0)
    assert (k == 0 or ceil(log(k, 2)) <= n)
    result=[]
    num=1
    while (num <= k):
        num *= 2
    if (num > k):
        num /= 2
    if (k == 0):
        result.append(0)
    else:
        result.append(1)
    k -= num
    while (num > 1):
        num /= 2
        if (num <= k):
            result.append(1)
            k -= num
        else:
            result.append (0)
    while (len(result) < n):
        result.insert(0, 0)
    return result
    
    
        
        
        
    

print (getNumberOfGroups(2))
print (getNumberOfGroups(3))
print (getNumberOfGroups(4))
print (getNumberOfGroups(25))

print (permutation(5, 2))
print (combination(5,2))

print (factorial (4))
print (factorial (3))
print (factorial (2))
print (factorial (1))
print (factorial (0))

print (toBinaryArray(7, 4))
print (toBinaryArray(6, 4))
print (toBinaryArray(5, 4))
print (toBinaryArray(4, 4))
print (toBinaryArray(3, 4))
print (toBinaryArray(2, 4))
print (toBinaryArray(1, 4))
print (toBinaryArray(0, 4))

print (getGroups (1))
print (getGroups (2))
print (getGroups (3))
print (getGroups (4))
print (getGroups (5))
print (getGroups (6))