#Dictionary is mutable (we can change). Always we keep string as a key. 
# generally, we can keep tuple as a key because it cannot change and it is not mutable. also we can write any datatype as a key but it will not be changing (like any number).
dict = {
    "key" : "Value",
    "name" : "apnacollege",
    "subject" : ["Python", "C", "C++"],
    "topics" : ("dict", "set"),
    "learning" : "coding",
    True : 35,
    14.4 : "true",
    12 : 94.4
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict["subject"])

# Change 
dict["name"] = "shradha"
dict["surname"] = "khapra"
print(dict)

null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)
