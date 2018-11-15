for i in range(5):
    for j in range(7):
        if ((i==0 and j<6 )) or (i==4) or ((j==4) and i==1) or ((j==3) and i==2) or ((j==2) and i==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
