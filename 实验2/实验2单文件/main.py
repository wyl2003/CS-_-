"""
@Description: 实验2
@Author: wyl2003
@Date: 2022-12-23 21:57:52
"""

def main():
    global courses_list
    global students_list
    courses_list,students_list=[],[]
    courses_file = open('courses.txt', 'r')
    i = 0
    while True:
        line = courses_file.readline().rstrip()
        if not line: #判断读到文件末尾
            break
        courses_list.append([])
        courses_list[i]=line.split(',')
        courses_list[i].append(courses_file.readline().rstrip())
        i += 1
    courses_file.close()

    students_file = open('students.txt', 'r')
    i = 0
    while True:
        line = students_file.readline().rstrip()
        if not line: 
            break
        students_list.append([])
        students_list[i]=line.split(',')
        t = int(students_file.readline())
        students_list[i].append(t)
        temp = []
        for count in range(t):
            temp.append(students_file.readline().rstrip())
        students_list[i].append(temp)
        i += 1
    students_file.close()

    menu()

def menu():
    print("-------------------------------------------------------------------------------------------\n\
The choice to maintain COURSEs information [add|remove|update|search|show]\n\
The choice to maintain STUDENTs information [insert|delete|modify|retrieve|display]\n\
The choice quit means to finish the program.[quit]\n\n\n")
    tmp = input('Please enter choice:')
    if tmp == 'add':
        add()
    elif tmp == 'remove':
        remove()
    elif tmp == 'update':
        update()
    elif tmp == 'search':
        search()
    elif tmp == 'show':
        show()
    elif tmp == 'insert':
        insert()
    elif tmp == 'delete':
        delete()
    elif tmp == 'modify':
        modify()
    elif tmp == 'retrieve':
        retrieve()
    elif tmp == 'display':
        display()
    elif tmp == 'quit':
        my_quit()
    else:
        print('Not a valid command - please try again.\n\n\n')

    menu()#回到菜单

def my_quit():
    global courses_list
    global students_list

    temp_courses= open('new_course.txt', 'w')
    s = ','
    for i in range(len(courses_list)):
        temp_courses.write(s.join(courses_list[i][0:5]))
        temp_courses.write('\n')
        temp_courses.write(courses_list[i][5])
        temp_courses.write('\n')

    temp_courses.close()

    temp_students= open('new_students.txt', 'w')
    k = '\n'
    for i in range(len(students_list)):
        temp_students.write(s.join(students_list[i][0:4]))
        temp_students.write('\n')
        temp_students.write(str(students_list[i][4]))
        temp_students.write('\n')
        temp_students.write(k.join(students_list[i][5]))
        temp_students.write('\n')

    print('\n\n-- Program Terminating --')
    quit()



#[insert|delete|modify|retrieve|display]
#["WuKong SUN","1766060102","m","Computer Science and Technology",2, ["31060103","31060104"]]
def display():
    print('========================================\nAll Students Information\n========================================')
    global students_list
    global courses_list
    for i in range(len(students_list)):
        print('----------------------------------------')
        print('Student Name: '+students_list[i][0])
        print('Student ID (Gender): '+students_list[i][1]+'('+students_list[i][2]+")")
        print('Major: '+students_list[i][3])
        count = students_list[i][4]
        print('Selected Courses ('+ str(count) +') :')
        if count != 0:
            for id in students_list[i][5]: #打印课程
                for j in range(len(courses_list)):
                    if courses_list[j][1] == id: 
                        break
                print('    '+ id +':'+courses_list[j][0])
    print('----------------------------------------\n========================================')

def  retrieve():
    global students_list
    global courses_list
    tmp = input('Please enter student ID: ')
    for i in range(len(students_list)+1):
        if i == len(students_list):
            print('Student (ID='+ tmp +') is not found in the students list.')
            return 0 #结束该函数
        if students_list[i][1] == tmp: 
            break
    print('\n\nStudent Name: '+students_list[i][0])
    print('Student ID (Gender): '+students_list[i][1]+'('+students_list[i][2]+")")
    print('Major: '+students_list[i][3])
    count = students_list[i][4]
    print('Selected Courses ('+ str(count) +') :')
    if count != 0:
        for id in students_list[i][5]:
            for j in range(len(courses_list)):
                if courses_list[j][1] == id: 
                    break
            print('    '+ id +':'+courses_list[j][0])

def insert():
    global students_list
    tmp = input('Please enter student ID: ')
    t = len(students_list)
    for i in range(t):
        if students_list[i][1] == tmp: 
            print('Course (ID='+ tmp +') already exists in the courses list.')
            return 0 
    students_list.append([])
    students_list[t].append(input('Please enter student name: '))
    students_list[t].append(tmp)
    gender = ''
    while gender != 'f' and gender!= 'm':
        gender = input('Please enter student gender(m/f): ')
    students_list[t].append(gender)
    students_list[t].append(input('Please enter student major:'))
    students_list[t].append(0)
    students_list[t].append([])
    print('Successfully inserted the Student (ID='+ tmp +') into the students list.')

def modify():
    global students_list
    global courses_list
    tmp = input('Please enter student ID: ')
    t = len(students_list)
    for i in range(t+1):
        if i == t:
            print('Student (ID='+ tmp +') is not found in the student list.')
            return 0 #结束该函数
        if students_list[i][1] == tmp: 
            break
    mod=input('Modify student (ID='+ tmp +') [major|enroll|drop]: ')
    if mod == 'major':
        students_list[i][3] = input('Please enter student major: ')
        print('Modified the major of Student (ID='+ tmp +').')
        print('----------------------------------------\n\n')
        print('\n\nStudent Name: '+students_list[i][0])
        print('Student ID (Gender): '+students_list[i][1]+'('+students_list[i][2]+")")
        print('Major: '+students_list[i][3])
        count = students_list[i][4]
        print('Selected Courses ('+ str(count) +') :')
        if count != 0:
            for id in students_list[i][5]:
                for j in range(courses_list):
                    if courses_list[j][1] == id: 
                        break
                print('    '+ id +':'+courses_list[j][0])

    elif mod == 'enroll':
        tmp_course = input('Please enter ID of course to be enrolled in: ')
        for k in students_list[i][5]: #个人课表里有没有
            if k == tmp_course: 
                print('Course (ID='+ tmp_course +') is already in the enrolled courses list.')
                return 0 #结束该函数
        for j in range(len(courses_list)+1): #找整个课表里有没有
            if j == len(courses_list):
                print('Course (ID='+ tmp_course +') is not found in the courses list.')
                return 0 #结束该函数
            if courses_list[j][1] == tmp_course: 
                break
        students_list[i][4]+=1
        students_list[i][5].append(tmp_course)
        print('Modified the information of Student (ID='+ tmp +').')
        print('----------------------------------------\n\n')
        print('\n\nStudent Name: '+students_list[i][0])
        print('Student ID (Gender): '+students_list[i][1]+'('+students_list[i][2]+")")
        print('Major: '+students_list[i][3])
        count = students_list[i][4]
        print('Selected Courses ('+ str(count) +') :')
        if count != 0:
            for id in students_list[i][5]:
                for j in range(len(courses_list)):
                    if courses_list[j][1] == id: 
                        break
                print('    '+ id +':'+courses_list[j][0])

    elif mod =='drop':
        tmp_course = input('Please enter ID of course to be dropped: ')
        for j in range(len(students_list[i][5])+1): #找选课表里有没有
            if j == len(students_list[i][5]):
                print('Course (ID='+ tmp_course +') is not found in the courses list.')
                return 0 #结束该函数
            if students_list[i][5][j] == tmp_course: 
                break
        del students_list[i][5][j]
        students_list[i][4]-=1
        print('Modified the information of Student (ID='+ tmp +').')
        print('----------------------------------------')
        print('\n\nStudent Name: '+students_list[i][0])
        print('Student ID (Gender): '+students_list[i][1]+'('+students_list[i][2]+")")
        print('Major: '+students_list[i][3])
        count = students_list[i][4]
        print('Selected Courses ('+ str(count) +') :')
        if count != 0:
            for id in students_list[i][5]:
                for j in range(len(courses_list)):
                    if courses_list[j][1] == id: 
                        break
                print('    '+ id +':'+courses_list[j][0])

    else:
        print('Not a valid command - returning to main menu.')

def delete():
    global students_list
    tmp = input('Please enter student ID: ')
    for i in range(len(students_list)+1):
        if i == len(students_list):
            print('Student (ID='+ tmp +') is not found in the students list.')
            return 0 #结束该函数
        if students_list[i][1] == tmp: 
            break
    del students_list[i]
    print('Successfully removed the Course (ID='+ tmp +') from the courses list.')



#[add|remove|update|search|show]
#["Academic English I","31060101","3","Liang ZHU-GE","8-102","Two hours each week-day."]
def show():
    print('========================================\nAll Courses Information\n========================================')
    global courses_list
    for i in range(len(courses_list)):
        print('----------------------------------------')
        print('Course Name: '+ courses_list[i][0])
        print('Course ID | Credits: '+ courses_list[i][1]+'|'+courses_list[i][2])
        print('Instructor Name: '+ courses_list[i][3])
        print('Address: '+ courses_list[i][4])
        print('Description: '+ courses_list[i][5])
    print('----------------------------------------\n========================================')

def search():
    global courses_list
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

def add(): 
    global courses_list
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

def update():
    global courses_list
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

def remove():
    global courses_list
    global students_list
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


main()