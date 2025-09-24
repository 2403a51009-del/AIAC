class Student:
    def __init__(self, n, a, m1, m2, m3):
        self.n = n
        self.a = a
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def details(self):
        print("Name:", self.n, "Age:", self.a)
    def total(self):
        return self.m1 + self.m2 + self.m3
# input
s1 = Student("Ravi", 20, 85, 90, 78)
s2 = Student("Anita", 19, 88, 76, 92)

s1.details()
print("Total Marks:", s1.total())
print()
s2.details()
print("Total Marks:", s2.total())