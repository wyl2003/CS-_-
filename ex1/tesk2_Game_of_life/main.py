import random

def instruction(): #介绍
    print("Welcome to Conway's game of Life.\n\
This game uses a grid of size 20 by 60 in which \n\
each cell can either be occupied by an organism or not. \n\
The occupied cells change from generation to generation \n\
according to the number of neighboring cells which are alive.")


def initialize(): #初始化网格
    global gird
    gird = [[0 for i in range(-1,19)]for j in range(-1,59)]
    for i in range(-1,19): #行
        for j in range(-1,59): #列
            gird[j][i] =  random.randint(0,1)


def printState(): #打印状态
    global gird
    for i in range(60):
        tmp = ''
        for j in range(20):
            if gird[i][j] == 1:
                tmp=tmp + '*'
            elif gird[i][j] == 0:
                tmp=tmp + ' '
        print (tmp)


def updateState(): #更新状态
    global gird
    for j in range(-1,19):
        for i in range(-1,59):
            if gird[i][j] == 1:
                if neighbor_count(i,j) <= 1:
                    gird[i][j] = 0
                elif neighbor_count(i,j) >= 4:
                    gird[i][j] = 0
            if gird[i][j] == 0:
                if neighbor_count(i,j) == 3:
                    gird[i][j] = 1


def neighbor_count(row, col): #8格邻居统计
    global gird
    sum = 0
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]
    for i in range(8):
        x = row + dx[i]
        y = col + dy[i]
        try: #扫描到网格外时当做异常处理
            sum += gird[x][y]
        except:
            pass
    return sum


def user_say_yes(): #要求用户输入
    while True:
        tmp = input("继续模拟?(Y/N)")
        if tmp == "Y" or tmp == "y":
            return True
        if tmp == "N" or tmp == "n":
            return False


def main():
    instruction()#介绍
    initialize() #初始化网格
    printState() #打印状态
    t = user_say_yes() #要求用户输入
    while t:
        updateState() #更新状态
        printState() #打印状态
        t = user_say_yes() #要求用户输入


main()