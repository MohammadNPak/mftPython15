
# numbers
#     bool     True False
#                1   0
#     int
#     float
#     complex

# str
#     ""
#     ''

# a="-2.2a"
# print(a,type(a))
# b = float(a)
# print(b,type(b))


# a = input("please enter your age: ")
# a= int(a)
# print(a,type(a))


# <           a = 22 != 3          
# >
# <=
# >=
# ==
# !=




# weight= float(input("weight (kg): "))
# height= float(input("height (m): "))
# gender = input("gender: ")
# if gender == "man":
#     gender=True
# else:
#     if gender=="woman":
#         gender=False

# bmi = weight / (height**2)
# #   => Underweight  
# if bmi <= 18.5:
#     print("Underweight")
# else:
#     if bmi < 24.9:
#         print("Normal weight")
#     else:
#         if bmi < 29.9:
#             print("Overweight")
#         else:
#             print("Obesity ")


# if    شرط  :
#     دستورات1
#     دستورات2
#     دستورات3
#     ...


# روش اول
# weight= float(input("weight (kg): "))
# height= float(input("height (m): "))
# bmi = weight / (height**2)
# gender = input("gender: ")
# if gender == "man":
#     gender=True
# else:
#     if gender=="woman":
#         gender=False

# if gender:
#     if bmi <= 18.5:
#         print("Underweight")
#     else:
#         if bmi < 24.9:
#             print("Normal weight")
#         else:
#             if bmi < 29.9:
#                 print("Overweight")
#             else:
#                 print("Obesity ")
# else:
#     if bmi <= 19.5:
#         print("Underweight")
#     else:
#         if bmi < 25.9:
#             print("Normal weight")
#         else:
#             if bmi < 30.9:
#                 print("Overweight")
#             else:
#                 print("Obesity ")




# روش د وم
# weight= float(input("weight (kg): "))
# height= float(input("height (m): "))
# gender = input("gender: ")
# bmi = weight / (height**2)
# if gender == "man":
#     gender=True
# else:
#     if gender=="woman":
#         gender=False
# if gender:
#     gender_factor =1
# else:
#     gender_factor =0 

# if bmi <= 18.5+gender_factor:
#     print("Underweight")
# else:
#     if bmi < 24.9+gender_factor:
#         print("Normal weight")
#     else:
#         if bmi < 29.9+gender_factor:
#             print("Overweight")
#         else:
#             print("Obesity ")


# روش سوم
weight= float(input("weight (kg): "))
height= float(input("height (m): "))
gender = input("gender: ")
bmi = weight / (height**2)
if gender == "man":
    gender_factor =1
else:
    gender_factor =0
if bmi <= 18.5+gender_factor:
    print("Underweight")
else:
    if bmi < 24.9+gender_factor:
        print("Normal weight")
    else:
        if bmi < 29.9+gender_factor:
            print("Overweight")
        else:
            print("Obesity ")


# x       y       x and y     x or y      not x  
# True    True    True        True        False  
# True    False   False       True        False  
# False   True    False       True        True   
# False   False   False       False       True

