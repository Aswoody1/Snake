from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 270)
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("data.txt", mode="w") as data:
                    data.write(str(self.high_score))
            self.clear()
            self.write(f"Score = {self.score} High Score:{self.high_score}", font=FONT, align = ALIGNMENT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", font = FONT, align = ALIGNMENT)






