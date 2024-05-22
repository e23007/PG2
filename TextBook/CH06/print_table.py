table_data=[['apple','oranges','cherries','banana'],
            ['Alice','Bob','Carol','Dvid'],
            ['dogs','cats','moose','goose']]

def print_table(table_data):
    print(f"{table_data[0]: >10}{table_data[1]: >10}{table_data[2]: >10}")


list(map(print_table,table_data))
