def f(s, *a):  # *args
    print(s)
    return sum(a)


print(f("0", 1, 2, 3))
print(f("0", 1, 2))

a = [1, 2, 3, 4, 5]
print(*a)


def g(s, **d):  # *kwargs
    print(s)
    print(d)
    for key in d:
        print(f"{key}: {d[key]}")


g("gsdgds", bds=532, jk="gsgds", d=[1, 3, "f"])


s = f"answer {a if 2 > 1 else a[1:2]} bool int"
print(s)
