n=int(input('Enter n:'))
sum1=0
t=n
while (n>0):
    rem=n%10
    sum1=sum1+(rem*rem*rem)
    n=n//10

if t==sum1:
    print ('Entered no is Armstrong_no')
else:    
    print ('Entered no is NOT Armstrong_no')

