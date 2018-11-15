n=int(input("Enter Number of Digit:"))
sum=0;
while(n>0):
    a=n%10;
    sum=sum+a;
    n=n/10;
print("Sum of digits:",sum)
