inventorys={'ロープ':1,'たいまつ':6,'金貨':42,'手裏剣':1,'矢':12}

def displey_inventory(inventorys):
    item=0
    for key,value in inventorys.items():
        print(value,key)
        item+=value
    return item
print('持ち物リスト：')
result=displey_inventory(inventorys)
print(f"アイテム総数：{result}")