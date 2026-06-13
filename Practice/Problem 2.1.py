marks = int(input("Enter your mark :"))

if(marks >= 90):
    Grade = "A"  # print("Grade = A")
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print("Grade of student ->", Grade)

# Nesting
age = 18
if(age>=18):
    if(age>=80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("can not drive")
