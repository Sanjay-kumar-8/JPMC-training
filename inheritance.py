class A:
    a="This is a1"
    def a1(self):
        print("This is class A")

class B(A):
    b="This is b1"
    def b1(self):
        print("This is class B")
class C(B):
    c="This is c1"
    def c1(self):
        print("This is class C")
class D(B,A):
    d="This is d1"
    def d1(self):
        print("This is class D")
class F:
    a="This is a1 of class F"
    def a1(self):
        print("This is class F")
class G(A,F):
    g="Hello"
    def g1(self):
        print("This is class G")


a=A()
print(a.a)
a.a1
