'''
The question is in this link
https://github.com/vedhavyas/battleship 

###Input File Input file should be of the following format
GridSize (0<M<10)
Number of ships for each player
Player 1 ship positions, should be of format x1,y1:x2,y2:x3,y3:x4,y4
Player 2 ship positions, should be of format x1,y1:x2,y2:x3,y3:x4,y4
Total number of missiles for each player (0<T<100)
Player 1 Moves, should be of format x1,y1:x2,y2:x3,y3:x4,y4
Player 2 Moves, should be of format x1,y1:x2,y2:x3,y3:x4,y4

###Output file Program requires an output file to write the result back to the file. If file does not exist, one will be created. If file exists, then the data is overwritten
##Output Programs sample output in the Output File will look as follows.
Player1
O O _ _ _
_ B O _ _
B _ _ X _
_ _ _ _ B
_ _ _ X _
Player2
_ X _ _ _
_ _ _ _ _
_ _ _ X _
B O _ _ B
_ X _ O _

P1: 3
P2: 2
Player1 wins
'''

class Solution:
    def __init__(self, gridsize, ships):
        self.gridsize   = gridsize
        # Board has values:
        # 0 - nothing at that position      ( - )
        # 1 - a ship placed at that pos     ( B )
        # 2 - the bomb hit the ship         ( X )
        # 3 - the bomb missed the ship      ( O )
        self.map        = {0 : '_', 1 : 'B', 2 : 'X', 3 : 'O'}
        # Boards for 2 players
        self.board1     = [[0 for i in range(gridsize)] for j in range(gridsize)]
        self.board2     = [[0 for i in range(gridsize)] for j in range(gridsize)]
        self.ships      = ships

        # Player1 and Player2's hit numbers
        self.hit1       = 0
        self.hit2       = 0

    def place_ships(self, player1, player2):
        for i in range(0, len(player1), 2):
            self.board1[player1[i]][player1[i+1]] = 1

        for i in range(0, len(player2), 2):
            self.board2[player2[i]][player2[i+1]] = 1

    def missile_battle(self, missiles1, missiles2):
        for i in range(0, len(missiles1), 2):
            if self.board2[missiles1[i]][missiles1[i+1]] == 1:
                self.board2[missiles1[i]][missiles1[i+1]] = 2
                self.hit1 += 1
            else:
                self.board2[missiles1[i]][missiles1[i+1]] = 3

        for i in range(0, len(missiles2), 2):
            if self.board1[missiles2[i]][missiles2[i+1]] == 1:
                self.board1[missiles2[i]][missiles2[i+1]] = 2
                self.hit2 += 1
            else:
                self.board1[missiles2[i]][missiles2[i+1]] = 3
            
    def print_board(self):
        print("Player1")
        for i in self.board1:
            for j in i:
                print(self.map[j], end=' ')
            print()
        
        print("Player2")
        for i in self.board2:
            for j in i:
                print(self.map[j], end=' ')
            print()
        
        print("P1", self.hit1)
        print("P2", self.hit2)

        if self.hit1 == self.hit2:
            print("It's a draw")
        elif self.hit1 > self.hit2:
            print("Player1 wins")
        else:
            print("Player2 wins")

    def fill_board(self, player1_ships, player2_ships, player1_mis, player2_mis):
        self.place_ships(player1_ships, player2_ships)
        self.missile_battle(player1_mis, player2_mis)
        self.print_board()

battle = Solution(int(input()), int(input()))
player1_ships = list(map(int, input().strip().split()))
player2_ships = list(map(int, input().strip().split()))
missiles = int(input())
player1_missile = list(map(int, input().strip().split()))
player2_missile = list(map(int, input().strip().split()))
battle.fill_board(player1_ships, player2_ships, player1_missile, player2_missile)
