record=[
    {'name' : ' ',
    'clas' : '',
    'roll_no': ''}
]


def add_info():

    # data=[]
    name = input("enter  name: ")
    clas= input("enter clas: " )
    roll_no=input("Enter roll no: ")
    record.append(name)
    record.append(clas)
    record.append(roll_no)
    # record.append(data)
    return 
print(record)
    
def lists():
    for i in range(0,len(record)):
        print(record[i])

 

def delete():
    a=input("Enter number to delete: ")
    for i in range(0,len(record)):
        if a == record[i]:
            del record[i]
    print("deleted successfullyyy")

 

def update():
    data=[]
    lists()
    a=int(input("Enter the number to update"))
    new_name=input("Enter new name: ")
    new_clas=input("Enter new class:")
    new_roll_no=input("Enter new roll_no: ")
    record[int(a)][0]=new_name
    record[int(a)][1]=new_clas
    record[int(a)][2]=new_roll_no
    print("success")


    
def menu():
    print("1. Add a new student")
    print("2. List all student")
    print("3.delete an existing student")
    print("4 update student value")
    choice=int(input("enter your choice"))
    if choice == 1:
        add_info()
    elif choice == 2:
        lists()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
    menu()
# print(record)
menu()