list=[{"name":"shailu","cash":200},{"name":"shailubujji","cash":50},{"name":"sindhu","cash":350},{"name":"sindhuqueen","cash":250}]
user=input("enter the name :")
for i in list:
    a=i["name"]
    if user in i["name"]:
        print(i)
sum=0
for j in list:
    sum=sum+j["cash"]
print(sum)



a=[1,2,3]
b=[4,5,6]
list=[]
i=0
while i<len(a):
    j=0
    while j<len(b):
        c=[a[i],b[j]]
        list.append(c)
        j+=1
    i+=1
print(list)
        