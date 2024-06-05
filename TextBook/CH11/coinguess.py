import random
coin=['表','裏']

def choices():
    guess=''
    while guess not in ('表','裏'):
        print('コインの表裏を当ててください。表か裏を入力してください。')
        guess=input()
    return guess

guess=choices()
toss=coin[random.randint(0,1)] #0は裏,1は裏
if toss==guess:
    print('当たり!')
else:
    print('はずれ!もう一回当てて!')
    guess=choices()
    if toss==guess:
        print('当たり!')
    else:
        print('はずれ。このゲームは苦手ですね。')

# import random
# guess=''
# while guess not in ('表','裏'):
#         print('コインの表裏を当ててください。表か裏を入力してください。')
#         guess=input()
# toss=random.randint(0,1)#0は表,1は裏
# if toss==guess:
#     print('当たり!')
# else:
#     print('はずれ!もう一回当てて!')
#     guess=input()
#     if toss==guess:
#         print('当たり!')
#     else:
#         print('はずれ。このゲームは苦手ですね。')