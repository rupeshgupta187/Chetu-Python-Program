class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{}, {}'.format(self.m1, self.m2)

s1 = Student(12, 54)
s2 = Student(56, 23)
print(s1)
print(s2)
if s1 > s2:
    print(f"{s1} is greater than {s2}")
else:
    print(f"{s2} is greater than {s1}")
