class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def funcion1(self):
        print("A")
        def funcion3():
            print("C")
    def funcion2(self):
        print("B")
        self.funcion1()
def funcion4():
    print("D")