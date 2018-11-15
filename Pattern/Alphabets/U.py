for i in range(6):
    for j in range(7):
        if (((j==0 and i!=5) or (j==6 and i!=5) ) or (i==5 and j!=0 and j!=6)  ):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
