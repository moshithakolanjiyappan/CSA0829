m=[[1,2,3],[4,5,6],[7,8,9]]
print("diagonal elements are...")
for i in range(0,3):
    sum=0
    for j in range(0,3):
        sum+=m[i][j]
    print (i,'column sum=',sum)
