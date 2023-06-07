import random
import ex1.tesk1_search_sort.my_search as my_search
import ex1.tesk1_search_sort.my_sort as my_sort
alist = []
for i in range(100):
    alist.append(random.randint(0,99)) #0到99中随机整数

alist_1 = alist

x = int(input('输入要搜索的数：'))
t = my_search.sequential_search(x, alist)
if t == -1:
    print("Not found!")
else:
    print("Found "+str(x)+" in the position "+str(t))

my_sort.insertion_sort(alist)
t = my_search.binary_search(x, alist)
if t == -1:
    print("Not found!")
else:
    print("Found "+str(x)+" in the position "+str(t))

tmp_list = my_sort.merge_sort(alist_1)
t = my_search.binary_search(x,tmp_list)
if t == -1:
    print("Not found!")
else:
    print("Found "+str(x)+" in the position "+str(t))