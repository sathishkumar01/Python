for i in range(7):
    for j in range(7):
        if ((j==6)and i!=6) or ((i==0) and j!=0) or ((i==6) and (j!=0 and j!=6) or ((i==5)and j==0) or ((i==4)and j==0)) :
            print("*",end="")
        else:
            print(end=" ")
    print()
        
