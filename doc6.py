dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
dic={}
for key,value in dict.items():
    dic[value]=len(value)
print(dic)