# 数据结构
# list(), dict(), tuple(),set()
# 重点讲解 list 列表 和 dict 字典，
# list 列表：
# students_number = [1,2,3,4,5,6,7,8,9,10]
# boys = [3,1,5,7,9]
# girls = [2,4,6,8,10]
# teachers =['牛顿','李白','爱因斯坦','莎士比亚','郎平']
#
# print(len(boys))
# boys.pop(0)
# print(len(boys))
# boys.append(99)
# boys.remove(9)
# boys.extend([55,66])
# boys.append([77,88])
# # boys.sort(reverse=True)
# print(boys)
#
# # 有多少名老师，他们都是谁？
# for i in range(len(teachers)):
#     print('第%d位老师是：%s' % (i+1,teachers[i]))
#
# for i in range(len(students_number)):
#     students_number.pop(0)
#     print('第%d同学正在打菜，还有%d位同学在等候' % (i+1,len(students_number)))

# 字典 dict {key:value}
# englist_words ={'apple':'苹果',
#                 'banana':'香蕉',
#                 'car':'小汽车',
#                 'ship':'轮船'}
# print(englist_words['car'])
# print(englist_words.keys())
# print(englist_words.values())
# print(englist_words.items())
# englist_words.pop('car')
# print(englist_words)
# englist_words.update({'plane':'飞机','school':'学校'})
# print(englist_words)
#学生健康表，dict   [{},{},{},{}]
students_health =[{'学号':101,'姓名':'宋江','性别':'男','年龄':25,'是否免疫':True},
                  {'学号':102,'姓名':'武松','性别':'男','年龄':35,'是否免疫':True},
                  {'学号':103,'姓名':'武则天','性别':'女','年龄':45,'是否免疫':True},
                  {'学号':104,'姓名':'刘备','性别':'男','年龄':55,'是否免疫':False},
                  {'学号':105,'姓名':'小乔','性别':'女','年龄':21,'是否免疫':False},
                  ]
print(len(students_health))
mut_num=0
for stu in range(len(students_health)):

    if students_health[stu]['是否免疫']:
        mut_num +=1 #mut_num = mut_num+1
    else:
        print('%s同学没有注射免疫疫苗'% (students_health[stu]['姓名']))
print('当前共有%d名同学免疫！'%(mut_num))

#tuple() 元组 元素是不可更改
week_day = ('Mon','Tue','Wed','Thu','Fri')
colors = ('red','yellow','blue','white','black')
wu_xing = ('金','木','水','火','土')
for wx in range(len(wu_xing)):
    print(wu_xing[wx])
# set() 集合 元素没有重复，具有去除重复元素的功能
stock_list =set({600000,300001})
stock_list.add(300002)
stock_list.update({600000,600001})
print(stock_list)

#########总结：list -> [], dict ->{key:value,}, tuple ->() , set -> {1,2,3}



