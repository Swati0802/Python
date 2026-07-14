def calc_avg(a,b,c):
    return (a+b+c)/2

avg = calc_avg(1,2,3)
print(avg)


def calc_prod(a,b=2):   # Default Parameter
    return a * b

prod = calc_prod(1)
print(prod)
