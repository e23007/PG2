import time,sys


print('表示したい回数分の数字を入力、無限ならを-1入力')
i=int(input())

def zigzag(i):
    indent=0
    indent_increasing=True
    while i>0  or i<0:
        print(' '* indent,end='')
        print('*'*8)
        time.sleep(0.2)
        if indent_increasing:
            indent+=1
            if indent==20:
                indent_increasing=False
        else:
            indent-=1
            if indent==0:
                indent_increasing=True
        i-=1
        if i==0:
            break

try:
    zigzag(i)
        
except KeyboardInterrupt:
    sys.exit()


# import time,sys

# indent=0
# indent_increasing=True

# print('表示したい回数分の数字を入力、無限ならを0入力')
# i=int(input())

# try:
#     if i==0:
#         print('1')
#         while True:
#                 print(' '* indent,end='')
#                 print('*'*8)
#                 time.sleep(0.2)
#                 if indent_increasing:
#                     indent+=1
#                     if indent==20:
#                         indent_increasing=False
#                 else:
#                     indent-=1
#                     if indent==0:
#                         indent_increasing=True
#     else:
#          while True:
#                 if i==0:
#                      sys.exit(0)
#                 else:
#                     print(' '* indent,end='')
#                     print('*'*8)
#                     time.sleep(0.2)
#                     if indent_increasing:
#                         indent+=1
#                         if indent==20:
#                             indent_increasing=False
#                     else:
#                         indent-=1
#                         if indent==0:
#                             indent_increasing=True
#                 i-=1
# except KeyboardInterrupt:
#     sys.exit()