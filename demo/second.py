class A:

    def __init__(self, a):
        self.a = a

    def func_a(self):
        print(self.a)


class B(A):

    def func_b(self):
        print(self.a + 'bbbb')


class C(B):

    def func_c(self):
        self.func_b()

    def func_d(self):
        self.func_a()


if __name__ == '__main__':
    c = C('111')
    c.func_c()
    c.func_d()
