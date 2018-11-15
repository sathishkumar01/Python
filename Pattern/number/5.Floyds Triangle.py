n=int(input('Enter n:'))
a=0
for i in range(1,n):
    for j in range(1,i):
        a=a+1
        print(a,end=" ")
    print()
