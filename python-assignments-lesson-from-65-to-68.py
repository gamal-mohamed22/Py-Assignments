# ###python-assignments-lesson-from-65-to-68
#
# import os
# path = os.path.abspath(r"C:\Users\DELL\OneDrive\Desktop\py")
# open(f"{path}/assign.py","w")
# print(os.getcwd())
# print(path)
# sum = os.listdir(path)
# print(len(sum),"<= Folder objects")
# for n in range(1,51) :
#     if n == 25 :
#         txt = open(os.path.abspath(f"{path}/special-text.txt"), "w")
#     else:
#         txt = open(os.path.abspath(f"{path}/txt{n}.txt"),"w")
#         txt.write(f"Elzero Web School => {n}\n")
#         number = 50
#         while number > 40:
#             os.remove(fr"{path}\txt{number}.txt")
#             number -= 1
#         if n == 1 :
#             txt = open(os.path.abspath(f"{path}/txt{n}.txt"), "a")
#             txt.write("Appended => Elzero Web School\n"*50)
#             txt = open(os.path.abspath(f"{path}/txt{n}.txt"), "r")
#             sum1 = txt.readlines()
#             print(len(sum1), "<= Number Of Lines")
#             txt = open(os.path.abspath(f"{path}/txt{n}.txt"), "r")
#             sum2 = " ".join(sum1)
#             print(sum2.count(" "),"<= Number Of Words")
#             print(sum2.count("l"), "<= Number Of Char l")
#             txt = open(os.path.abspath(f"{path}/txt{n}.txt"), "r")
#             sum3 = len(txt.read())
#             print(f"{sum3} <= Number Of Chars ")







