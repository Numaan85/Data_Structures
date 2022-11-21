def reverse_stack(s1,s2,n):
    if n==1:
        return s1
    m=s1.pop()
    s2.append(m)
    last=s1[-1]
    q=s2.pop()
    s1.append(q)
    reverse_stack(s1,s2,n-1)
    s1.append(last)
    return s1

s1=list(int(ele) for ele in input("Enter the number").split())
s2=[]
n=len(s1)
print(reverse_stack(s1,s2,n))