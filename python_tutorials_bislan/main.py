# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def f(x):
    return x**2 > 20

def g(x):
    x = x + 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Неизменяемые
    x = 64
    x = 43
    y = 10.9
    w = (1, 2, 3)
    w = (1, 2, 3, 4)
    # w[1] = 6 - Нельзя
    s = 'fmgmefkds'
    # s[1] = '1' - нельзя
    s = s[1:]

    x = 10
    y = x
    print(x, y, id(x), id(y))

    y = 5
    print(x, y, id(x), id(y))


    # Изменяемые
    #      0  1  2  3  4
    arr = [1, 2, 3, 4, 5]
    arr1 = list((1, 2, 3, 4))

    print(arr[-2:-1])
    print(s[::-1])
    d = {'a': 1, 'b': 2}
    d1 = dict()
    # Ключи - неизменяемые типы

    set1 = {1, 2, 3, 4, 4}
    set2 = (1, 2, 3, 4)
    print(set1)
    arr2 = arr
    print(id(arr2), id(arr))
    arr.append(10)
    print('arr2 = ', arr2)

    arr3 = arr.copy()
    arr.append(11)
    print('arr3 = ', arr3)

    print('\n\n\n')
    b = [i**2 for i in range(10)]
    c = [i for i in range(0, 10, 2)]
    #d = [i for i in range(10) if i % 2]
    e = [i if i % 2 else i**2 for i in range(10)]

    arr4 = [i for i in range(10) if f(i)]
    # print(b, e, arr4)

    #for x in arr:
    #    print(x)

    for x in d:
        print(x)

    for x in set1:
        print(x)

    arra = [x for x in arr if x % 2]
    print(arra)

    x = 4
    y = x
    a = g(x)
    print(a is None)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
