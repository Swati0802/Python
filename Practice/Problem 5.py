# 1 
i = 1 
while i <= 100 :
    print(i)
    i = i + 1

# 2
i = 100
while i >= 1 :
    print(i)
    i = i - 1

# 3
n = int(input("Enter the n : "))
i = 1
while i <= 10:
    print(n * i)
    i = i + 1 

# 4
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] # so go towards on tuple or list ,it is called Traverse(Travel)
idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1

# 5
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1
