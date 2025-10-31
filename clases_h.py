class T():
    def __init__(self, args):
        t = args
        self.t  = t
        print("clase T", self.t)
class A():
    def __init__(self, args):
        a = args
        self.a  = a
        print("clase A", self.a)
class Z():
    def __init__(self, args2):
        z = args2
        self.z  = z
        print("clase Z", self.z)
class X():
    def __init__(self, *arg3):
        x1,x2 = arg3
        self.x1 = x1
        self.x2 = x2
        print("clase X", self.x1,self.x2)
    
class B(A,Z, T, X):
    def __init__(self, *args4):
        a,z,t,x1,x2,b,c,d= args4
        self.b = b
        self.c = c
        self.d = d
        A.__init__(self, a)
        Z.__init__(self, z)
        T.__init__(self, t)
        X.__init__(self, x1,x2)
        print("clase B",self.b,self.c,self.d)
yo= B(3,4,5 ,6,7,8,9,10)