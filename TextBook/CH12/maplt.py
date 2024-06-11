#python3 maplt.py <検索したい住所を記入>
#python3 maplt.py　コピーをしておき実行
import webbrowser,sys,pyperclip

if len(sys.argv)>1:
    #コマンドラインから住所を取得する
    address=' '.join(sys.argv[2:])
else:
#TODO:クリップボードから住所を取得する
    address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)

#sudo apt update 
#sudo apt upgrade
#echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrom-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
#curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/googlechrom-keyring.gpg
#sudo apt update
#sudo apt install google-chrome-stable
#google-chrome
#google-chromeが開いたら成功