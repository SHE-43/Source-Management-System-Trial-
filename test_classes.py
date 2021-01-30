import types

def foo():
    print ("foo")
a = 100
class A:
    a = 1
    def bar( self ):
        print( "bar")

    def assigner(self, cls):
        a = 2 # 
        cls.a = 3
        self.age = 55 # even if within a method, the object's instance value can be changed.

def fooFighters( self ):
    print( "fooFighters")


a2 = A()
a2.m = types.MethodType(fooFighters, a2)
a2.assigner(foo)
print(a2.age)
print(a2.a)
print(foo.a)
print(a2.a)
print(a)