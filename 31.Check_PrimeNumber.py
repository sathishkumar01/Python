n=int(input('Enter n:'))
k=0;
for i in range(1,n+1):
    if(n%i==0):
        k=k+1

if(k==2):
    print("Entered No is prime Number")
else:
    print("Entered No is NOT prime Number")
    
