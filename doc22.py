dic={'g':'red','h':'blue','i':'blue','j':'red','k':'pink'}
for i in dic:
    for j in dic:
        if i==j and i!="k":
            print(i)
