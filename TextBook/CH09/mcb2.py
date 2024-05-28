#! python2
#ターミナル(VSCodeでなく)で以下を実行
#mcb.py -クリップボードのテキストを保存・復元
#python3 mcb2.py save <keyword> - クリップボードをキーワードに紐付けて保存
#python3 mcb2.py <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
#python3 mcb2.py list - 全キーワードをクリップボードにコピー
#python3 mcb2.py delete <keyword> - キーワードに紐づけられたテキストを削除
#python3 mcb2.py clear - キーワード全削除
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
#TODO:キーワードを削除
elif sys.argv[1].lower()=='delete':
    if sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]
    elif sys.argv[2]=='clear':
        mcb_shelf.clear()
    else:
        print('そのようなキーワードはございません')
mcb_shelf.close()