# print the board
def print_board(board):
	print ("""
	 {} | {} | {}
	-----------
	 {} | {} | {}
	-----------
	 {} | {} | {}
	""".format(*(e for r in board for e in r)))

# print the board with 1-9 as those are the numbers the user
# should use to place at that cell
def print_board_pos():
	print_board((range(i*3+1,i*3+4) for i in range(3)))

# convert number of user input to array corrdinates
def place_to_pos(place):
	return (place-1) // 3, (place-1) % 3

def get_at_pos(coord, board):
	return board[coord[0]][coord[1]]

def set_at_pos(player, coord, board):
	board[coord[0]][coord[1]] = player

# garentees return of safe position
def get_player_pos(player, board):
	while True:
		place = input(f"Player {player}, where would you like to place (1-9): ")
		if place.isdigit() and int(place) in range(1,10):
			coord = place_to_pos(int(place))
			if get_at_pos(coord, board) == ' ':
				return coord
			else:
				print("Ivalid: That place is taken. Chose another.")
		else:
			print("Ivalid: Given place was not a number in the range or 1-9. Chose another.")

# return boolean, last player to place must be winner
def is_win(board):
	# check rows, cols, diags
	trans_board = tuple(zip(*board)) # the transposed (col maj) board
	diag_list = tuple(zip(*((r[i],r[len(r)-i-1]) for i,r in enumerate(board))))
	for b in (board, trans_board, diag_list):
		if any((set(r) in ({'X'},{'O'}) for r in b)):
			return True

def is_tie(board):
	return all(' ' not in r for r in board)

def main(player, board):
	print_board_pos()
	while True:
		coord = get_player_pos(player, board)
		set_at_pos(player, coord, board)
		print_board(board)
		if is_win(board):
			print(f"Player {player} Wins!")
			break
		elif is_tie(board):
			print("You Tied :(")
			break
		player = 'O' if player == 'X' else 'X'


if __name__ == '__main__':
	board = [[' ']*3 for i in range(3)]
	start_player = 'X'
	main(start_player, board)
