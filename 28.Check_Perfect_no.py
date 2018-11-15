n=int(input('Enter n:'))
k=0
t=n;
for i in range(1,n):
    if(n%i==0):
        k=k+i

if(k==t):
    print("Entered No is perfect Number")
    
