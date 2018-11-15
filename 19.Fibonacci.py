n=int(input("Enter Number:"))
a=1
b=1
print(a)
print(b)
for x in range(0,n+1):
    c=a+b;
    a=b;
    b=c;
    print(c)
