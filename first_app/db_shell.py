# exec(open(r"G:\class\B6\Django\first_project\first_app\db_shell.py").read())
# from first_app.models import Student
# from first_app.models import Student_info

# stud_all_data = Student.objects.all()   # object  ORM
# print(stud_all_data.query)

# first_studs = Student.objects.first()   
# print(first_studs.__dict__)

# data = Student.objects.filter(id__gte =3)     #queryset-----list[]------index[0]
# print(data)

# data = Student.objects.filter(id=5)      # if there is no data then filter give emplty queryset
# print(data)

# for i in data:
#     print(i)

# try:
#     single_data = Student.objects.get(id=4)   # if there id no data ten raise exception
#     # print(single_data)
# except Student.DoesNotExist:
#     print("No data")

# single_data =Student.objects.get(id=1)
# print(single_data.__dict__)

# single_data = Student.objects.get(id=4)
# single_data.name = "DDD"
# single_data.save()         #need to save changs   like commit()
# print(single_data)

# def inc_mark():
#     all_data = Student.objects.all()
#     # print(all_data)
#     for stud in all_data:
#         # print(stud)
#         stud.marks += (stud.marks*5/100)
#         if stud.marks <= 100:       #  105 <= 100
#             stud.save()
#         else:
#             continue
# inc_mark()  

#single_student_details
# S1 = Student.objects.get(id=1)
# res = S1.get_stud_details()
# print(res)

#All student_detalis
# Student.get_all_stud_details()

#Avrage marks of all student marks
# res = Student._avg_of_all_stud_marks()
# print(res)

#Average of marks using REDUCE
# res = Student.avg_of_stud_marks_using_reduce()
# print(res)

# res = Student.avg_of_stud_marks_using_lamda_and_reduce()
# print(res)

#Delete single Student
# res = Student.delete_single_student()
# print(res)


#Student name stet with "A"
# Student.get_stud_name_start_with_A()


# print student having subject Math
# Student.get_stud_according_subject("Math")

# print marks of all student having subject "Eng" 
# res = Student.get_stud_mark_according_sub("Math")
# print(res)

#print student class according marks
# Student.get_stud_class_acoording_marks()


#print student according null address
# Student.get_Stude_having_null_address()


# all_Stud_of_Student_info = Student_info.objects.all()
# print(all_Stud_of_Student_info)



# all_Stud = Student.objects.all()
# # print(all_Stud)
# def import_data_from_student_info_to_student():

#     all_Stud_of_Student_info = Student_info.objects.all()

#     for stud in all_Stud_of_Student_info:
#     # print(stud)
#         a = Student(name =stud.name,marks=stud.marks,subject=stud.subject,address=stud.address,age=stud.age,is_active=stud.is_active)
#         print(a)
#         a.save()


# # import_data_from_student_info_to_student()

# print(Student.inactive_objects.all())
# print(Student.active_objects.all())
# print(Student.objects.all())



