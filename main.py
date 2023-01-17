# Online Python - Крестики-нолики
field = [['-']*4 for _ in range(4)] 

# Создаем игровое поле 4х4 сверху цифры, по вертикали буквы
def show_field (f):
    print ('  1 2 3 4')
    num = 'A B C D'
    for row,i in zip(field,num.split()):
        print (f"{i} {' '.join (str(j) for j in row)}")

# Проверяем ввод координат пользователем, переводим буквенное обозначение в координату
def users_input (f):
    while True:
        place = input ('Введите координат :').split()
        if len(place) !=2:
            print ('Введите 2 координаты через пробел')
            continue
        if not place[0].isalpha():
            print ('Первый знак координат должен быть буквой')
            continue
        if not place[1].isdigit():
            print ('Второй знак координат должен быть цифрой')
            continue
        
        x = int(ord(place[0]))-65
        y = int(place[1])-1
        print (x, y) # Для контроля правильности координат
        
        if not (y>=0 and y<4):
            print ('Вышли из диапазона')
            continue
        if f[x][y] !='-':
            print ('Клетка занята')
            continue
        break
    return x,y

# Функция проверки победителя с учетом размерности 4х4, побеждает тот, кто заполнит ряд из 4 символов
def win_v1 (f, user):
    def check_line (a1, a2, a3, a4, user):
        if a1 == user and a2 == user and a3 == user and a4 == user:
            return True
    for n in range (3):
        if check_line (f[n][0], f[n][1], f[n][2], f[n][3], user) or \
        check_line (f[0][n], f[1][n], f[2][n], f[3][n], user) or \
        check_line (f[0][0], f[1][1], f[2][2], f[3][3], user) or \
        check_line (f[0][3], f[1][2], f[2][1], f[3][0], user):
            return True
    return False

# Выполнение программы, ничья возможна, если все 16 клеток заполнены, и никто не выиграл
count = 1
while True:
    if count%2==0:
        user = 'O'
    else:
        user = 'X'
    show_field (field)
    print ('Ход номер:', count)
    x,y = users_input (field)
    field [x][y] = user
    if count ==16:
        print ('Ничья')
        break
    if win_v1 (field, user):
        show_field (field)
        print ('Выиграл игрок:', user)
        break
    count +=1
