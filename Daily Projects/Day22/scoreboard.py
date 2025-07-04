from turtle import Turtle
ALIGNMENT = "center"
FONT = ("FiraMono Nerd Font", 56, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)
        
