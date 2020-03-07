text=input("Enter a text\n")
listA=text.split()
i=0
for i in listA:
    j=1
    for j in listA:
        if listA[i]==listA[j]:
            del listA[j]
    else:
        continue
    j+=1
i+=1
print(listA)
