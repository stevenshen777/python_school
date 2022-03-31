'''
>
<
==
!=
>=
<=
'''
your_gender = input('请输入您的性别(boy or girl):')
# print(type(your_gender))
# if your_gender =="boy" :
#     print('play football')
# if your_gender =="girl" :
#     print('play volleyball')
##########################################
#  if  else
def play_balls(your_gender):
    if your_gender == 'boy' :
        print('让我们去踢足球！')
    else:
        print('我们去打排球！')

# 如果气温>=30 go swimming , 气温 《 30 play outside


def what_to_do(temperature,weather='sunny'):
    if temperature > 28 and weather =='sunny':
        print("Let's go swimming!")
        print('让我们去游泳!')
    elif temperature < 25  and weather =='sunny':
        print('play outside!')
        play_balls(your_gender)
    else:
        print('Let\'s do homework!')

temperature = 32
weather = 'rainy'
what_to_do(temperature,weather)








