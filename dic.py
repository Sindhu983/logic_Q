dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for i in dic:
    v=dic[i]
    d=[]
    for j in v:
        if j%2==0:
            d.append(j)
        dic[i]=d
print(dic)
            

print("....................................................")


dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for i in dic:
    v=dic[i]
    k=[]
    for j in v:
        if j%2==1:
            k.append(j)
        dic[i]=k
print(dic)
            

