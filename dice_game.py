# 掷骰子小游戏

from random import randint

def dice(sides=6):
    point = randint(1,sides)
    # print(point)
    return point

def roll_dice(num=3,points=0):
    while num >0:
        p = dice()
        print(p)
        points =points+ p
        num =num -1
    return points

def big_small(points):
    isBig = 11<=points<=18
    isSmall = 3<=points<=10
    if isBig :
        return 'Big'
    elif isSmall:
        return 'Small'

def play_game(times =3):
    while times>0:
        your_choice = input('请输入Big 或者 Small：')
        p = roll_dice()
        result = big_small(p)
        if your_choice==result:
            print('You win')
        else:
            print('You lose')
        times = times-1

play_game(times=2)

