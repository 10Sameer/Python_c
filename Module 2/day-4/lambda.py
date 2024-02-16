# f_x = lambda x: x**2 + 5*x + 3
# print(f_x(5))


# def f_x(x) :
#     y = x**2 + 5*x + 3
#     return y
# numbers = [1,2,3,4,5,6,7,8,9,10]
# y=[f_x(x) for x in numbers]
# print(y)


def f_x(x) :
    y = x**2 + 5*x + 3
    return y
numbers = [1,2,3,4,5,6,7,8,9,10]
# y=[f_x(x) for x in numbers]
# print(y)

map_example = list(map(f_x,numbers))
print(map_example)

