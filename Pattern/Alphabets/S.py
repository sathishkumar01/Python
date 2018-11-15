for i in range(10):
    for j in range(8):
        if ((j==0 ) and i>0 and i<3) or ((i==0 or i==3) and (j>0 and j<6)) or ((j==7) and i>3 and i<=5) or ((i==6) and  j>0 and j<6):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
