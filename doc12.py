students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for key,value in students.items():
    print(key)
    for i in value:
        print(i,":",value[i])
