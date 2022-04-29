

# student = {"name":"ali","last_name":"alavi","age":15,[2,3,4]:"a key"}

# student["name"]=" mohammad "+student["name"]
# student[(2,3,4)]+="5"

# print(student[(2,3,4)])
# immutable  => tuple  str int float complex bool
# mutable    => list set dict
# a= (2,3,4)
# a = 2.2
# print(hash(a))
# print(type(hash()))
# print(id(a))

# student = {"name":"alireza","last_name":"alavi","age":15,"grades":[20,12,17,18]}

# print(max(student["grades"]))

# max
# min
# sum
# abs
# print(f"name:{student['name']}\nlast name: {student['last_name']}")

import json

students = []
while True:
    command= input("command: ")
    if command == "add":
        student = { "name":input("please enter your name: "),
                    "last_name":input("please enter your last name:"),
                    "age":int(input("please enter your age: ")),
                    "grades": list(map(float,input("please enter your grades:").split()))
                    }
        students.append(student)
    elif command == "quit":
        break
    elif command=="show all":
        for i in range(len(students)):
            student = students[i]
            print(f"""\t\t{i:4} name:{student['name']}
            last name: {student['last_name']}
            age: {student['age']}
            grades: {student['grades']}
            mean: {sum(student['grades'])/len(student['grades'])}""")
    elif command=="show student":
        name = input("please enter student name")
        last_name = input("please enter student last name")
        for student in students:
            if student["name"]== name and student["last_name"] == last_name:
                print(f"""\t\t{i:4} name:{student['name']}
                last name: {student['last_name']}
                age: {student['age']}
                grades: {student['grades']}
                mean: {sum(student['grades'])/len(student['grades'])}""")
            else:
                print(f"student with name {name} and last name {last_name} does not exist!")
    elif command == "show top":
        top_index = 0
        max_mean = 0
        for i in range(len(students)):
            grades = students[i]["grades"]
            mean = sum(grades)/len(grades)
            if mean > max_mean:
                top_index=i
        student = students[i]
        print(f"""\t\t{i:4} name:{student['name']}
        last name: {student['last_name']}
        age: {student['age']}
        grades: {student['grades']}
        mean: {sum(student['grades'])/len(student['grades'])}""")
    
    if command == "save":
        f = open("data","w")
        for student in students:
            f.write(f"")


    # elif command == "save":
    #     file_name = input("please enter file address: ")
    #     f = open(file_name,"w",encoding="utf8")
    #     json.dump(students,f)
    #     f.close()
    # elif command=="load":
    #     file_name = input("please enter file address: ")
    #     f = open(file_name,"r",encoding="utf8")
    #     students= json.load(f)
    #     f.close()


