import time
print('整数を入力してください：')
number=int(input())

def callatz(number):
    time.sleep(1)
    if number%2==0:
        number//=2
        return number
    else:
        number=number*3+1
        return number


while number>1:
    result=callatz(number)
    print(result)
    number=result