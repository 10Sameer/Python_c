def get_multiplication_table(num):
    for i in range(1,11):
        
        print(f"{num} * {i} = {num*i}")
        
number = int(input("Enter a number"))

for i in range(10):
   get_multiplication_table(number)

