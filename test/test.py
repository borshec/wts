class MyList():
    def __init__(self, data=[]):
        self.data = list(data)

    def __add__(self, other):
        c = []
        c.extend(self.data)
        c.extend(other)
        return MyList(c)

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return MyList(self.data[item])

    def __setitem__(self, key, value):
        self.data[key] = value

    def append(self, obj):
        self.data.append(obj)

    def sort(self):
        self.data.sort()

if __name__ == "__main__":
    a = ['a', 1, 'b', 2]
    b = ['c', 3, 'd', 4]
    c = ['e', 5, 'f', 6, 'j', 7]
    L1 = MyList()
    L2 = MyList(a)
    L3 = MyList(c)
    print(L2)
    print(L1, L2)
    print(L2 + L3)
    L2[1]='Z'
    print(L2)
    L2.append('Y')
    print(L2)
    print(L2[1:3])
    print(L2[2])
    L4 = MyList(("a", "c", "b"))
    L4.sort()
    print(L4)