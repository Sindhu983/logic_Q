list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
#{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
i=0
dic={}
while i<len(list):
    j=0
    b=[]
    while j<len(list[i]):
        if list[i][j]!=list[i][0]:
            b.append(list[i][j])
        j+=1
    dic[list[i][0]]=b
    i+=1
print(dic)



