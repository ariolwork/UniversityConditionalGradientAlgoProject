# list with modification by need modules

class my_list:
    def __init__(self, a):
        self.list = a
    def __add__(self, other):
        return my_list([self.list[i]+other.list[i] for i in range(0, len(self.list))])
    def __sub__(self, other):
        return my_list([self.list[i]-other.list[i] for i in range(0, len(self.list))])
    def __neg__(self):
        return my_list([-self.list[i] for i in range(0, len(self.list))])
    def __getitem__(self, i):
        return self.list[i]
    def __len__(self):
        return len(self.list)
    def __str__(self):
        return self.list.__str__()
    def __mul__(self, a):
        return my_list([self.list[i]*a for i in range(0, len(self.list))])
    def __imul__(self, a):
        return my_list([self.list[i]*a for i in range(0, len(self.list))])
    def __rmul__(self, other):
        return self*other
    def __eq__(self, a):
        return my_list([self.list[i] == a.list[i] for i in range(0, len(self.list))])

class np:
    @staticmethod
    def all(a) -> bool:
        ansv = True
        for i in a:
            ansv = ansv and i
        return ansv
    @staticmethod
    def dot(a,b):
        answ = 0
        for i in range(0, len(a)):
            answ += a[i]*b[i]
        return answ
    @staticmethod
    def array(a):
        return my_list(a)
    
