grid=[['.','.','.','.','.','.'],
      ['.','O','O','.','.','.'],
      ['O','O','O','O','.','.'],
      ['O','O','O','O','O','.'],
      ['.','O','O','O','O','O'],
      ['O','O','O','O','O','.'],
      ['O','O','O','O','.','.'],
      ['.','O','O','.','.','.'],
      ['.','.','.','.','.','.']]
WIDTH=6
HEIGTH=9
for x in range(WIDTH):
    for y in range(HEIGTH):
        print(grid[y][x-6],end='')
    print()