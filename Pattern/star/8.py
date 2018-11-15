n=int(input("ENTER NO OF ROWS:"))
k=9
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,k+1):
        print("*",end=" ")
    k=k-2
    print()
