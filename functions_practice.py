def hello():
    print("Hello human!")

def pack(x,y,z):
    list = [x,y,z]
    return list

def eat_lunch(list):
    if list:
        is_first = True
        for i in list:
            if is_first:
                is_first = False
                print(f"First I eat {i}")
            else:
                print(f"Next I eat {i}")
    else:
        print("My lunchbox is empty!")


hello()
lunch_box = pack("a PB&J","an apple", "a cookie")
print(lunch_box)
eat_lunch(lunch_box)