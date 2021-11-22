n=int(input())
if(n>=1 and n<=1000):
    for i in range(n):
        a,b=list(map(int, input().strip().split()))
        if(a>=1 and a<=5 and b>=1 and b<=5):
            if((a+b)%2==1):
                print("Alice")
            else:
                print("Bob")
