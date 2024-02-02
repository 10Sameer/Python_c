A=[1,4,5,8,9,100,25,56,53,87]
temp_value=A[0]
for element in A:
    if element > temp_value:
        temp_value=element
    max_value = temp_value
print(max_value)
    
    
# Another way
A=[98,56,88,125,15]
B=A[0]
for i in A:
    if i>B:
        B=i
    C=B
print(C)