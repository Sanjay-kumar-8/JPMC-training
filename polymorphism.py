#overriding
class A:
    a="This is a1"
    def a1(self):
        print("Hello world")
class B(A):
    b="This is b1"
    def a1(self):
        print("Welcome")
b=B()
b.a1()
