import random
list = ["камень", "ножницы", "бумага"]
def start():
    print("Привет! Хочешь поиграть?")
    ans = input("Напиши \"Да\" или \"Нет\" ")
    if ans.lower() == "да": 
        compare()
    elif ans.lower() == "нет":
        print("В следующий раз")
    else:
       ans = input("")
def compare():
    us = input("Сделай выбор: камень, ножницы или бумага? ")
    comp = random.choice(list)
    if us.lower() == "камень" and comp == "ножницы" or us.lower() == "ножницы" and comp == "бумага" or us.lower() == "бумага" and comp == "камень":
        print(f"Твой выбор: {us}, а мой выбор: {comp}. Ты выиграл! Попробуй еще раз.")
        ans1 = input("Хочешь еще раз?")
        if ans1.lower() == "да": 
             compare()
        elif ans1.lower() == "нет":
             print("В следующий раз")
        else:
             ans1 = input("Неправильный ввод. Введите заново")
    elif us.lower() == comp:
        print(f"Твой выбор: {us}, а мой выбор: {comp}. Ничья. Попробуй еще раз.")
        ans1 = input("Хочешь еще раз?")
        if ans1.lower() == "да": 
             compare()
        elif ans1.lower() == "нет":
             print("В следующий раз")
        else:
             ans1 = input("Неправильный ввод. Введите заново")
    else:
        print(f"Твой выбор: {us}, а мой выбор: {comp}. Ты проиграл! Попробуй еще раз.")
        ans1 = input("Хочешь еще раз?")
        if ans1.lower() == "да": 
             compare()
        elif ans1.lower() == "нет":
             print("В следующий раз")
        else:
             ans1 = input("Неправильный ввод. Введите заново")
start()