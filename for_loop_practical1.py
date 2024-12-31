# (1) print the elements of the following list using loop.

# l1 = [1,4,9,16,25,36,49,64,81,100]

# for i in l1:
#     print(i,end=" ")

# (2) search for a number of x in tuple using loop.

tup1 = (1,4,9,16,25,36,49,64,81,100,49)

x = 49
idx = 0

for i in tup1:

    if (i == x):
        print("Number found at :",idx)
        break
    idx += 1
        


