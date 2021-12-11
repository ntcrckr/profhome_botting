a = 0
b = "1"
# c = "1.1"
# d = int(c)

#

try:
    print(a + b)
except TypeError:
    print(str(a) + str(b))

a = [1, 2, 3]
s = set(a)
t = tuple(s)
print(a, s, t)

# Traceback (most recent call last):
#   File "C:\Users\lehap\Desktop\prog\profhome_botting\testing_exceptions\test_0.py", line 7, in <module>
#     print(a + b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
