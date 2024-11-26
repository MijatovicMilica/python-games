import turtle as t

# Kreiranje prozora za prikaz dugmeta
window = t.Screen()
window.title("Test dugmeta")
window.bgcolor("dark red")
window.setup(width=400, height=300)

# Kreiranje dugmeta (pravougaonik)
play_button = t.Turtle()
play_button.shape("square")
play_button.color("gold")
play_button.shapesize(stretch_wid=4, stretch_len=6)  # Podesi veličinu pravougaonika
play_button.penup()
play_button.goto(0, 0)  # Pozicija na sredini ekrana

# Kreiranje teksta za dugme PLAY
play_button_text = t.Turtle()
play_button_text.penup()
play_button_text.hideturtle()  # Sakrij kornjaču koja piše tekst, da ne bi prikazala strelicu
play_button_text.color("black")
play_button_text.goto(0, -10)  # Podešavanje pozicije teksta na centru pravougaonika
play_button_text.write("PLAY", align="center", font=('Arial', 25, 'bold'))

# Funkcija za klik na dugme
def on_click(x, y):
    if -60 < x < 60 and -40 < y < 40:  # Proverava da li je klik unutar dugmeta
        print("Dugme je pritisnuto!")  # Izvrši neku akciju

# Reagovanje na klik u okviru dugmeta
window.onclick(on_click)

# Pokreni prozor
window.mainloop()