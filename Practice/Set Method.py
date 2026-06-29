collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apna colleg")
collection.add((1, 2, 3))  #we cannot add list, it will be changed().

collection.remove(1)
print(collection)

collection.clear()

print(len(collection))

#pop
collection = {"hello", "world", "coding", "python"} # removes a random value
print(collection.pop())
print(collection.pop())

# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

#intersection
print(set1.intersection(set2))
