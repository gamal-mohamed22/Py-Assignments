########python-assignments-lesson-from-56-to-59[1]#############

# def calculate(num1, num2, operatin="add"):
#     #####You Can write operatin full name or First letter or Symbol all must be in Doule Quotes Like "+" #####
#     operatin = operatin.lower()
#     if operatin == "add" or operatin == "a" or operatin == "+":
#         print(num1+num2)
#     elif operatin == "substract" or operatin == "s" or operatin == "-":
#         print(num1-num2)
#     elif operatin == "multiplay" or operatin == "m" or operatin == "*":
#         print(num1*num2)
#     else:
#         print("No opertation Found")
#
#
# calculate(12, 13, "-")
# calculate(12, 13, "ADd")
# calculate(12, 13, "MULTIPLAY")


########python-assignments-lesson-from-56-to-59[2]#############

# def addition(*nums):
#     m = 0
#     for num in nums:
#         if num == 5:
#             num = 5
#             m = m-num
#         elif num == str(num):
#             print("Please enter intger number !")
#         elif num == 10:
#             continue
#         else:
#             m = m+num
#
#     else:
#         print(m)
#
#
# addition(1, 4, 4, 46, 6, 10, 10, 5, 5, 4, 5, 4,5,5,10,7,5,1,10)


#######python-assignments-lesson-from-56-to-59[3]#############
# def char(name, *skills):
#     print(f"hello {name} Your Skills is : ")
#     if len(skills) == 0:
#         print("None")
#     else:
#         for skill in skills:
#             print(f"{skill}")
#
#
# char("Gamal")
# char("Osama", "HTML", "CSS", "JS", "Python")


########python-assignments-lesson-from-56-to-59[4]#############
# def welcoming(name="defaultName",age="defaultAge",country="defaultCountry"):
#     print(f"hello {name} Your age is {age} Years old , You are from {country}")
#
# welcoming("Gamal",20,"Egypt")
# welcoming()


########python-assignments-lesson-from-60-to-64[1]#############
# def get_score(**subjects):
#     for student_key, student_value in subjects.items():
#         print(f"{student_key} => {student_value}")
#
#
# get_score(Math=90, Science=80, Language=70, Sports=50)
# get_score(Logic=70, Problems=60)


########python-assignments-lesson-from-60-to-64[2]#############
# def get_people_scores(name="defaultName", **skills):
#     if name == "defaultName":
#         print()
#     elif len(skills) == 0:
#         print(f"hello {name} You Have No Scores To Show")
#     else:
#         print(f"hello {name} This Is Your Score Table:")
#     for student_key, student_value in skills.items():
#         print(f"{student_key} => {student_value}")
#
#
# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")


########python-assignments-lesson-from-60-to-64[3]#############

# scores_list = {
#
#     "Math": 90,
#     "Science": 80,
#     "Language": 70
# }


# def Score(name="defaultName", **skills):
#     if name == "defaultName":
#         pass
#     elif len(skills) == 0:
#         print(f"hello {name}  You Have No Scores To Show :")
#     else:
#         print(f"hello {name} This is Your Score table :")
#     for student_key, student_value in skills.items():
#         print(f"{student_key} => {student_value}")
#
#
# Score("Osama", **scores_list)
# Score("Osama")
# Score(**scores_list)

