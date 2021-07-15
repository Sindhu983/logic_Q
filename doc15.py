dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
dict={}
for key,value in dic.items():
    if value[0]>=6.0 and value[1]>=70:
        dict[key]=value
print(dict)

