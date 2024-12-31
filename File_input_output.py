# Python can be used to perform operation on a file(read & write data).

# Types of all files
# (1)--> Text files:-->.txt,.docx,.log,etc.
# (2)--> Binary files:--> .mp4,.mov,.png,.jpeg,etc

# file = open("Python.txt","r")

# data=file.read()
# print(type(data))
# print(data)

# file.close()

# singl line read
# file = open("Python.txt","r")
# line1=file.readline()
# print(line1)

# line2=file.readline()
# print(line2)
# file.close()


# # new file create
# f = open("sample.txt","w")
# data = f.write("This is new File")
# f.close()


# using with syntax

# with open ("Python.txt","r") as f:
    
#     data=f.read()
#     print(data)

# # using write mode

# with open ("sample.txt","w+") as file:
    
#     file.write("This is simple File and used to simple")
    
# new file creat

f = open("sample1.txt","w")
f.write("Hello world!")
f.close()