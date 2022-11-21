s="[{(a+b)}]"
y=[]
for i in s:
    count=0
    if i  not in ")}]":
        y.append(i)
    if i ==")":
        for j in range(len(y)-1,-1,-1):
            if y[j] =="(":
                y.pop()
                if count==0:
                    print("False")
                break
            else:
                y.pop()
                count+=1
    if i =="}":
        for j in range(len(y)-1,-1,-1):
            if y[j] =="{":
                y.pop()
                if count==0:
                    print("False")
                break
            else:
                y.pop()
                count+=1
    if i =="]":
        for j in range(len(y)-1,-1,-1):
            if y[j] =="[":
                y.pop()
                if count==0:
                    print("False")
                break
            else:
                y.pop()
                count+=1
print("True")