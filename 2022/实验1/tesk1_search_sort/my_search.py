def sequential_search(elem, alist): #顺序查找
    count = 0

    for i in alist:
        if i == elem:
            return count
        count += 1
    return -1



def binary_search(elem, alist): #折半查找
    i = 0
    j = len(alist) - 1

    while i <= j :
        if alist[(i+j)//2] == elem:
            return (i+j) //2
        elif alist[(i+j)//2] < elem:
            i = (i+j) //2 + 1
        else:
            j = (i+j) //2 - 1
    return -1