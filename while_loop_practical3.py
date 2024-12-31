#  (1) print the elements of the following list using a loop.

# nums=[1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print((nums[idx]))
    
#     idx += 1


# (2) wap to find sum of first n number using while loop.

# n1 = int(input("Enter the first Number : "))
# n2 = int(input("Enter the secound Number : "))

# n = 10
# sum = 0
# i = 1

# while i<=n:
#     sum += i
#     i += 1

# print("Total sum is :=",sum)



# (3) wap find the factorial  of first n numbers.using while loop

# n = 5
# fact = 1
# i = 1
# while i<=n:
#     fact *= i
#     i +=1
# print("Factoreal is = ",fact)


# using for loop factoreal

n = 5
fact = 1
for i in range(1,6):
    fact *=i
print("The factoreal is =",fact)
    
