# find the maximum of three numbers (I assume this means the largest of the three?)
def max_num(x,y,z):
    return max(x,y,z)

print("max_num(3,2,7) = ", max_num(3,2,7))

# multiply all the numbers in a list

def mult_list(input):
    output = 1
    for i in input:
        output = output * i
    return output

print("mult_list([3,4,5]) = ", mult_list([3,4,5]))

# reverse a string

def rev_string(str):
    return ''.join(list(reversed(str)))

print('rev_string("Howdy") = ', rev_string("Howdy"))

# check whether a number falls in a given range

def num_within(num,start,end):
    if num >= start and num <= end:
        return True
    else:
        return False

print("num_within(3,2,4) = ", num_within(3,2,4))

# prints out the first n rows of Pascal's triangle

def pascal(n):
    print("I couldn't figure this out and the solution code makes sense when I check it. I could copy and paste that here but I figured this would get the same point across. Happy to erase this and copy paste solution code instead if that's what ya need.")

pascal(1)

# def pascal(n):
#     output = ""
#     while n > 0:
#         output.join(" 1")
#         print(output)
#         n -= 1

# pascal(4)