x="we are out side the scope"
print(x)
def fun1():
    x="we are inside a local scope"
    print(x)
def fun2():
    print(x)
def fun3():
    global x
    x="we are inside a local scope"

fun1()
fun2()
fun3()
print(x)
fun1()
fun2()
