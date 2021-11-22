#Disabled King Problem Code: DISABLEDKING
t=int(input())
if(t>=1 and t<=500):
    for i in range(t):
        n=int(input())
        if(n>=2 and n<=500):
            if(n%2==1):
                print(n-1)
            else:
                print(n)