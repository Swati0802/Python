i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue   # skip.   # and forward code will not give output
    print(i)
    i += 1

# Odd
i = 0
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# Even 
i = 0
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
