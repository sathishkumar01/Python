n=int(input("ENTER NO OF ROWS:"))
for i in range(0,n):
    for k in range(1,n-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end="")    
    print()
