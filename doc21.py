


# dict={"name":"sindhu","name2":"anusha"}
# dic={}
# for key,value in dict.items():
#     dic[value]=key
# print(dic)




dic={"name":"sindhu","name2":"anusha"}
print(dict(zip(dic.values(),dic.keys())))


dic={1:"sindhu",4:"Anusha",2:"sowji",3:"shabeera"}
dict={}
a=sorted(dic.items())
for key,value in a:
    dict[key]=value
print(dict)
    