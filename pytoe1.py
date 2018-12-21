"""
Tic-tac-toe two player game in python
inputs are index of 		1 2 3
							4 5 6
							7 8 9
"""
import numpy as np

def main():
	board = [" "]*9
	player = None	# anything but "O" will become "X"
	while not win(board) and " " in board:
		player = nextPlayer(player)
		board = playerMove(board, player)
		printBoard(board)
	if win(board):
		print (player + " wins!")
	elif " " not in board:
		print ("Tie T^T")

def printBoard(board):
	print(
	"""
	{} | {} | {}
	---------
	{} | {} | {}
	---------
	{} | {} | {}
	""".format(*board)
	)

# checks for a win
# true if win else false
def win(board):
	b = np.array(board).reshape(3, 3)
	row_win = any([compare3(ls3) for ls3 in b])
	col_win = any([compare3(ls3) for ls3 in b.transpose()])
	diag_win = any([compare3(ls3) for ls3 in (b.diagonal(), b[::-1].diagonal())])
	return row_win or col_win or diag_win

# for win()
# checks if list of 3 has same items beside " "
def compare3(ls):
	return ls[0] == ls[1] == ls[2] != " "

# takes input from player and returns the new board
# handles improper inputs
def playerMove(board, player):
	printBoard([b if b != " " else i+1 for i,b in enumerate(board)])		# print board with empty spots as input index
	while True:
		index_input = input(player + " where would you like to move?\n")
		index = getFirstInt(index_input)
		if index != None and board[index-1] == " ":
			board[index-1] = player
			return board
		print("Invalid input. Enter the number of the position of your move (1:9)")
	
# finds first integer(1,9) in input
def getFirstInt(index_input):
	for s in index_input:
		if s.isdigit and int(s) in range(1,10):
			return int(s)

# return the string name of the next player
def nextPlayer(curPlayer):
	if curPlayer == "X":
		return "O"
	return "X"


if __name__ == '__main__':
	main()
