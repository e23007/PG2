table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# 最大の桁数を見つける
max_width = len(str(max(max(row) for row in table_data)))

def print_table(table_data,max_width):
    for i in range(len(table_data[0])):
        # 各要素を右寄せにして幅を揃える
        print("".join(str(line[i]).rjust(max_width) for line in table_data))


print_table(table_data,max_width)