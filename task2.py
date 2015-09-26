import json

stud_file = open('Students.json')
data_stud = json.load(stud_file)

teach_file = open('Teachers.json')
data_teach = json.load(teach_file)


teacher_name = 'Владимир Вышкин'.split(' ')  # input('Введите имя и фамилию учителя: ').split(' ')

students_list = []

for teacher in data_teach:
    if teacher_name[0] == teacher['name'] and teacher_name[1] == teacher['surname']:
        school = teacher['school']
        class_nums = teacher['class']

for student in data_stud:
    for class_num in class_nums:
        if student['class'] == class_num and student['school'] == school:
            students_list.append(' '.join([student['name'], student['middle_name'], student['surname']]))

print(students_list)


student_name = 'Иван Иванов'.split(' ')

for student in data_stud:
    if student['name'] == student_name[0] and student['surname'] == student_name[1]:
        school = student['school']
        st_class = student['class']

for teacher in data_teach:
    if teacher['school'] == school:
        for class_num in teacher['class']:
            if class_num == st_class:
                teacher_name2 = ' '.join([teacher['name'], teacher['middle_name'], teacher['surname']])

print(teacher_name2)


stud_file.close()
teach_file.close()