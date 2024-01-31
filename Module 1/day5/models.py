from primemultiplication import check_prime

number = int(input("Enter a number to check prime"))
value_of_check_prime = check_prime(number)
if value_of_check_prime:
   a=number^2+5*number+2
   print("f(x)=",a)
else:
    for i in range(1,11):
     print(f"{number}*{i}={number*i}")   