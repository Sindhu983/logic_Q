a=[1,2,3]
a1=[]
a2=[]
i=0
while i<len(a)-1:
    a1.append(a[i])
    i+=1
a2.append(a[-1])
a3=[]
j=0
while j<len(a):
    m1=[a1[j],a1[j+1]]
    m2=[a1[j],a2[j]]
    m3=[a1[j+1],a2[j]]
    a3.append(m1)
    a3.append(m2)
    a3.append(m3)
    j+=1
    break
print(a3)