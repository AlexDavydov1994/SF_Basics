def win(polygon):
    if any([all(x == 'x' for x in polygon[0]), all(x == 'x' for x in polygon[1]), all(x == 'x' for x in polygon[2]),
            all(polygon[x][0] == 'x' for x in range(3)), all(polygon[x][1] == 'x' for x in range(3)),
            all(polygon[x][2] == 'x' for x in range(3)),
            all(polygon[x][x] == 'x' for x in range(3)), all(polygon[2 - x][x] == 'x' for x in range(3))]):
        return 'win1'
    elif any([all(x == 'o' for x in polygon[0]), all(x == 'o' for x in polygon[1]), all(x == 'o' for x in polygon[2]),
              all(polygon[x][0] == 'o' for x in range(3)), all(polygon[x][1] == 'o' for x in range(3)),
              all(polygon[x][2] == 'o' for x in range(3)),
              all(polygon[x][x] == 'o' for x in range(3)), all(polygon[2 - x][x] == 'o' for x in range(3))]):
        return 'win2'
    else:
        return 'win12'


def printPoly(polygon):
    print('  0 1 2')
    print('0', *polygon[0])
    print('1', *polygon[1])
    print('2', *polygon[2])

def check_input(a):
    if len(a) != 2:
        print('Нужно ввести 2 координаты')
        return 0
    c1, c2 = map(int, a)
    if 0 > c1 or c1 > 2 or 0 > c2 or c2 > 2:
        print('Введите координаты от 0 до 2')
        return 0
    else:
        return 1
def turn(polygon, step):
    while True:
        if step == 0:
            a=input('Ход 1-ого игрока: Введите коордитнаты клетки куда поставить крестик').split()
            if check_input(a):
                c1, c2 = map(int, a)
                if polygon[c1][c2] == '-':
                    polygon[c1][c2] = 'x'
                    yield polygon
                else:
                    print('Эта клетка уже занята, введите другую')
        else:
            a = input('Ход 2-ого игрока: Введите коордитнаты клетки куда поставить нолик').split()
            if check_input(a):
                c1, c2 = map(int, a)
                if polygon[c1][c2] == '-':
                    polygon[c1][c2] = 'o'
                    yield polygon
                else:
                    print('Эта клетка уже занята, введите другую')


print('Правила игры:\n1)Игроки ходят по очереди. Первый ход делает игрок, который играет крестиками.\n2)Для хода введите 2 координаты(0,1,2) через пробел(первая координата, это номер строки, вторая номер столбца.\nУдачной игры.')
poly = [['-' for i in range(3)] for j in range(3)]
step = 0
print('Начало игры.')
printPoly(poly)
while ('-' in poly[0] or '-' in poly[1] or '-' in poly[2]) and (win(poly) != 'win1' and win(poly) != 'win2'):
    next(turn(poly, step))
    if step == 0:
        step = 1
    else:
        step = 0
    printPoly(poly)
if win(poly) == 'win1':
    print('Поздравляю игрок №1. Вы выиграли!\nИгрок №2, не расстраивайся в следющий раз победишь!')
elif win(poly) == 'win2':
    print('Поздравляю игрок №2. Вы выиграли!\nИгрок №1, не расстраивайся в следющий раз победишь!')
else:
    print('Ничья, победила дружба!')

