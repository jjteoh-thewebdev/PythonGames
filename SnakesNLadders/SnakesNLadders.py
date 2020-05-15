# modified from my solution for kata on codewars.com
# Rules:
# climb or fall if step on snakes or ladders
# reach exact 100 to win the game
# if exceed 100, move backward

class SnakesLadders():

    def __init__(self):
        # key = step-on, value = drop-to
        self.snakes = { 16: 6, 
                        46: 25, 
                        49: 11, 
                        62: 19, 
                        64: 60, 
                        74: 53, 
                        89: 68, 
                        92: 88, 
                        95: 75, 
                        99: 80 }
        
        # key = step-on, value = climb-to
        self.ladders = { 2: 38,
                         7: 14,
                         8: 31,
                         15: 26,
                         21: 42,
                         28: 84,
                         36: 44,
                         51: 67,
                         71: 91,
                         78: 98,
                         87: 94 }

        self.players = { 1:0, 2:0 } 
        self.turn = 1
    
    # check step on snakes or ladders
    def fallOrClimb(self, sqr):
        return self.snakes.get(sqr, 0) + self.ladders.get(sqr, 0) or sqr

    def updatePosition(self, die1, die2):
        sqr = die1 + die2 + self.players[self.turn]

        # move backward if overlap
        if sqr > 100: 
            sqr = 200 - sqr

        # check step on snakes or ladders
        sqr = self.fallOrClimb(sqr)

        self.players[self.turn] = sqr

        return sqr
    
    # if one player reach exact 100, game is over 
    def isGameOver(self):
        return 100 in self.players.values()

    def play(self, die1, die2):
        # check gameover
        if self.isGameOver(): 
            return 'Game over!'
        
        # update current player position
        sqr = self.updatePosition(die1, die2)
        
        # return msg
        if self.isGameOver(): 
            msg = f'Player {self.turn} Wins!'
        else: 
            msg = f'Player {self.turn} is on square {sqr}'

        # if same dices, gain extra turn
        if die1 != die2:
            self.turn = 2 if self.turn == 1 else 1
        
        return msg

game = SnakesLadders()
print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
print(game.play(1, 1))




