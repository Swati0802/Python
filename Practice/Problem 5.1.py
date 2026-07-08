# 1
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)

# 2.   It is linear search
list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a value of X :"))
idx = 0
for el in list:
    if(el == x):
        print("X Found at index",idx)
        break
    idx = idx + 1
