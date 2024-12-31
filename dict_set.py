# d = {
#     1:"one",
#     2:"two",
#     3:"three"
# }

# print(d)

# dict method most used

# (1) keys()
# (2) values()
# (3) items()
# (4) get()
# (5) update()


# set{} methods 

# (1) add()
# (2) remove()
# (3) clear()
# (4) pop()
# (5) union()
# (6) intersection()

# set1 = {"apple","Banana","Cherry"}
# set2 = {"watermelon","Banana","pineple"}

# # new_set = set1.union(set2)
# new_set = set1.intersection(set2)
# print(new_set)


# practical 
# (1) store following word in python dictionary
# d1 =    {
#             "table": ["a piece of furniture","list of fact & figures"],
#             "cat":"a small Animal",
#             }
# print(d1)

# (2) wap you are given a list of subjects for students. Assume one classroom is required for 1 subject .
#       how many classroom are needed by all student.

# subjects = {
#     "python","java","c++","python","javascript","java","python",
#     "c++","c","java"
# }

# print(len(subjects))

# (3) 

marks = {}

x = int(input("Enter phy : "))
marks.update({"phy":x})
x = int(input("Enter math : "))
marks.update({"math":x})
x = int(input("Enter chem : "))
marks.update({"chem":x})

print(marks)

