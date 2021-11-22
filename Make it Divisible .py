n=int(input())
sum=0
if(n>=1 and n<=50):
    for i in range(n):
        A=[]
        q=[]
        flag1=0
        flag2=0
        s=int(input())
        sum+=s;
        if(sum<=2*(10**5)):
            if(s>=2 and s<=10**5):
                p=list(input().split())
                for k in range(len(p)):
                    q.append(int(p[k]))
                for o in range(s):
                    if(q[o]>=1 and q[o]<=10**9):
                        if(q[o]%3==1):
                            flag1+=1
                        if(q[o]%3==2):
                            flag2+=1
                if(flag1>=1 and flag1==flag2):
                    print(flag1)
                else:
                    if(flag1==0 and flag2==0):
                        print("0")
                    else:
                        print("-1")
                    

