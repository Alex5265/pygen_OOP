# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4


from enum import Flag

class Color(Flag):
    RED = 1
    GREEN = 2
    BLUE = 4


combined1 = Color.RED | Color.GREEN
combined2 = Color.RED | Color.GREEN | Color.BLUE

print(combined1)
print(combined2)