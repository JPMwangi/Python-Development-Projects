from turtle import Turtle
FONT = ('Courier', 24, 'bold')
ALIGNMENT = 'left'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(-265, 265)
        self.level = 1
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level {self.level}', align=ALIGNMENT, font=FONT)
 
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
     