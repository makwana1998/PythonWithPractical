# range() function return a sequence of numbers,strting from 0 by default,
#           increments by 1 ,and stop before a spicified number.

# seq = range(1,11)
# for i in seq:
#     print(i)

# print(range(11))

# for i in range(6):
#     print(i,end=" ")
#     # print()

# for i in range(1,6):
#     print(i,end=" ")
#     # print()

# for i in range(1,10,2):
#     print(i)

# print the 1 to 10 even number

for i in range(1,11):
    if(i %2 == 0):
        print("The even number is",i)