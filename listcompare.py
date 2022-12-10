n1=int(input("no of elements in the first list : "))
list1=[]
for i in range(n1):
    value=int(input("enter the elements : "))
    list1.append(value)
n2=int(input("no of elements in the second list : "))
list2=[]
for i in range(n2):
    value=int(input("Input no : "))
    list2.append(value)
if(n1 == n2):
    print("Same length")
else:
    print("Not same length ")

if(sum(list1)==sum(list2)):
    print("Same sum ")
else:
    print("Sum are different")
list3=[each for each in list1 if each in list2]
print("Same members are  :",list3)