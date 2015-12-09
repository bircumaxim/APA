def addIfNotExists(arr,el):
    for i in arr:
        if i == el:
            return
    arr.append(el)

def contains(arr,el):
    i = 0
    for i in arr:
        if i == el:
            return i
        else:
            i += 1
    return -1

