import math
t=int(input())
while t>0:
    n=int(input())
    val=int(math.sqrt(n))

    for i in range(0,val+1):
        for j in range(0,val+1):
            if i**2 + j**2 ==n and i<=j:
                print(f"({i},{j})", end=" ")
    t-=1
    print("\n")
