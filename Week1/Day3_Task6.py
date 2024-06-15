#merge intervals
InputList=[(1, 3), (2, 6), (8, 10), (15, 18)]
updatedlist=[]
newtuple=()
count=0
# print(InputList[0][1])
for tupleIndex in range(len(InputList)):
    if count <= len(InputList):
        #print(count)
        if newtuple == ():
            newtuple = InputList[tupleIndex]
        else:
            if newtuple[1] >= InputList[tupleIndex][0]:
                newtuple = (newtuple[0], max(newtuple[1], InputList[tupleIndex][1]))
                #print(newtuple)
            else:
                updatedlist.append(newtuple)
                newtuple = InputList[tupleIndex]
        count += 1
    else:
        break

updatedlist.append(newtuple)
print(updatedlist)