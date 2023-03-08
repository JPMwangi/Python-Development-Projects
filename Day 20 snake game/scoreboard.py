from turtle import Turtle
FONT = ('Courier', 24, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.ht()
        self.goto(0, 265)
        self.score = 0
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.write(f'Score {self.score}', align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        
     