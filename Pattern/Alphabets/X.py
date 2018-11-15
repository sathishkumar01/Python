for i in range(7):
    for j in range(8):
        if ((j==0 and i==0)) or ((j==1 and i==1)) or ((j==2 and i==2)) or ((j==3 and i==3)) or ((j==4 and i==4)) or ((j==5 and i==5)) or ((j==5 and i==0)) or ((j==4 and i==1)) or ((j==3 and i==2)) or ((j==2 and i==3)) or ((j==1 and i==4)) or ((j==0 and i==5))  :
            print("*",end="")
        else:
            print(end=" ")
    print()
        
