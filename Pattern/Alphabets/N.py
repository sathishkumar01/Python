for i in range(5):
    for j in range(8):
        if ((j==0)) or ((j==1 and i==0)) or ((j==2 and i==1)) or ((j==3 and i==2)) or ((j==4 and i==3)) or ((j==5))  :
            print("*",end="")
        else:
            print(end=" ")
    print()
        
