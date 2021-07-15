list=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
dic={}
i=0
while i<len(list):
    c=list[i]
    i+=1
    dic.update(c)
print(dic)


# dict={}
# for i in list:
#     for key,val in i.items():
#         dict[key]=float(val)
# print(dict)




list=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
result = [dict([a, float(b)] for a, b in x.items()) for x in list]
print(result)
