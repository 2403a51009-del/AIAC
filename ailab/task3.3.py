class Emp:
    def __init__(self, n, s): self.n, self.s = n, s
    def inc(self, p): self.s += self.s * p / 100
    def pr(self): print(f"emp: {self.n} salary: {self.s}")

e1 = Emp("pranay", 1000); e1.inc(10); e1.pr()
