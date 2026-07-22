# 1
list = ["goa", "noida", "pune", "mumbai", "channai"]

def find_len(list):
    return len(list)

len = find_len(list)
print(len)

# 2
def print_list(list):
    for item in list:
        print(item, end= " ")

print_list(list)

# 3
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

calc_fact(5)

# 4
def converter(usd_val):
    inr_val = usd_val * 95.16
    print(usd_val,"USD =", inr_val, "INR")

converter(100)

# 5
def check_num(n):
    if n %2 == 0:
        print("EVEN")
    else:
        print("ODD")

check_num(8)
