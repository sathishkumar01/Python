for i in range(4):
    for j in range(7):
        if ((j==0)and i==0) or ((j==1)and i==1) or ((j==2)and i==2) or ((j==3)and i==1) or ((j==4)and i==0):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
