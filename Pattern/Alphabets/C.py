for i in range(4):
    for j in range(4):
        if ((j==0 ) and i!=0 and i!=3) or ((i==0 or i==3) and (j>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
