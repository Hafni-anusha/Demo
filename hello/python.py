list1=[{"name":'afi',"id": 11,"class":2},
{"name":"anusha","id":12,"class":3},
{"name":"megha","id":13,"class":4}]
list2=[{"name":'afi',"rollnum":22},
{"name":"anusha","rollnum":24},
{"name":"sali","rollnum":36}]
list3=[]
list4=[]

for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]['name'] == list2[j]['name'] :
            
            list3.append(list1[i]['name'])
            # list3.append(list1[j]['name'])
            list3.append(list2[j]['rollnum'])
            
            # list3.sort()
# for i in range(0,len(list3)):
#     sort lists(list3)
print(list3)
            # equal.append("name")\
            # equal.append("rollnum")
            # print(list1("name"),list2())
            # equal.extend('name','rollnum')
