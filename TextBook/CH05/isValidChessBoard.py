chess={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}
position_check=[]
for x in range(1,9):
    for y in range(1,9):
        position_check.append(str(x)+chr(y+96))


def chess_check(chess,position_check):
    piece_check=['pawn','knight','bishop','rook','queen','king']
    for position,piece in chess.items():
        if position not in position_check:
            print(position)
            return False
        if piece[1:] not in piece_check:
            print(piece)
            return False
        elif piece[0:1]!='w' and piece[0:1]!='b':
            return False
    return True


print(chess_check(chess,position_check))