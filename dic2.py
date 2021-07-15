dic={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
sum=0
for key,val in dic.items():
    sum=sum+len(val)
print(sum)
