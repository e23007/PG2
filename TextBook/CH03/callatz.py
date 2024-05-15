def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

number = int(input("数字を入力してください: "))
print(r:= collatz(number))
while r != 1:
    print(r := collatz(r))


# import time
# print('整数を入力してください：')
# number=int(input())

# def callatz(number):
#     time.sleep(1)
#     if number%2==0:
#         number//=2
#         return number
#     else:
#         number=number*3+1
#         return number


# while number>1:
#     result=callatz(number)
#     print(result)
#     number=result