list=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
i=0
dic={}
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        if list[i][0]==list[j][0]:
            b.append(list[j][1])
        j+=1
    dic[list[i][0]]=b
    i+=1
print(dic)
    