#!/bin/python
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = list(str(input().strip()))
    product = 0
    for i in range(0,len(num)-k):
        temp =1
        for j in range(0,k):
            temp = temp*int(num[i+j])
        product = max(product,temp)
    print(product)
