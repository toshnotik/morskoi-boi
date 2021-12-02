class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


a = Dot(1, 1)
b = Dot(3, 2)
c = Dot(1, 1)


aa = [Dot(1, 1), Dot(3, 5), Dot(3, 10), Dot(1, 5)]

print(a in aa)