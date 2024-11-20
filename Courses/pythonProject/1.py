str = input()
arr = list(map(float, str.split()))

x = arr[0]
y = arr[1]
x1 = arr[2]
y1 = arr[3]
x2 = arr[4]
y2 = arr[5]
r = arr[6]
s = arr[7]

# 0 -1 0 0 1 1 2 1

if x * x + y * y <= r * r:
    flag_c = 1
else:
    flag_c = 0

if ((x1 <= x <= x2) or (x1 >= x >= x2)) and ((y1 <= y <= y2) or (y1 >= y >= y2)):
    flag_s = 1
else:
    flag_s = 0

# print (flags, flagc)

if s == 0:
    if flag_c == 1 or flag_s == 1:
        print(True)
    else:
        print(False)
else:
    if flag_c == 1 and flag_s == 1:
        print(True)
    else:
        print(False)