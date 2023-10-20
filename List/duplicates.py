originallist = [1, 2, 2, 3, 4, 4, 5]
uniquelist = []
for item in originallist:
    if item not in uniquelist:
        uniquelist.append(item)
print(uniquelist)
