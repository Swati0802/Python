n = int(input("Enter n :"))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print("Factorial :", fact)


# By For loop
n = int(input("Enter n :"))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial :", fact)
