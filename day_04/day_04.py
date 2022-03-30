import numpy as np
from itertools import product

with open("day_04/input.txt") as fp:
    draws = list(map(int, fp.readline().split(",")))
    boards = [np.mat(board.replace("\n", ";")) for board in fp.read()[1:-1].split("\n\n")] 
    
won_boards = set()
firstWin = True
firstWinnerScore = 0 
for draw, (idx, board) in product(draws, enumerate([np.ma.masked_array(board) for board in boards])):
    board.mask |= board.data == draw
    if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
        if firstWin:
            firstWinnerScore = board.sum()*draw
            firstWin = False
        if idx not in won_boards and len(won_boards) == len(boards) -1:
            lastWinner = board.sum()*draw
            break
        won_boards.add(idx)
print("\np1 result: ", firstWinnerScore ,"\np2 result : ", lastWinner,"\n")