len=int(input("how many elements you want to enter "))
list = []
count=0
for i in range(0,len):
    fname = input("Enter name : ")
    list.append(fname)
for words in list:
    for letters in words:
        if(letters=="a"):
            count=count+1;
print(count)
