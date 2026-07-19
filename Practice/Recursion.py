# Function calls itself repeatedly.
def show(n):
    if (n == -1):   #Base Case
        return
    print(n)
    show(n-1)
    print("END")
show(5)


# New
def  fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))
