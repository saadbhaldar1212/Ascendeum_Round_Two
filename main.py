import random
        
class Board():
    def __init__(self, board_size: int):
        self.board_size = board_size
        
    def game_board(self, board_size):
        return self.board_size ** 2
              
        
class Game(Board):
    def __init__(self, board_size):
        super().__init__(board_size)
        self.board_size = self.game_board(board_size)
        
        # Can be added in a seperate class `Player`
        self.player1 = "Player 1"
        self.player1_dice_roll_history = []
        self.player1_position_history = []
        self.player1_win_status = 0
        self.player1_position = 0
        
        self.player2 = "Player 2"
        self.player2_dice_roll_history = []
        self.player2_position_history = []
        self.player2_win_status = 0
        self.player2_position = 0
        
        self.player3 = "Player 3"
        self.player3_dice_roll_history = []
        self.player3_position_history = []
        self.player3_win_status = 0
        self.player3_position = 0
        
        self.player4 = "Player 4"
        self.player4_dice_roll_history = []
        self.player4_position_history = []
        self.player4_win_status = 0
        self.player4_position = 0
        
    def dice_roll(self):
        return random.randint(1, 6)
    
    def play(self):
        while True:
            # Can be modularized for 'n' number of players
            self.player1_roll_dice = self.dice_roll()
            self.player1_dice_roll_history.append(self.player1_roll_dice)
            self.player1_position_history.append(self.player1_position)
            self.player1_position += self.player1_roll_dice
            
            if self.player1_position > self.board_size:
                self.player1_position -= self.player1_roll_dice
                
            if self.player1_position == self.board_size:
                self.player1_win_status = 1
                print(f"{self.player1} Winner.\nDice History: {self.player1_dice_roll_history}\nPosition History: {self.player1_position_history}\nWin status: {self.player1_win_status}", end="\n\n")
                print(f"{self.player2}.\nDice History: {self.player2_dice_roll_history}\nPosition History: {self.player2_position_history}\nWin status: {self.player2_win_status}", end="\n\n")
                print(f"{self.player3}.\nDice History: {self.player3_dice_roll_history}\nPosition History: {self.player3_position_history}\nWin status: {self.player3_win_status}", end="\n\n")
                print(f"{self.player4}.\nDice History: {self.player4_dice_roll_history}\nPosition History: {self.player4_position_history}\nWin status: {self.player4_win_status}", end="\n\n")
                break
            
            self.player2_roll_dice = self.dice_roll()
            self.player2_dice_roll_history.append(self.player2_roll_dice)
            self.player2_position_history.append(self.player2_roll_dice)
            
            self.player2_position += self.player2_roll_dice
            
            if self.player2_position > self.board_size:
                self.player2_position -= self.player2_roll_dice
            
            if self.player2_position == self.board_size:
                self.player2_win_status = 1
                print(f"{self.player1}.\nDice History: {self.player1_dice_roll_history}\nPosition History: {self.player1_position_history}\nWin status: {self.player1_win_status}", end="\n\n")
                print(f"{self.player2} Winner.\nDice History: {self.player2_dice_roll_history}\nPosition History: {self.player2_position_history}\nWin status: {self.player2_win_status}", end="\n\n")
                print(f"{self.player3}.\nDice History: {self.player3_dice_roll_history}\nPosition History: {self.player3_position_history}\nWin status: {self.player3_win_status}", end="\n\n")
                print(f"{self.player4}.\nDice History: {self.player4_dice_roll_history}\nPosition History: {self.player4_position_history}\nWin status: {self.player4_win_status}", end="\n\n")
                break
            
            self.player3_roll_dice = self.dice_roll()
            self.player3_dice_roll_history.append(self.player3_roll_dice)
            self.player3_position_history.append(self.player3_position)
            self.player3_position += self.player3_roll_dice
            
            if self.player3_position > self.board_size:
                self.player3_position -= self.player3_roll_dice

            if self.player3_position == self.board_size:
                self.player3_win_status = 1
                print(f"{self.player1}.\nDice History: {self.player1_dice_roll_history}\nPosition History: {self.player1_position_history}\nWin status: {self.player1_win_status}", end="\n\n")
                print(f"{self.player2}.\nDice History: {self.player2_dice_roll_history}\nPosition History: {self.player2_position_history}\nWin status: {self.player2_win_status}", end="\n\n")
                print(f"{self.player3} Winner.\nDice History: {self.player3_dice_roll_history}\nPosition History: {self.player3_position_history}\nWin status: {self.player3_win_status}", end="\n\n")
                print(f"{self.player4}.\nDice History: {self.player4_dice_roll_history}\nPosition History: {self.player4_position_history}\nWin status: {self.player4_win_status}", end="\n\n")
                break
            
            self.player4_roll_dice = self.dice_roll()
            self.player4_dice_roll_history.append(self.player4_roll_dice)
            self.player4_position_history.append(self.player4_position)
            self.player4_position += self.player4_roll_dice
            
            if self.player4_position > self.board_size:
                self.player4_position -= self.player4_roll_dice
            
            if self.player4_position == self.board_size:
                self.player4_win_status = 1
                print(f"{self.player1}.\nDice History: {self.player1_dice_roll_history}\nPosition History: {self.player1_position_history}\nWin status: {self.player1_win_status}")
                print(f"{self.player2}.\nDice History: {self.player2_dice_roll_history}\nPosition History: {self.player2_position_history}\nWin status: {self.player2_win_status}")
                print(f"{self.player3}.\nDice History: {self.player3_dice_roll_history}\nPosition History: {self.player3_position_history}\nWin status: {self.player3_win_status}")
                print(f"{self.player4} Winner.\nDice History: {self.player4_dice_roll_history}\nPosition History: {self.player4_position_history}\nWin status: {self.player4_win_status}", end="\n\n")
                break


game = Game(5)
game.play()
