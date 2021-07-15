dic={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
list=[]
for i in dic:
    k=dic[i]
    list.append(k)
dict={}
i=0
while i<len(list):
    j=0
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
        j+=1
        dict[list[i]]=count
    i+=1
print(dict)
