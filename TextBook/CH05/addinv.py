inventorys={'ロープ':1,'金貨':42}
added_item=['金貨','手裏剣','金貨','金貨','ルビー']

def add_to_inventory(indentorys,added_items):
    for added_item in added_items:
        if added_item in indentorys.keys():
            indentorys[added_item]+=1
        else:
            indentorys[added_item]=1
    return inventorys

def displey_inventory(inventorys):
    item=0
    for key,value in inventorys.items():
        print(value,key)
        item+=value
    return item

(inventorys:=add_to_inventory(inventorys,added_item))
print('持ち物リスト：')
result=displey_inventory(inventorys)
print(f"アイテム総数：{result}")