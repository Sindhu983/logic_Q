dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key value count")
count=0
for key,value in dict.items():
    count+=1
    print(key,' ',value, ' ',count)
