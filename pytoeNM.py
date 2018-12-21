import argparse
class PyToe(object):
	"""tic-tac-toe of any size. You can only win on diagonals if the game is a square"""
	def __init__(self, R, C):
		self.board = [[' ']*C for i in range(R)]
		self.padding_spaces = len(str(R*C))	# size for string of max number in the grid
		self.player = 'X'	# player starts as X
		self.R = R		# number of rows
		self.C = C		# number of cols
	
	# add spaced to the front of the token for padding
	def pad_token(self, token):
		return ' '*(self.padding_spaces - len(token)) + token

	# print the board
	def print_board(self, board):
		board_str = ('\n'+'-'*((3+self.padding_spaces)*self.C-1)+'\n').join(['|'.join([' {} ']*self.C)]*self.R)
		print(board_str.format(*(self.pad_token(e if e != ' ' else str(self.pos_to_place((r, c)))) for r,row in enumerate(board) for c,e in enumerate(row))))	# flatten

	# convert number of user input to array corrdinates
	def place_to_pos(self, place):
		return (place-1) // self.C, (place-1) % self.C

	# convert array corrdinates to number of user input
	def pos_to_place(self, coord):
		return coord[0]*self.C + coord[1] + 1

	def get_at_pos(self, coord):
		return self.board[coord[0]][coord[1]]

	def set_at_pos(self, coord):
		self.board[coord[0]][coord[1]] = self.player

	# garentees return of safe position
	def get_player_pos(self):
		while True:
			place = input(f"Player {self.player.strip()}, where would you like to place (1-{self.R*self.C}): ")
			if place.isdigit() and int(place) in range(1,self.R*self.C+1):
				coord = self.place_to_pos(int(place))
				if self.get_at_pos(coord) == ' ':
					return coord
				print("Ivalid: That place is taken. Chose another.")
			else:
				print("Ivalid: Given place was not a number in the range or 1-{self.R*self.C}. Chose another.")

	# return boolean, last player to place must be winner
	def is_win(self):
		# check rows, cols, diags
		trans_board = tuple(zip(*self.board)) # the transposed (col maj) board
		diag_list = tuple(zip(*((r[i],r[len(r)-i-1]) for i,r in enumerate(self.board)))) if self.R == self.C else []	# only check diags if square
		for b in (self.board, trans_board, diag_list):
			if any((set(r) in ({'X'},{'Y'}) for r in b)):
				return True

	def is_tie(self):
		return all(' ' not in r for r in self.board)

	def play(self):
		self.print_board(self.board)
		while True:
			coord = self.get_player_pos()
			self.set_at_pos(coord)
			self.print_board(self.board)	# pass board
			if self.is_win():
				print(f"Player {self.player.strip()} Wins!")
				break
			elif self.is_tie():
				print("You Tied :(")
				break
			self.player = 'O' if self.player == 'X' else 'X'


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="""Play tic-tac-toe with and NxM sized board. Diagonals are only considered if the board is a square""")
	parser.add_argument('rows', type=int, help="The number of rows in the board")
	parser.add_argument('cols', type=int, help="The number of columns in the board")
	args = parser.parse_args()

	pt = PyToe(args.rows, args.cols)
	pt.play()
