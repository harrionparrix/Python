# As you might already know, Ada the Ladybug has a huge TODO-list. Sometimes she inserts a new job into her TODO-list and sometimes she is wondering whether there is a job (in her TODO-list), which she wants to do now. She doesn't require the whole job to be there, perhaps just a part of it.

# Can you create a program which would serve her? That means it either inserts a new job into her TODO-list or answers whether there exists a word (in her TODO-list) which is a substring of given word.

# Input
# The first line of input containts Q, the number of queries.

# The next Q lines contains a number 0 ≤ t ≤ 1 and nonempty string s. If t is equal to 0 then it is inserion query, otherwise it is question query. s consists of lowercase characters only.

# The sum of lengths of queries of both types doesn't exceed 106 (that means the total sum of lengths of strings will be at most 2*106)

# Output
# For each query of type 1, print either YES, if there is already a substring in the TODO-list and NO otherwise.

# Example Input
# 12
# 0 cat
# 1 dogville
# 0 dog
# 1 dogville
# 1 gooutwithcat
# 1 gooutwithcrocodile
# 1 fancyconcatenation
# 0 crocodile
# 1 lacoste
# 1 gooutwithcrocodile
# 1 catalanreferendum
# 1 rocodile
# Example Output
# NO
# YES
# YES
# NO
# YES
# NO
# YES
# YES
# NO

n=int(input())
l=[]
l1=[]
l2=[]
for i in range(n):
    flag=0
    p,q=int,input().split()
    l.append(q[0])
    l1.append(q[1])
    if(q[0]=="1"):
        for j in range(i):
            if(l1[i] in l1[j]=="TRUE"):
                flag=1
                break
        if(flag==1):
            l2.append("YES")
        else:
            l2.append("NO")
        
print(l2)