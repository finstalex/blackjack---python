koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
name=input(str("Введите Ваше имя : "))
print("Поиграем в Блекджек "+name+"?")
print ("Правила игры: Нужно набрать 21 очко")
count = 0
while True:
    choice = input("Будете брать карту? да/нет\n")
    if choice == "да":
        current = koloda.pop()
        print("Вам попалась карта достоинством %d" %current)
        count += current
        if count > 21:
            print("Извините "+name, "но вы проиграли")
            break
        elif count == 21:
            print("Поздравляю "+name , "вы набрали 21!")
            break
        else:
            print(name+" у вас %d очков." %count)
    elif choice == 'нет':
        print(name+" у вас %d очков и вы закончили игру." %count)
        break
print("До новых встреч!")
