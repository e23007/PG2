import random
secret_number=random.randint(1,20)
print('1から20までの数を当ててください')
for guess_taken in range(6):
    print('数を入力してください')
    guess=int(input())
    if guess < secret_number:
        print('あなたの推定値は小さいです。')
    elif guess > secret_number:
        print('あなたの推定値は大きいです。')
    else:
        break
if guess == secret_number:
    print('当たり！'+str(guess_taken)+'回で当たりました')
else:
    print('残念。正解'+str(secret_number)+'はでした。')