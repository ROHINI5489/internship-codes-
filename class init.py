class A:
    def __init__(self):
        self.b=self.B()
        self.c=self.b.C()
        self.c.fan()
class B:
        def __init__(self):
            pass
    
        class C:
            def __init__(self):
                print("c")
            def fan(self):
                print("fan run")
                
A()