#! python2
#ターミナル(VSCodeでなく)で以下を実行
#mcb.py -クリップボードのテキストを保存・復元
#python3 mcb.py save <keyword> - クリップボードをキーワードに紐付けて保存
#python3 mcb.py <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
#python3 mcb.py list - 全キーワードをクリップボードにコピー
import shelve,pyperclip,sys
mcb_shelf=shelve.open('mcb')
#TODO:クリップボードの内容を保存
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcb_shelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
#TODO:キーワード一覧を、内容の読み込み
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
