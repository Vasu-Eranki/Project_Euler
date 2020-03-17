#!/bin/python3
def fibonacci(n):
    x=[2,8]
    while(n>max(x)):
        length = len(x)
        temp = 4*x[length-1]+x[length-2]
        x.append(temp)
    x.pop()
    return sum(x)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = fibonacci(n)
    print(result)
