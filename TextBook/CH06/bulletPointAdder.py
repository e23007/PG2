#! python3
# bulletPointAdder.py - クリップボードのテキストの各行に
#点を打って、Wikipediaの箇条書きにする

import pyperclip
text=pyperclip.paste()

#行を分割して、を"*"追加する
pyperclip.copy(text)
lines=text.split('\n')
for i in range(len(lines)-1):
    lines[i]='*'+lines[i]

text='\n'.join(lines)
pyperclip.copy(text)

