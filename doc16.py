dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
num=int(input("enter the number:"))
for key,value in dic.items():
    if value==num:
        print("True")
    else:

        print("False")
    



lst=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
list=[]
lst.remove(lst[0])
list.append(lst)
print(list)
