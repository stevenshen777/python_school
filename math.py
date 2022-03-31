from math import *

# 一中 有3个年级，每个年级10班，每班40人，一共？
'''
grades = 3
grade_classes = 10
class_students = 40
'''
#
# grades = 3 # 年级
# grade_classes = 10 #班级数量
# class_students = 40 #每班人数
# total_students = class_students*grade_classes*grades
# # print(total_students)
# print(type(total_students))
# print(type('一中共有学生'))
# print('一中共有学生：'+str(total_students)+'名')
# print('我中学共有 %d个年级，%s名学生' %(grades,str(total_students)))
# '''
# 练习打印 男生boys，女生girls
# '''
'''
计算面积：
s1= a * b
s2 = 1/2 * c * h
s3 = pi * r * r
'''
#
# ####正方形面积##################
# a = 100
# b = 50
# s1 =a*b
# ####三角形面积##################
# c = 20
# h = 30
# s2 = 1/2*c*h
# ######计算圆形面积###############
# pi = 3.14
# r =10
# s3 = pi*r*r
# ######打印结果#################
# print(type(s1))
# print(type(s2))
# print(type(s3))
# print('长方形面积：%d'%(s1))
# print('三角形面积：%f'%(s2))
# print('圆形面积：%f'%(s3))
#
# a = input('请输入长方形边长a:')
# b = input('请输入长方形边长b:')
# print(type(a))
# s1 =int(a)*int(b)
# print(type(s1))
# print('长方形面积：%d' % (s1))
#####################################
# c = input('请输入三角形边长c:')
# h = input('请输入三角形高h:')
# print(type(c))
# s2 =1/2*float(c)*float(h)
# print(type(s2))
# print('三角形面积：%f' % (s2))
#######################################
# pi = 3.1415926
# r = float(input('请输入圆形半径r:'))
# s3 = pi*r*r
# print('圆形面积：%f' % (s3))
########################################
# def something():
#     print("something function")
def circle_size(r):
    s3 = pi*r*r
    print('圆形面积：%f' % (s3))

def triangle_size(c,h):
    s = 1/2*c*h
    print('三角形面积：%f' % (s))

def rectangle_size(a,b):
    s = a*b
    print('长方形面积：%f' % (s))

# r = float(input('请输入圆形半径r:'))
# circle_size(r)
# c = float(input('三角形底边长c：'))
# h = float(input('三角形高h：'))
# triangle_size(c,h)
#
# a = float(input('请输入长方形边长a:'))
# b = float(input('请输入长方形边长b:'))
# rectangle_size(a,b)

# for i in range(0,10):
#     print(i+1)
# for i in range(1,11):
#     print(i)
#
#
# i = 0
# while(1):
#     i = i+1
#     print(i)
#     if i==1000:
#         break

# 1+2+3+...100=?
# sum = 0
# num = 0
# for i in range(1,101):
#     sum =sum+i
#     print('当前总和：%d ，当前循环数字：%d' % (sum,i))
#
# print('最终总和：%d'%(sum))
#
# while(True):
#     num = num +1
#     sum = sum + num
#     print('当前总和：%d ，当前循环数字：%d' % (sum, num))
#     if num ==100:
#         break
# 打印九九乘法表
# row 表示行，col 表示列


def multi_table(num=10):
    for row in range(1, num):
        print('当前行：%d' % (row))
        for col in range(row, num):
            print('当前行：%d,当前列：%d' % (row, col))
            print('当前行：%d *当前列：%d = %d' % (row, col, row * col))

# multi_table(num=100)
from random import randint

def add_problems(problems=100):
    for prob in range(0,problems):
        a = randint(1, 100)
        b = randint(1, 100)
        print('第 %d 道题：%d + %d = %d' % (prob+1,a,b,a+b))

def multi_problems(problems=100):
    for prob in range(0,problems):
        a = randint(1, 100)
        b = randint(1, 100)
        print('第 %d 道题：%d * %d = %d' % (prob+1,a,b,a*b))

# def minus_problems(problems=100):
#     for prob in range(0,problems):
#         a = randint(1, 100)
#         b = randint(1, 100)
#         if a<b :
#             continue
#         print('第 %d 道题：%d - %d = %d' % (prob+1,a,b,a-b))
#
# def divided_problems(problems=100):
#     for prob in range(0,problems):
#         a = randint(1, 1000)
#         b = randint(1, 1000)
#         if a<b:
#             continue
#         if a%b!=0:
#             continue
#         if b==1:
#             continue
#         print('第 %d 道题：%d / %d = %d' % (prob+1,a,b,a/b))
# divided_problems(problems=2000)

def minus_problems(problems=100):
    prob = 0
    while(True):
        a = randint(1, 100)
        b = randint(1, 100)
        if a < b:
            continue
        print('第 %d 道题：%d - %d = %d' % (prob + 1, a, b, a - b))
        prob =prob+1
        if prob == problems:
            break
# minus_problems(problems=20)

def divided_problems(problems=100):
    prob = 0
    while(True):
        a = randint(1, 100)
        b = randint(1, 100)
        if a<b:
            continue
        if a%b!=0:
            continue
        if b==1:
            continue
        print('第 %d 道题：%d / %d = %d' % (prob+1,a,b,a/b))
        prob = prob + 1
        if prob == problems:
            break

divided_problems(problems=20)




















