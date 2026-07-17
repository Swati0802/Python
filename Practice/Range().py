print(range(5))

# new
seq = range(5)  # range(stop)
for i in seq:
    print(i)

# In general we write this syntax
for i in range(0, 10):  # range(start, stop)
    print(i)

# Odd
for i in range(0, 10, 2):  # range(start, stop, step)
    print(i)

# Even
for i in range(1, 10, 2):
    print(i)
