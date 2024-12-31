# (1) waf to print  the length of a list.(list is the parameter)

def find_length_list(list):
    return(len(list))

a = find_length_list([1,2])
print(a)


# (2) waf to print elements of a list in a singl line.(list in the parameter)..

def print_list_singl_line(list):
    for item in list:
        print(item,end=" ")

print_list_singl_line(['apple','banana','cherry','watermelon'])

# (3) waf to the find of factorial of n.(n is the parameter)

def find_factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact *=i

    print(fact)

find_factorial(5)


# waf to convert USD to INR...

def converter(usd_value):
    inr_value = usd_value * 85.610
    print(usd_value,"USD =",inr_value,"INR")

converter(10)



