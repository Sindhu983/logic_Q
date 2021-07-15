list=[3,9,6.5,5.3,"9"]
new=[]
i=0
sum=0
while i<len(list):
    if list[i] not in new:
        new.append(int(list[i]))
        sum=sum+new[i]
        i+=1
print(sum)



print("...........")




i=1
a=1
while i<=4:
    j=1
    while j<=5:
        print(j**i,end=" ")
        j+=1
        a+=1
    print()
    i+=1
    
       




