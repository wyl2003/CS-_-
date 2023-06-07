#[insert|delete|modify|retrieve|display]
#["WuKong SUN","1766060102","m","Computer Science and Technology",2, ["31060103","31060104"]]
def display(courses_list,students_list):
    print('========================================\nAll Students Information\n========================================')
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

def  retrieve(courses_list,students_list):
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

def insert(students_list):
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

def modify(courses_list,students_list):
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

def delete(students_list):
    tmp = input('Please enter student ID: ')
    for i in range(len(students_list)+1):
        if i == len(students_list):
            print('Student (ID='+ tmp +') is not found in the students list.')
            return 0 #结束该函数
        if students_list[i][1] == tmp: 
            break
    del students_list[i]
    print('Successfully removed the Course (ID='+ tmp +') from the courses list.')
