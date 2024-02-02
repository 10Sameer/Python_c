A=[1,2,3,4,5,6,7,8,9]
even_list,odd_list=[] , []
for element in A:
   if element % 2 == 0:
      even_list.append(element)
   else:
       odd_list.append(element)

print(even_list,odd_list)       


# List comprehension technique Important
C=[element+3 for element in A]
print(C)
D=[element for element in A if element % 2 ==0]
print(D)
#E=[element for element in A if element % 2 ! =0]
#print(E)

F=[1,2,5,-5,-8]
D=[element for element in F if element > 0]
print(D)
E=[element for element in F if element < 0]
print(E)
print(len(F))
print(len(D))
print(len(E))
