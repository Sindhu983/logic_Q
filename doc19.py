list=[21,22,56]
i=0
dic={}
while i<len(list):
    j=0
    a=str(list[i])
    string=''
    while j<len(a):
        if a[j]=="1":
            string+="one"
        elif a[j]=="2":
            string+="two"
        elif a[j]=="3":
            string+="three"
        elif a[j]=="4":
            string+="four"
        elif a[j]=="5":
            string+="five"
        elif a[j]=="6":
            string+="six"
        j+=1
    dic[list[i]]=string
    i+=1
print(dic)




