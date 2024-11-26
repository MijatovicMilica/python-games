import turtle as t
import winsound

playerAscore = 0
playerBscore = 0
game_started = False

#kreiranje prozora za igru
window = t.Screen()
window.title("LOPTICA SKOCICA")
window.bgcolor("dark red")
window.setup(width=800, height=600)
window.tracer(0)

#kreiranje levog gola
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#kreiranje desnog gola
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

#kreiranje lopte
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.5
ballydirection = 0.5

#kreiranje olovke za rezultat
pen = t.Turtle()
pen.speed(0)
pen.color("gold")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("REZULTAT", align="center", font=('Impact', 15, 'italic'))

#kreiranje dugmeta play
play_button = t.Turtle()
play_button.shape("square")
play_button.color("gold")
play_button.shapesize(stretch_wid=4, stretch_len=6)
play_button.penup()
play_button.goto(0, 0)
window.update()
# Kreiranje teksta za dugme PLAY
play_button_text = t.Turtle()
play_button_text.penup()
play_button_text.hideturtle()
play_button_text.color("black")
play_button_text.goto(0, -10)

window.update()

def display_play_text():
    play_button_text.clear()
    play_button_text.write("PLAY", align="center", font=('Arial', 25, 'bold'))
window.update()
#funkcije za pomeranje golova
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 50
    leftpaddle.sety(y)
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 50
    leftpaddle.sety(y)
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 50
    rightpaddle.sety(y)
def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 50
    rightpaddle.sety(y)

# Funkcija za startovanje igre
def start_game():
    global game_started, playerAscore, playerBscore
    if not game_started:
        game_started = True
        playerAscore = 0
        playerBscore = 0
        pen.clear()
        pen.write("{}    REZULTAT    {}".format(playerAscore, playerBscore), align="center", font=('Impact', 15, 'italic'))
        play_button.hideturtle()
        play_button_text.clear()
window.update()
# Funkcija za resetovanje igre
def reset_game():
    global game_started, playerAscore, playerBscore
    game_started = False
    playerAscore = 0
    playerBscore = 0
    pen.clear()
    play_button.showturtle()  # Prikazuje dugme
    display_play_text()
window.update()
# Funkcija za klik na dugme PLAY
def on_click(x, y):
    if -60 < x < 60 and -40 < y < 40:
        start_game()
window.update()
# Dodavanje događaja na klik
window.onclick(on_click)
display_play_text()

#tasteri za upravljanje
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()
    if not game_started:
        continue

    #pomeranje lopte
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0 ,0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("{}    REZULTAT    {}".format(playerAscore, playerBscore), align="center", font=('Impact', 15, 'italic'))
        winsound.PlaySound("go.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("{}    REZULTAT    {}".format(playerAscore, playerBscore), align="center", font=('Impact', 15, 'italic'))
        winsound.PlaySound("go.wav", winsound.SND_ASYNC)
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        winsound.PlaySound("odbijanje.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ballxdirection = ballxdirection * -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        winsound.PlaySound("odbijanje.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ballxdirection = ballxdirection * -1

    if playerAscore >= 5:
        pen.clear()
        reset_game()
        pen.write("Player A wins!", align="center", font=('Monaco', 22, 'italic', 'bold'))
    elif playerBscore >= 5:
        pen.clear()
        reset_game()
        pen.write("Player B wins!", align="center", font=('Monaco', 22, 'italic', 'bold'))

