lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
flag=0
i=1
while i<n:
    if lst[i-1]>lst[i]:
        i+=1
    else:
        if lst[i-1]==lst[i]:
            flag=1
            break
        else:
            break
flag2=0
while i<n:
    if flag==1:
        i=i+1
        flag=0
    elif lst[i-1]<lst[i]:
        i=i+1
    else:
        flag2=1
        break
if flag2==1:
    print("false")
else:
    print("true")
