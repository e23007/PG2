#変化5の階乗だが0から始まってしまっているので1からに変更した
#デバック後
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

logging.debug('プログラム開始')

def factorial(n):
    logging.debug(f'factorial({n}開始)')
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug(f'i={i},i=total={total}')
    logging.debug(f'factorial({n}終了)')
    return total
print(factorial(5))
logging.debug('プログラム終了')


#デバック前
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

# logging.debug('プログラム開始')

# def factorial(n):
#     logging.debug(f'factorial({n}開始)')
#     total=1
#     for i in range(n+1):
#         total*=i
#         logging.debug(f'i={i},i=total={total}')
#     logging.debug(f'factorial({n}終了)')
#     return total
# print(factorial(5))
# logging.debug('プログラム終了')