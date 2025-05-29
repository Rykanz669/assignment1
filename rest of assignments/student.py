students = {"alice":(85,90,78),
            "bob":(50,45,60)}

name = input("enter student name: ")

if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print(average)
    if average > 60:
        print("passed")
    else:
        print("failed")
else:
    print("student not found")





