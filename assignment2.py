
def reverseStr(string):
    length = len(string)
    if length == 1:
        return string
    return string[length-1] + reverseStr(string[0:length-1])

def productOfItems(list):
    lengthOfList = len(list)
    newList = []
    for i in range(lengthOfList):
        newList.append(1)
        for j in range(lengthOfList):
            if i == j:
                continue
            else:
                newList[i]*=list[j]
    return newList


if __name__  == "__main__":
    print(reverseStr("Ivan"))

    print(productOfItems([1,2,3,4]))