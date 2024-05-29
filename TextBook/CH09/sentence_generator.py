import sys,re


if len(sys.argv) < 2:
    sys.exit('どのテキストを開きますか？')
# テキストファイルをすべて読み込む
src_file = open(sys.argv[1], 'r')
src_data = src_file.read()
src_file.close()

# 置き換える文字列
pattern = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')

while True:
    # 出現順にユーザに問い合わせる
    mo = pattern.search(src_data)
    if not mo:
        break

    # プロンプトを表示して、入力を受け付ける。
    print('Enter a', end='')
    # ADJECTIVE と ADVERB の場合は、冠詞を an にする
    if mo.group(1)[0] == 'A':
        print('n', end='')
    repl = input(mo.group(1).lower() + ': ')

    # ひとつだけ置換する
    src_data = src_data.replace(mo.group(1), repl, 1)

# 置換結果を画面に表示する
print(src_data, end='')

# テキストファイルに保存する
dst_file = open(sys.argv[1] + '.generated.txt', 'w')
dst_file.write(src_data)
dst_file.close()


# import pyinputplus as pyip

# def change_text(adjective, noun, verb, adverb, file_path):
#     with open(file_path, 'r') as f:
#         content = f.read()
#         placeholders = {'ADJECTIVE': adjective, 'NOUN': noun, 'VERB': verb, 'ADVERB': adverb}
#         for placeholder, replacement in placeholders.items():
#             content = content.replace(placeholder, replacement)
#     with open(file_path, 'w') as f:
#         f.write(content)


# def main():
#     file_path = 'file_name.txt'
#     prompts = {
#         '形容詞を入力してください: ': 'adjective',
#         '名詞を入力してください: ': 'noun',
#         '動詞を入力してください: ': 'verb',
#         '副詞を入力してください: ': 'adverb'
#     }
#     user_inputs = {key: pyip.inputStr(prompt) for prompt, key in prompts.items()}
#     change_text(**user_inputs, file_path=file_path)


#main()