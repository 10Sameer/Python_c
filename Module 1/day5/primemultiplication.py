def check_prime(number):
    counter = 0
    for i in range(1,number+1):
        if number % i ==0:
            counter = counter+1
        if counter == 2:
            prime = True
        else:
           prime= False
    return prime

# number = int(input("Enter a number to check prime"))
# value_of_check_prime = check_prime(number)
# if value_of_check_prime:
#    a=number^2+5*number+2
#    print("f(x)=",a)
# else:
#     for i in range(1,11):
#      print(f"{number}*{i}={number*i}")   