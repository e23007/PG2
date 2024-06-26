#python3 findMistake.py
#https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit?gid=289119951#gid=289119951

import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet = ss[0]
for row in range(1, sheet.rowCount):
    data = sheet.getRow(row + 1)
    try:
        beans_per_jar = int(data[0])
        jars = int(data[1])
        total_beans = int(data[2])
        if beans_per_jar * jars != total_beans:
            print(f'{row + 1}行の{beans_per_jar}と{jars}の掛け算が{total_beans}となっている')
    except:
        break