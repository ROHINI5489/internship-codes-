class ECE:
    def __init__(self,marks):
        self.markst=marks
    def total(a,b,c):
        print(a.marks,b.marks,c.marks,a.marks+b.marks+c.marks)
    def getback(self):
        print(self.marks)
nawaz=ECE(45)
malli=ECE(56)
rohini=ECE(95)
ECE.total(nawaz,malli,rohini)