import random,time,copy,sys

WIDTH=60
HEIGTH=20

next_cells=[]
try:
    for x in range(WIDTH):
        column=[]
        for y in range(HEIGTH):
            if random.randint(0,1)==0:
                column.append('#')
            else:
                column.append(' ')
        next_cells.append(column)

    while True:
        print('\n\n\n\n\n')
        current_cells=copy.deepcopy(next_cells)
        for y in range(HEIGTH):
            for x in range(WIDTH):
                print(current_cells[x][y],end='')
            print()

        for x in range(WIDTH):
            for y in range(HEIGTH):
                left_coord=(x-1)%WIDTH
                right_coord=(x+1)%WIDTH
                above_coord=(y-1)%HEIGTH
                below_coord=(y+1)%HEIGTH

                num_neighbors=0
                if current_cells[left_coord][above_coord]=='#':
                    num_neighbors+=1
                if current_cells[x][above_coord]=='#':
                    num_neighbors+=1
                if current_cells[right_coord][above_coord]=='#':
                    num_neighbors+=1
                if current_cells[left_coord][y]=='#':
                    num_neighbors+=1
                if current_cells[right_coord][y]=='#':
                    num_neighbors+=1
                if current_cells[left_coord][below_coord]=='#':
                    num_neighbors+=1
                if current_cells[x][below_coord]=='#':
                    num_neighbors+=1
                if current_cells[right_coord][below_coord]=='#':
                    num_neighbors+=1
                if (current_cells[x][y]=='#' and (num_neighbors==2 or num_neighbors==3)):
                    next_cells[x][y]='#'
                elif current_cells[x][y]==' ' and num_neighbors==3:
                    next_cells[x][y]='#'
                else:
                    next_cells[x][y]=' '
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()