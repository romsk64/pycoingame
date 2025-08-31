import random

coins = 100
credit2 = 0 # 0 - кредитов нет, 1 - кредиты есть
crtype = 0 # тип кредита: 1 на 100к, 2 на 1млн, 3 на 1млрд
print('Ваши коины:', coins)

def credit():
    print("Кредит взят. Долг снимется с вас через 100 ходов.")
    global hods
    global credit2
    hods = 0 # ходы. если ходы = 100, списываются деньги
    credit2 = 1

def unknown():
    print("Неизвестная команда")

# колво шагов
def hodcnt():
    if credit2 == 1:
        hods += 1

def work():
    print("Ты нажиматель ENTER'а. Готов работать?")
    ch6 = input("1 - да, 2 - нет")
    if ch6.lower() == "1":
        print("Начали!")
        for i in range(100):
            input()
        print("Молодец! Вот 10000 коинов!")
        global coins
        coins += 10000
    else:
        print("Ну и иди на помойку >:(")

choice = input('bal - посмотреть баланс, rul - посмотреть куда нажимать, q - выйти\n')
while choice.lower() != "q":
    if coins < 0:
        print("Вы проиграли(((")
        print(f"У вас осталось {coins} коинов")
        print("Разработчик: romsk64")
        break
    elif credit2 == 1 and hods >= 100:
        if crtype == 1:
            coins -= 100000
        elif crtype == 2:
            coins -= 1000000
        elif crtype == 3:
            coins -= 1000000000
        print("Снимаю долг.")
        print(f"Ваш баланс: {coins}")
    elif choice.lower() == 'bal':
        print(f"Ваш баланс: {coins}")
        print("")
    elif choice.lower() == 'rul':
        print("1 - магазин, 2 - посмотреть рекламу(+5), 3 - взять кредит, 4 - учавствовать в игре, 5 - участвовать в игре «Пять букв», 6 - работать на нормальной работе")
    elif choice.lower() == '1':
        hodcnt()
        ch2 = input("1 — стикер (50), 2 — футболка (100)")
        if ch2 == '1':
            coins -= 50
            print(f"Ваши коины: {coins}")
        elif ch2 == '2':
            coins -= 100
            print(f"Ваши коины: {coins}")
        else:
            unknown()
    elif choice.lower() == '2':
        hodcnt()
        coins += 5
        print(f"Ваши коины: {coins}")
    elif choice.lower() == '3':
        hodcnt()
        print("Вы хотите взять кредит?")
        ch3 = input("1 - да, 2 - нет")
        if ch3.lower() == '1':
            print("На какую сумму?")
            ch4 = input("1 - на 100тыс коинов, 2 - на 1млн коинов, 3 - на 1млрд коинов")
            if ch4.lower() == '1':
                credit()
                crtype = 1
                coins += 100000
            elif ch4.lower() == '2':
                credit()
                crtype = 2
                coins += 1000000
            elif ch4.lower() == '3':
                credit()
                crtype = 3
                coins += 1000000000
            else:
                unknown()
        elif ch3.lower() == '2':
            print("Ок")
        else:
            unknown()
    elif choice.lower() == '4':
        hodcnt()
        print("Игра! Вы должны угадать случайное число")
        ch5 = input("1 - две цифры (500 коинов, выигрыш - 700), 2 - три цифры (400 коинов, выигрыш - 800), 3 - пять цифр (300 коинов, выигрыш - 1000)")
        if ch5 == '1':
            coins -= 500
            number = random.randrange(1, 3)
            prise = int(input("Введите число 1 или 2"))
            if prise == number:
                print("Ты выиграл! Держи 700 коинов!")
                coins += 700
            else:
                print("Ты проиграл. Повезет в следующий раз")
        elif ch5 == '2':
            coins -= 400
            number = random.randrange(1, 4)
            prise = int(input("введите число 1, 2 или 3"))
            if prise == number:
                print("Ты выиграл! Держи 800 коинов!")
            else:
                print("Ты проиграл. Повезет в следующий раз!")
        elif ch5 == '3':
            coins -= 300
            number = random.randrange(1, 6)
            prise = int(input("Введите число от 1 до 5"))
            if prise == number:
                print("Ты выиграл! Держи 1000 коинов!")
            else:
                print("Ты проиграл. Повезет в следующий раз!")
        else:
            unknown()
    elif choice.lower() == '5':
        hodcnt()
        ch6 = ("1 - играть, 2 - правила")
        if ch6.lower() == '2':
            print('У тебя 6 попыток. Если ты отгадаешь букву, то будет написано "П", а если не угадал, то "Н"')
        randomword = random.randint(0, 3)
        words = "САХАРКРЕСТМЕТРОНОСОК"
        if randomword == 0:
            chosenword = words[0:5]
            print(chosenword)
            wordletter1 = words[0]; wordletter2 = words[1]; wordletter3 = words[2]; wordletter4 = words[3]; wordletter5 = words[4]
            print(wordletter1, wordletter2, wordletter3, wordletter4, wordletter5)
        elif randomword == 1:
            chosenword = words[5:10]
            print(chosenword)
            wordletter1 = words[5]; wordletter2 = words[6]; wordletter3 = words[7]; wordletter4 = words[8]; wordletter5 = words[9]
            print(wordletter1, wordletter2, wordletter3, wordletter4, wordletter5)
        elif randomword == 2:
            chosenword = words[10:15]
            print(chosenword)
            wordletter1 = words[10]; wordletter2 = words[11]; wordletter3 = words[12]; wordletter4 = words[13]; wordletter5 = words[14]
            print(wordletter1, wordletter2, wordletter3, wordletter4, wordletter5)
        elif randomword == 3:
            chosenword = words[15:20]
            print(chosenword)
            wordletter1 = words[15]; wordletter2 = words[16]; wordletter3 = words[17]; wordletter4 = words[18]; wordletter5 = words[19]
            print(wordletter1, wordletter2, wordletter3, wordletter4, wordletter5)
    elif choice.lower() == '6':
        hodcnt()
        work()
    else:
        unknown()
    hodcnt()
    choice = input('bal - посмотреть баланс, rul - посмотреть куда нажимать, q - выйти\n')