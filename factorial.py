def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

#def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))