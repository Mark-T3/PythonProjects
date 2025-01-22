import random
board = list(range(1,10))
def biuldarea(x):
    for i in range(3):
        print("_"*13)
        print("❘ "+str(x[i*3+0])+" ❘ "+str(x[i*3+1])+" ❘ "+str(x[i*3+2])+" ❘")
    print("_"*13)  
def turn (x):
    valid = False
    while not valid:
       ans = input("Напиши номер клетки ")
       ans = int(ans)
       if 0 < ans < 10:
           if str(board[ans-1]) not in 'X0':
              board[ans-1]= x
              valid = True
           else:
              print("Тут занято! Выбери другую клетку")
       else:
           print("Введите правильно номер клетки")
def main(x):
    count = 0
    win = False
    while not win:
        biuldarea(x)
        if count%2 == 0:
            turn('X')
        else:
            turn('0')
        count+=1
        tmp = checkwin(board)
        if tmp:
            print("{0} победитель!".format(tmp))
            win = True
            break
        if count == 9:
            print("Ничья!")
            break
    biuldarea(board)

def checkwin(x):
    varlist = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in varlist:
        if x[i[0]] == x[i[1]] == x[i[2]]:
            return board[i[0]]
    return False
            

main(board)

