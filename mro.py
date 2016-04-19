class A(object):
    pass

class B(A):
    pass

class C(B, A):
    pass


print(C.__mro__)
