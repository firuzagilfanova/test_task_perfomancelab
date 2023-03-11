import sys, random, os

# функция для получения рандомной карты
def randomcard():
    suits = ['R', 'G', 'B', 'W']
    while True:
        card = random.choice(suits) + str(random.randint(1, 10))
        if card not in cards_on_table:
            cards_on_table.append(card)
            return card

# функция для проверки входных значений
def check():
    if N > 40:
        print("Ошибка: Количество карт больше количества карт в колоде")
        raise SystemExit
    if N < C:
        print("Ошибка: Карт меньше чем игроков")
        raise SystemExit
    if N % C != 0:
        print("Ошибка: Количетсво карт не делится на количество игроков")
        raise SystemExit

# функция для проверки на пустой файл
def check_file():
    if os.stat("players.txt").st_size == 0:
        print("Ошибка: Карты не выданы игрокам, используйте команду start")
        raise SystemExit


if sys.argv[1] == 'start' or sys.argv[1] == 'Start':
    cards_on_table = []
    N = int(sys.argv[2])
    C = int(sys.argv[3])
    check()
    card_in_hand = int(N / C)
    file = open("players.txt", "w")
    for i in range(C):
        for j in range(card_in_hand):
            file.write(randomcard() + ' ')
        file.write('\n')

    file.close()

else:
    check_file()
    C = sys.argv[2]
    file = open("players.txt", "r")
    file_lines = file.readlines()
    if len(file_lines) < int(C):
        print("Ошибка: Количество игроков меньше чем вводимое число")
        raise SystemExit
    print(C, file_lines[int(C) - 1])
    file.close()
