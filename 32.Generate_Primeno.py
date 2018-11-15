n=int(input('Enter n:'))

for i in range(1,n):
    c=1
    for j in range(2,n):
        if(i%j==0):
            c=c+1
    if c==2:
        print (i)

    

        



















    
