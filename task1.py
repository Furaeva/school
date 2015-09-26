import json

stud_file = open('Students.json')
data_stud = json.load(stud_file)

teach_file = open('Teachers.json')
data_teach = json.load(teach_file)

student_names = [student["name"] for student in students]

print('Имена всех учеников: ', student_names)


tchname_list = []

for dictionary in data_teach:
    tchname_list.append(dictionary['name'])

print(tchname_list)


st_in_class_list = []

class_num = input('Введите нормер и букву класса: ')

for dictionary in data_stud:
    if dictionary['class'] == class_num:
        st_in_class_list.append(dictionary['name'])

if st_in_class_list:
    print(st_in_class_list)
else:
    print("Учеников из этого класса нет")


schools_list = []

for dictionary in data_stud:
    schools_list.append(dictionary['school'])

print(list(set(schools_list)))


surnames = []

for dictionary in data_stud:
    surnames.append(dictionary['surname'])

while surnames:
    surname = surnames.pop(0)
    if surname in surnames:
        print("Однофамильцы: ", surname)


stud_file.close()
teach_file.close()