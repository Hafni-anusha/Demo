students = [{"name" : "manu",
            "roll_no" : 1,
            "subject" : "maths",
            "class" : 1 },

            {"name" : "sanu",
            "roll_no" : 2,
            "subject" : "hindi",
            "class" : 2 }
            ]


def add_student():
    students.append({"name":input("enter the name of the student"),"roll_no":input("enter the rollnumber of the student"),"subject":input("enter the subject"),"class":input("enter the class")})

    print("--------------------------------")


def remove():
    dele = input("enter the name to be deleted")
    for i in range(len(students)):
        if students[i]['name'] == dele:
            del students[i]
            break
        print("--------------------------------")

def update():
    upd = input("enter the name to be updated")
    for i in range(len(students)):
        if students[i]['name'] == upd:
            val = input("enter the value to be updated")
            if val == "name":
                students[i]["name"] = input("enter the new name")
                print("value updated sucessfully")
                break
            elif val == "roll_no":
                students[i]["roll_no"] = input("enter the new roll number")
                print("value updated sucessfully")
                break
            elif val == "subject":
                students[i]["subject"] = input("enter the new subject")
                print("value updated sucessfully")
                break
            elif val == "class":
                students[i]["class"] = input("enter the new class")
                print("value updated sucessfully")
                break
            else:
                print("inalid value entered")

        print("--------------------------------")


def call():
    options = int(input("1 - list all the students \n"
                "2 - Add a new student \n"
                "3 - Delete an existing student \n"
                "4 - update details of student \n"
                    "enter your options:"))

    if options == 1:
        print(students)
    elif options == 2:
        add_student()
    elif options == 3:
        remove()
    elif options == 4:
        update()
    else:
        print("invalid option")

    call()


call()

