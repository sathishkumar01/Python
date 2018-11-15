n=int(input('Enter n:'))
rev=0
t=n
while (n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

if t==rev:
    print ('Entered no is Palindrome')
else:    
    print ('Entered no is NOT Palindrome')

