

with open('file_study/student_details.csv') as file:
    student_list=file.readlines()
    file.close()
student_list=[student.strip() for student in student_list[1:]]

for student in student_list:
     details=student.split(',')
     name=details[0]
     age=details[1]
     course=details[2]
     clg=details[3]
     print(f"{name} of age {age} studying {course} in {clg}")

