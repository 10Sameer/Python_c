A=[[2,3,4],[1,1,1],[2,2,2]]
B=[[1,1,1],[2,16,5],[8,7,2]]
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
 for j in range(len(B)):
     C[i][j]=A[i][j]+B[i][j]
print(C)