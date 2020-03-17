# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
def convergence(n):
    y = [1, 2]
    k = 2
    count =1
    x=[2,3]
    for i in range(2, n):
        if(count%3==0):
            y.append(2*k)
            k+=1
            count= 1
        else:
            y.append(1)
            count+=1
    for i in range(1,n-1):
        temp = y[i]*x[i]+x[i-1]
        x.append(temp)
    z=str(max(x))
    print()
    total=0
    for j in z:
        total = total+int(j)
    if(n==1):
        total =2 
    elif(n==2):
        total = 3
    else:
        pass
    return total
if __name__=='__main__':
    n = int(input())
    sum1 = convergence(n)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(sum1)+'\n')
    fptr.close()  
    
