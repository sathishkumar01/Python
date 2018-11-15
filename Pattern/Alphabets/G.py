for i in range(5):
    for j in range(6):
        if ((j==0 ) and i!=0 and i!=4) or ((i==0 ) and j>0 and j<5) or ((i==4) and j>0 ) or ((j==5) and i>=2 and i<5) or ((j==4) and i==2)or ((j==3) and i==2) :
            print("*",end="")
        else:
            print(end=" ")
    print()
        
