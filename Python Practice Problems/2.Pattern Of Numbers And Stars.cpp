n=input()
for x in range(1,int(n)+1):
    print(x, end=" ")
print("\n")
for l in range(1,int(n)):
    for i in range(1,int(n)-int(l)+1):
        print(i,end=" ")
    for j in range(2*int(l)-1):
        print("*",end=" ")
    print("\n")
