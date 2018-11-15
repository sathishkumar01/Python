n=int(input('Enter n:'))
c=1
for i in range(0,n+1):
    for k in range(0,n-i+1):
        print(" ", end="")
    for j in range(0,i+1):
        if (j==0 or i==0):
            c=1;
        else:
            c=c*(i-j+1)//j;
        print(c, end=" ")
    print()
