n=int(input("ENTER NO OF ROWS:"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
