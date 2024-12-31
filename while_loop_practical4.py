# search for a number x in this tuple using loop

tup1 = (1,4,9,16,25,36,49,64,81,100)

x = 81
i = 0 

while i < len(tup1):
    
    if (tup1[i]) == x:

        print("Found at idx" , i)

    i += 1