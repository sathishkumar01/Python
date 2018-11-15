a=int(input('Enter a:'))
b=int(input('Enter b:'))

add=a+b
sub=a-b
multiply=a*b
division=a/b
Trncatedivision=a//b

negation=~a
Trncatedivision=a//b
exponential=a**b

print("The value of %d + %d is %d "%(a ,b ,add))
print("The value of %d - %d is %d "%(a,b,sub))
print("The value of %d * %d is %d "%(a,b,multiply))
print("The value of %d / %d is %d "%(a,b,division))
print("The value of %d // %d is %d "%(a,b,Trncatedivision))

print("The value of ~%d is %d "%(a,negation))
print("The value of %d and %d is %d "%(a,b,exponential))
