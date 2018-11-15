for i in range(4):
    for j in range(7):
        if ((j==0 )) or ((i==0) and j!=6) or ((i==3) and j!=6) or ((j==6) and i>0 and i<3) :
            print("*",end="")
        else:
            print(end=" ")
    print()
        
