import re


message=input('入力してください:')


def restrip(message,cut=r'\s'):
    return re.sub('^[' +cut+ ']*(.*?)[' +cut+ ']*$', r'\1', message)


print(restrip(message))