import re
passwd=input('パスワードを入力して下さい:')




def passcheck(passwd):
    if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])[A-Za-z\d]{8,}$',passwd):
        return print('passwd条件を満たしています')
    else:
        return print('passwd条件を満たしていません')


passcheck(passwd)
