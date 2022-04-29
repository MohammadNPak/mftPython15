
import json
import csv
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
    
    elif command == "save":
        with open("data.txt","w") as f:
            for student in students:
                f.write(f"{student['name']},{student['last_name']},{student['age']},{' '.join(map(str,student['grades']))}\n")

    elif command == "load":
        students = []
        with open("data.txt","r") as f:
            for line in f.readlines():
                d = line.strip().split(",")
                student = { "name":d[0],
                        "last_name":d[1],
                        "age":int(d[2]),
                        "grades": [float(x) for x in d[3].split()]}
                students.append(student)



    elif command == "save_csv":
        if students:
            with  open("data.csv","w") as f:
                f.write(",".join(students[0].keys())+'\n')
                for student in students:
                    f.write(f"{student['name']},{student['last_name']},{student['age']},{' '.join(map(str,student['grades']))}\n")
                

    elif command == "load_csv":
        students = []
        with open("data.csv","r") as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                student = { "name":line[0],
                        "last_name":line[1],
                        "age":int(line[2]),
                        "grades": [float(x) for x in line[3].split()]}

                students.append(student)
