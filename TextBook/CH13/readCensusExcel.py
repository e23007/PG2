#! python3
# readCensusExcel.py

import openpyxl,pprint
print('ワークブックを開いています...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
county_data={}
#TODO:cunty_dataに郡の人口と地域数を格納する
print('行を読み込んでいます')
for row in range(2,sheet.max_row+1):
    #スプレットシートの1行に1つの人口調査標準地域のデータがある
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
#TODO:新しいテキストファイルを開き、county_dataの内容を書き込む
#conty_data={'AK':{'Aeutians East':{'pop':3141,'tracts':1},'Aleutians West':{'pop':5561,'tracts':12},'Anchorage':{'pop':291826,'tracts':55},'Bethel':{'pop':17013,'tracts':3},'Bristol Bay':{'pop':997,'tracts':1}}}

    #この州のキーが確実に存在するようにする
    county_data.setdefault(state,{})
    #この州のこの郡のキーが確実に存在するようにする
    county_data[state].setdefault(county,{'tracts':0,'pop':0})
    #各行が人口調査標準地域を表すので、数を1つ増やす
    county_data[state][county]['tracts']+=1
    #この人口調査標準地域の人口だけ郡の人口を増やす
    county_data[state][county]['pop']+=int(pop)
#TODO:新しいテキストファイルを開き、county_dataの内容を書き込む
print('結果を書き込み中...')
result_file=open('census2010.py','w')
result_file.write('all_data='+pprint.pformat(county_data))
result_file.close()
print('完了')
