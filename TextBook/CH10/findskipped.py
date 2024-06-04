# #python3 findskipped.py txt txt
import re,os,shutil
def find_skiped_files(folder, prefix, rename=False):
    ''' folderの中のprefixから始まるファイルの連番の飛びを調べる。
        renameがTrueなら、飛びを埋めるようにファイル名を変更する。
    '''
    files = {}         # { 連番: 元ファイル名 } 
    max_digit_len = 0  # 連番の最大の長さ
    rest = ''          # 残りのファイル名 (例 spam001.txtなら、'.txt')

    # 「prefix 連番 残り」を検索
    pattern = re.compile('^' + prefix + r'(\d+)(.*)')
    for filename in os.listdir(folder):
        mo = pattern.search(filename)
        if not mo:
            continue
        files[int(mo.group(1))] = filename
        max_digit_len = max(max_digit_len, len(mo.group(1)))
        rest = mo.group(2)

    # マッチするファイルがなければ終了
    if len(files) == 0:
        return

    # 連番を小さい順に並べる
    org_index = sorted(files.keys())
    start = org_index[0]
    end = org_index[-1]
    # 連番の飛びを調べる
    for n in range(start, end + 1):
        if not n in files:
            print('Missing', prefix + str(n).rjust(max_digit_len, '0') + rest)

    # 飛びを埋めるようにファイル名を変更する
    if rename:
        for n,ind in enumerate(org_index):
            # 新しいファイル名を作る
            new_filename = prefix + str(start + n).rjust(max_digit_len, '0') + rest
            # 元のファイルと同じなら何もしない
            if new_filename == files[ind]:
                continue
            # ファイル名を変更する
            print('Rename', os.path.join(folder, files[ind]), 
                  '->', os.path.join(folder, new_filename))
            shutil.move(os.path.join(folder, files[ind]), 
                        os.path.join(folder, new_filename))

# テスト用
if __name__ == "__main__":
    find_skiped_files('txt', 'txt')
    find_skiped_files('txt', 'txt', True)


# import os, sys, re, shutil

# #ファイル名を取得
# dir_file = sys.argv[1]
# pre = sys.argv[2]
# file_dict = {}

# file_list = os.listdir(dir_file)

# for i in range(0, len(file_list)):
#     file_dict[file_list[i]] = pre + "{:03}.txt".format(i+1)

# #index的にはあるはずなのに、ファイル名として存在しないファイルを探す
# def find_missing_file():
#     for fname in file_dict.values():
#         regex = re.compile(fname)
#         mo = regex.search(", ".join(file_dict.keys()))
#         if not mo:
#             print(fname)


# #元のファイル名から、連番の番号にする
# def change_fname(change = False):
#     if change == True:
#         for k, v in file_dict.items():
#             if k != v:
#                 print(k,v)
#                 shutil.move(os.path.join(dir_file, k), os.path.join(dir_file, v))
        
# find_missing_file()

# print("Do you want to change file name?:  y or [n]")
# option = str(input())
# if option == "y":
#     change = True
# else:
#     change = False
# change_fname(change)