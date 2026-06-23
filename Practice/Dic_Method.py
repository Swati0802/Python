student = {
    "name" : "shradha",
    "subejcts" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 99
    }
}

print(student.keys())
print(list(student.keys()))
print(len(student)) #print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
pair = list(student.items())
print(pair[0])

print(student.get("name"))
print(student.get("name2")) #None(no error)

student.update({"city" : "delhi "})
print(student)

new_dict = {"name" : "manan","city" : "delhi", "age" : 60}
student.update(new_dict)
print(student)
