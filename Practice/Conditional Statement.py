age = int(input("Enter your age :"))
if(age >= 18):
    print("You can vote & Apply for license") # indentation
else:
    print("You can not vote & Apply for license\n")

''' if = always checked  
elif = if "if" is false then after elif checked'''


# New
light = "pink"
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")
