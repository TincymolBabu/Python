h=input("enter the word:")
vowels= "aeiou"
firstlist=[]
for x in h:
     if (x in vowels and x not in firstlist):
         firstlist.append(x)

print(firstlist)