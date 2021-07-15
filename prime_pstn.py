# user=int(input("enter the number :"))
# a=2
# count=0
# while a>0:
#     b=2
#     while b<a:
#         if a%b==0:
#             break
#         b+=1
#     else:
#         if count==user:
#             print(a)
#             break
#         count+=1
#     a+=1



user=input("enter sentence")
b=user.split()
i=0
s=""
while i<len(b):
    if b[i]==b[0]:
        s=s+b[i][0]
    else:
        s=s+"."+b[i]
    i=i+1
print(s)


    