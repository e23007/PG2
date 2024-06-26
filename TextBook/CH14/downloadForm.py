#python3 downloadForm

import ezsheets

ID = '1GG9nofKlwcU0C5Ts5Q2Ls0j8ZWsj2Zhzaa9Eu6FZP0w'

ss = ezsheets.Spreadsheet(ID)
sheet = ss[0]
for row in range(sheet.rowCount):
    data = sheet.getRow(row + 1)
    print(data)