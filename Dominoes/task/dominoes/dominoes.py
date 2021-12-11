# Write your code here
import random

domino_snake = []
full_domino = []
doubles_set = [[0, 0], [1, 1], [3, 3], [2, 2], [5, 5], [4, 4], [6, 6]]
# 1. create full domino set
for i in range(7):
    for j in range(7):
        if [j, i] not in full_domino:
            full_domino.append([i, j])
# 2. split domino pieces
random.shuffle(full_domino)
print(full_domino)
stock_pieces = full_domino[0:13]
#print(stock_pieces)
computer_pieces = full_domino[14:21]
player_pieces = full_domino[22:29]

# 3. determine starting piece and first player
#for i in range(7):
    #if stock_pieces[i][i] == stock_pieces[i][i+1]: