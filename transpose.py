X =[[12,7],[13,5],[14,2]]
result =[[0,0,0],[0,0,0]]

#iterate through the rows

for i in range(len(X)):
    #iterate through columns
    
    for j in range(len(X[0])):
        result[j] = X[i][j]
        
for r in result:
