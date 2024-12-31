# import os
# os.remove("sample1.txt")

with open("sample1.txt","w") as f:
    data = f.write("My first file...")
    print(data)