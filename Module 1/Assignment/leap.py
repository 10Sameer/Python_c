def leap_year(year):
    if (year%4==0):
        print("its a leap year")
    else:
        print("its not a leap year")

find=int (input("enter a year"))
leap_year(find)


def positive_negative(number):
    if number==0:
        print("its a zero")
    elif number>0:
        print("its a positive number")
    else:
        print("its a negative number")


find=int (input("enter a number"))
positive_negative(find)


