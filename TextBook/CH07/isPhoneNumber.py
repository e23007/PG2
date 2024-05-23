def is_phone_number(text):
    #全体が12文字かどうか確認
    if len(text)!=12:
        return False
    #先頭から3文字が数字であることを確認
    for i in range(3):
        if not text[i].isdecimal():
            return False
    #3文字のあとに-がついているか確認
    if text[3]!='-':
        return False
    #-を確認できたら3文字が数字か確認
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    #3文字の数字のあとに-が付いているか確認
    if text[7]!='-':
        return False
    #-の後に4文字の数字があるか確認
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    #全てOKだったらをTrue返す
    return True
print('415-555-4242は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi は電話番号:')
print(is_phone_number('Moshi moshi'))
