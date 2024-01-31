a = int(input("Enter a number"))
c = 0
for i in range(1,a+1):
    if a % i == 0:
        c = c+1
if c == 2:
        print("It is prime")
else:
        print("not prime")
        