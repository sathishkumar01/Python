for i in range(10):
    for j in range(6):
        if ((j==0 ) and i>0 and i<3) or ((i==0 or i==3) and (j>0 and j<4)) or ((j==4) and i>0 and i<3) or  ((j==3) and i==2) or ((j==4) and i==3) or ((j==5) and i==4) :
            print("*",end="")
        else:
            print(end=" ")
    print()
