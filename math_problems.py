# 题库
from random import randint

min = 1
max = 100
prob_num = 100
def add_problems(problems=prob_num, score=0): # 加法题库
    for prob in range(0,problems):
        a = randint(min, max)
        b = randint(min, max)
        print('第 %d 道题：%d + %d = ?' % (prob+1,a,b))
        result = input('请输入本题的答案(必须为数字)：')
        if result.isdigit(): #判断是否数字
            result = int(result)
        else:
            continue
        if result == a+b:
            score = score +1 #累计分数
        else:
            continue
    score = score/problems*100 #计算分数占比
    return score



def multi_problems(problems=prob_num,score = 0): # 乘法题库
    for prob in range(0,problems):
        a = randint(min, max)
        b = randint(min, max)
        print('第 %d 道题：%d * %d = ?' % (prob+1,a,b))
        result = input('请输入本题的答案(必须为数字)：')
        if result.isdigit():  # 判断是否数字
            result = int(result)
        else:
            continue
        if result == a * b:
            score = score + 1  # 累计分数
        else:
            continue
    score = score / problems * 100  # 计算分数占比
    return score





def minus_problems(problems=prob_num,score=0): #减法题库
    prob = 0
    while(True):
        a = randint(1, 100)
        b = randint(1, 100)
        if a < b:
            continue
        print('第 %d 道题：%d - %d = ?' % (prob + 1, a, b))
        prob =prob+1
        result = input('请输入本题的答案(必须为数字)：')
        if result.isdigit():  # 判断是否数字
            result = int(result)
        else:
            continue
        if result == a - b:
            score = score + 1  # 累计分数
        else:
            continue
        if prob == problems:
            break
    score = score / problems * 100  # 计算分数占比

    return score


def divided_problems(problems=prob_num,score=0): #出发题库
    prob = 0
    while(True):
        a = randint(min, max)
        b = randint(min, max)
        if a<b:
            continue
        if a%b!=0:
            continue
        if b==1:
            continue
        print('第 %d 道题：%d / %d = ?' % (prob+1,a,b))
        prob = prob + 1
        result = input('请输入本题的答案(必须为数字)：')
        if result.isdigit():  # 判断是否数字
            result = int(result)
        else:
            continue
        if result == a / b:
            score = score + 1  # 累计分数
        else:
            continue
        if prob == problems:
            break
    score = score / problems * 100  # 计算分数占比

    return score