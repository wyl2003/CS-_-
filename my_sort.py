def insertion_sort(alist): #插入排序 升序
    for i in range(1,len(alist)):
        tmp = alist.pop(i)
        for j in range(i):
            if tmp < alist[j]:
                alist.insert(j,tmp)
                break
            elif j == i-1:
                alist.insert(j+1,tmp)


def merge_sort(alist,mode = 0,x=[],y=[]): #归并排序算法 升序 递归
    if mode == 0: #分解模式
        if len(alist) == 1:
            return alist
        middle = len(alist) //2
        l = merge_sort(alist[:middle])
        r = merge_sort(alist[middle:])
        return merge_sort(alist,1,l,r)
    
    if mode == 1: #合并模式
        tmp =[]
        i,j = 0,0
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                tmp.append(x[i])
                i += 1
            else:
                tmp.append(y[j])
                j += 1
        tmp += x[i:]
        tmp += y[j:]
        return tmp