# Palindrome = Racecar
list = [1, 2, 3, 2, 1]

list_copy = list.copy()

list.reverse() 
list_reverse = list

if(list_copy == list_reverse):
    print("Palindrome")
else:
    print("NOT Palindrome")
