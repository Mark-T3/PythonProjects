import random
def start():
    print("Привет! Хочешь поиграть в \"Угадай Число\"?")
    ans = input("Напиши \"Да\" или \"Нет\" ")
    if ans.lower() == "да":
        compare()
    elif ans.lower() == "нет":
        print("В следующий раз")
    elif ans.lower()!= "да" or ans.lower()!= "нет":
               ans = input("Неправильный ввод. Повторите:")
def compare():
   a = random.randint(0,10)
   while True:
       b = int(input("Твое число: "))
       if a == b:
           print("Ты выиграл!")
           ans1 = input("Хочешь еще раз ?")
           if ans1.lower() == "да":
               a = random.randint(0,10)
               continue
           elif ans1.lower() == "нет":
               print("В следующий раз")
               break
           elif ans1.lower()!= "да" or ans1.lower()!= "нет":
               ans1 = input("Неправильный ввод. Повторите:")
       elif a < b:
           print("Мое число меньше:)")
       elif a > b:
           print("Мое число больше:)")
start()
   