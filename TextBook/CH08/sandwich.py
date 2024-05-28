import pyinputplus as pyip

PRICES = {
    '小麦パン': 100,
    '白パン': 110,
    'サワー種': 120,
    'チキン': 200,
    'ターキー': 250,
    'ハム': 300,
    '豆腐': 280,
    'チェダー': 100,
    'スイス': 150,
    'モツァレラ': 180,
    'mayo': 10,
    'mustard': 10,
    'lettuce': 50,
    'tomato': 30,
}

def sandwich_maker(PRICES):
    bread=pyip.inputMenu(['小麦パン', '白パン', 'サワー種'],prompt='パンを選んで下さい:\n')
    protein=pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'],prompt='タンパク質の種類を選んで下さい:\n')
    cheese=pyip.inputYesNo(prompt='チーズを追加しますか?\n',yesVal='はい', noVal='いいえ')
    if cheese=='はい':
        cheese=pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'],prompt='チーズを選んで下さい\n')
    mayo = pyip.inputYesNo(prompt='マヨネーズを追加しますか？\n', yesVal='はい', noVal='いいえ', )
    mustard = pyip.inputYesNo(prompt='マスタードを追加しますか？\n', yesVal='はい', noVal='いいえ', )
    lettuce=pyip.inputYesNo(prompt='レタスを追加しますか\n',yesVal='はい',noVal='いいえ')
    tomato=pyip.inputYesNo(prompt='トマトを追加しますか？\n',yesVal='はい',noVal='いいえ')
    count=pyip.inputInt(prompt='サンドイッチの数を入力して下さい:\n',min=1)
    total=0
    total+=PRICES[bread]
    total+=PRICES[protein]
    if cheese!='いいえ':
        total+=PRICES[cheese]
    if tomato=='はい':
        total+=PRICES['tomato']
    if lettuce=='はい':
        total+=PRICES['lettuce']
    if mayo=='はい':
        total+=PRICES['mayo']
    if mustard=='はい':
        total+=PRICES['mustard']
    total*=count
    print('-'*20)
    print(f'注文内容は以下の通りです:\n'
          f'パン: {bread}\n'
          f'タンパク質: {protein}\n'
          f'チーズ: {cheese}\n'
          f'トマト: {tomato}\n'
          f'レタス: {lettuce}\n'
          f'マヨネーズ: {mayo}\n'
          f'マスタード: {mustard}\n'
          f'サンドイッチの数: {count}\n'
          f'合計金額:{total}'
          f'ありがとうございました！')



sandwich_maker(PRICES)



# def sandwich_maker():
#     bread = pyip.inputMenu(['小麦', '白パン', 'サワー種'], prompt='パンを選んでください:\n', )
#     protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n', )
#     cheese = pyip.inputYesNo(prompt='チーズを追加しますか？\n', yesVal='はい', noVal='いいえ',)
#     if cheese == 'はい':
#         cheese = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], prompt='チーズを選んでください:\n', )
#     else:
#         cheese = 'なし'
#     tomato = pyip.inputYesNo(prompt='トマトを追加しますか？\n', yesVal='はい', noVal='いいえ', )
#     lettuce = pyip.inputYesNo(prompt='レタスを追加しますか？\n', yesVal='はい', noVal='いいえ', )
#     mayo = pyip.inputYesNo(prompt='マヨネーズを追加しますか？\n', yesVal='はい', noVal='いいえ', )
#     mustard = pyip.inputYesNo(prompt='マスタードを追加しますか？\n', yesVal='はい', noVal='いいえ', )

#     count = pyip.inputInt(prompt='サンドイッチの数を入力してください:\n', min=1)

#     print(f'注文内容は以下の通りです:\n'
#           f'パン: {bread}\n'
#           f'タンパク質: {protein}\n'
#           f'チーズ: {cheese}\n'
#           f'トマト: {tomato}\n'
#           f'レタス: {lettuce}\n'
#           f'マヨネーズ: {mayo}\n'
#           f'マスタード: {mustard}\n'
#           f'サンドイッチの数: {count}\n'
#           f'ありがとうございました！')


# if __name__ == '__main__':
#     sandwich_maker()