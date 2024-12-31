# create a new file "Practice.txt" using Python 

# file = open("Practice.txt","w")
# data=file.write("Hi everyone\nwe are learning File I/O\n using Python\nI like programming in Python.")


# file.close()

# (2) replace Python to Java

# with open("Practice.txt","r") as f:

#     data = f.read()

# new_data=data.replace("Python","Java")
# print(new_data)

# with open("Practice.txt","w") as f:
#     f.write(new_data)

# (3) waf search if the word"learning" in file or not..

# def check_for_word():
#     word = "learning"

#     with open("Practice.txt","r") as f:
                
#                 data=f.read()

#                 if (word in data):
#                      print("found")
#                 else:
#                     print("Not Found")
# check_for_word()

# (4) waf to find which line of the file does the word"learning" occur first.
        # print 1  if word not found

# def check_for_line():
#     word = "learning"
#     data = True
#     line_num = 1

#     with open("Practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if (word in data):
#                 print(line_num)
#                 return
#             line_num += 1
#     return -1

# check_for_line()

# (5) for a containing numbers separated by comma,print the count even number

count = 0
with open("Practice.txt","r") as f:
    data=f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1
print(count)