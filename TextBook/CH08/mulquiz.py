import random,time,math

result=0
for i in range(10):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    mult=num1*num2
    print(f"{num1} X {num2}=",end='')
    start=time.perf_counter()
    while True:
        answer=int(input())
        if answer==mult:
            break
        else:
            print('不正解')
            continue
    end=time.perf_counter()
    if 8>math.floor(end-start):
        result+=1
        print('正解')
    else:
        print('時間切れ')

print(f"正解数は{result}/10でした。")    