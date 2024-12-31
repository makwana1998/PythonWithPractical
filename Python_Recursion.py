# When a function  calls itself repeatedly..

# def show(n): # recursive function

#     if (n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def fact(n):

    if (n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(0))