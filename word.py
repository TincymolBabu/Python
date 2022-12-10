sentence=input("enter the text")
counts=dict()
words=sentence.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
print(counts)