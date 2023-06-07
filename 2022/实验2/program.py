import course
import student


"""
@Description: 实验2
@Author: wyl2003
@Date: 2022-12-23 21:57:52
"""

def main():
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

    menu(courses_list,students_list)

def menu(courses_list,students_list):
    print("-------------------------------------------------------------------------------------------\n\
The choice to maintain COURSEs information [add|remove|update|search|show]\n\
The choice to maintain STUDENTs information [insert|delete|modify|retrieve|display]\n\
The choice quit means to finish the program.[quit]\n\n\n")
    tmp = input('Please enter choice:')
    if tmp == 'add':
        course.add(courses_list)
    elif tmp == 'remove':
        course.remove(courses_list,students_list)
    elif tmp == 'update':
        course.update(courses_list)
    elif tmp == 'search':
        course.search(courses_list)
    elif tmp == 'show':
        course.show(courses_list)
    elif tmp == 'insert':
        student.insert(students_list)
    elif tmp == 'delete':
        student.delete(students_list)
    elif tmp == 'modify':
        student.modify(courses_list,students_list)
    elif tmp == 'retrieve':
        student.retrieve(courses_list,students_list)
    elif tmp == 'display':
        student.display(courses_list,students_list)
    elif tmp == 'quit':
        my_quit(courses_list,students_list)
    else:
        print('Not a valid command - please try again.\n\n\n')

    menu(courses_list,students_list)#回到菜单

def my_quit(courses_list,students_list):

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

main()