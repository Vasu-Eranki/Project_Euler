#!/bin/python3
import math 

def prime(n):
    count =0
    while(n%2==0):
        n=n//2
        count =2 
    for i in range(3,int(n**0.5)+1,2):
        while(n%i==0):
            n=n//i
            count = i
    return n if n>2 else count
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest = prime(n)
    print(largest)
