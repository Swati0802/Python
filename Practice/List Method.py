#If we want to print new changes, we have to right the print(list)
# also we can write string. in string, ascending order by alphabet like A then B and so on.

list = [2, 1, 3]
list.append(4)  # adds one elemnt at the end
print(list)

#sorts in ascending order
list.sort()  # It change in original String
print(list)

#descending order
list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(5,0)  #(index, element)
print(list)

list.remove(0) # (elemnt)
print(list)

list.pop(1) # (index)
print(list)

list.copy()
print(list)
