x = "global"

def f():
    def g():
        nonlocal x  # Python 3 only
        x = "g"
    x = "f"
    g()
    print(x)

f()
print(x)