class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return 'Вы пытаетесь выстрелить за доску'

class BoardUsedException(BoardException):
    def __str__(self):
        return 'Вы уже среляли в эту клетку'

class BoardWrongShipException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cor_x = self.bow.x
            cor_y = self.bow.y

            if self.o == 0:
                cor_x += i

            elif self.o == 1:
                cor_y += i

            ship_dots.append(Dot(cor_x, cor_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid = False, size = 6):
        self.hid = hid
        self.size = size

        self.count = 0

        self.field = [['▒'] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        res = ''
        res += ' |1|2|3|4|5|6|'
        for i, row in enumerate(self.field):
            res += f'\n{i + 1}|' + '|'.join(row) + '|'

        if self.hid:
            res = res.replace('█', '0')
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contur(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cor = Dot(d.x + dx, d.y + dy)
                if not(self. out(cor)) and cor not in self.busy:
                    if verb:
                        self.field[cor.x] [cor.y] = '•'
                    self.busy.append(cor)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()

        for d in ship.dots:
            self.field[d.x] [d.y] = '█'
            self.busy.append(d)

        self.ships.append(ship)
        self.contur(ship)


b = Board()
b.add_ship(Ship(Dot(1, 1), 2, 1))
b.add_ship(Ship(Dot(5, 5), 1, 0))
print(b)

