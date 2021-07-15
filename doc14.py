dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
user=int(input("enter the num:"))
for key,value in dic.items():
    for i in value:
        print(value[user])
        break


dict = {'c1': 'Red', 'c2': 'Green', 'c3':None}
dic={}
for key,value in dict.items():
    if value is not None:
        dic[key]=value
print(dic)