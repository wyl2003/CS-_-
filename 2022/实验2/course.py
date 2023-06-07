#[add|remove|update|search|show]
#["Academic English I","31060101","3","Liang ZHU-GE","8-102","Two hours each week-day."]
def show(courses_list):
    print('========================================\nAll Courses Information\n========================================')
    for i in range(len(courses_list)):
        print('----------------------------------------')
        print('Course Name: '+ courses_list[i][0])
        print('Course ID | Credits: '+ courses_list[i][1]+'|'+courses_list[i][2])
        print('Instructor Name: '+ courses_list[i][3])
        print('Address: '+ courses_list[i][4])
        print('Description: '+ courses_list[i][5])
    print('----------------------------------------\n========================================')

def search(courses_list):
    tmp = input('Please enter course ID: ')
    for i in range(len(courses_list)+1):
        if i == len(courses_list):
            print('Course (ID='+ tmp +') is not found in the courses list.')
            return 0 #结束该函数
        if courses_list[i][1] == tmp: 
            break
    print('Course Name: '+ courses_list[i][0])
    print('Course ID | Credits: '+ courses_list[i][1]+'|'+courses_list[i][2])
    print('Instructor Name: '+ courses_list[i][3])
    print('Address: '+ courses_list[i][4])
    print('Description: '+ courses_list[i][5])

def add(courses_list): 
    tmp = input('Please enter course ID: ')
    t = len(courses_list)
    for i in range(t):
        if courses_list[i][1] == tmp: 
            print('Course (ID='+ tmp +') already exists in the courses list.')
            return 0 
    courses_list.append([])
    courses_list[t].append(input('Please input course name: '))    
    courses_list[t].append(tmp)
    courses_list[t].append(input('Please enter course credits: '))
    courses_list[t].append(input('Please enter course instructor: '))
    courses_list[t].append(input('Please enter course address: '))
    courses_list[t].append(input('Please enter course description: '))
    print('Successfully added the Course (ID='+ tmp +') to the courses list.')

def update(courses_list):
    tmp = input('Please enter course ID: ')
    t = len(courses_list)
    for i in range(t+1):
        if i == t:
            print('Course (ID='+ tmp +') is not found in the courses list.')
            return 0 #结束该函数
        if courses_list[i][1] == tmp: 
            break
    print('Before updating, the course information:\n----------------------------------------')
    print('Course Name: '+ courses_list[i][0])
    print('Course ID | Credits: '+ courses_list[i][1]+'|'+courses_list[i][2])
    print('Instructor Name: '+ courses_list[i][3])
    print('Address: '+ courses_list[i][4])
    print('Description: '+ courses_list[i][5])
    print('----------------------------------------')
    courses_list[i][0] = input('Please input course name: ')
    courses_list[i][1] = tmp
    courses_list[i][2] = input('Please enter course credits: ')
    courses_list[i][3] = input('Please enter course instructor: ')
    courses_list[i][4] = input('Please enter course address: ')
    courses_list[i][5] = input('Please enter course description: ')
    print('Successfully updated the Course (ID='+ tmp +') to the courses list.')

def remove(courses_list,students_list):
    tmp = input('Please enter course ID: ')
    for i in range(len(courses_list)+1):
        if i == len(courses_list):
            print('Course (ID='+ tmp +') is not found in the courses list.')
            return 0 #结束该函数
        if courses_list[i][1] == tmp: 
            break
    for j in range(len(students_list)): #删除学生个人课表相关
        for k in students_list[j][5]:
            if tmp == k:
                students_list[j][5].remove(tmp)
                students_list[j][4]-=1
    del courses_list[i]
    print('Successfully removed the Course (ID='+ tmp +') from the courses list.')
