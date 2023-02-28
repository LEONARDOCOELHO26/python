import tkinter as tk
import random
root = tk.Tk()
root.title("Login Screen")
root.attributes("-fullscreen", True)
bot = 0 
player = 0
class Login:
    def pedra(self):
        guess = 0
        random_number = random.randint(0, 2)
        self.chose.config(text=f"{random_number} | {guess}", fg="black", font=('Times New Roman', 50, 'bold'))
        if guess == 0 and random_number == 0:
            self.result.config(text=f"empate", fg="blue",font=('Times New Roman', 22))
        elif guess == 0 and random_number == 1:
            self.result.config(text=f"Derrota", fg="red",font=('Times New Roman', 22))
            bot = bot + 1
            self.point.config(text=f"\nbot:{bot} | player:{player}", fg="black",font=('Times New Roman', 22))
        elif guess == 0 and random_number == 2:
            self.result.config(text=f"Vitoria", fg="green")
            player = player + 1
    def tesoura(self):
        guess = 2
        random_number = random.randint(0, 2)
        self.chose.config(text=f"{random_number} | {guess}", fg="black",font=('Times New Roman', 50, 'bold'))
        if guess == 2 and random_number == 2:
            self.result.config(text=f"empate", fg="blue")
        elif guess == 2 and random_number == 0:
            self.result.config(text=f"Derrota", fg="red")
            bot = bot + 1
            self.point.config(text=f"{bot}", fg="black")
        elif guess == 2 and random_number == 1:
            self.result.config(text=f"Vitoria", fg="green")
            player = player + 1
    def papel(self):
        guess = 1
        random_number = random.randint(0, 2)
        self.chose.config(text=f"{random_number} | {guess}", fg="black",font=('Times New Roman', 50, 'bold'))
        if guess == 1 and random_number == 1:
            self.result.config(text=f"empate", fg="blue")
        elif guess == 1 and random_number == 2:
            self.result.config(text=f"Derrota", fg="red")
            bot = bot + 1
            self.point.config(text=f"{bot}", fg="black")
        elif guess == 1 and random_number == 0:
            self.result.config(text=f"Vitoria", fg="green")
            player = player + 1
          
    def __init__(self, root):
        self.chose = tk.Label(root, text="")
        self.chose.pack()
        
        self.result = tk.Label(root, text="")
        self.result.pack()

        self.point = tk.Label(root, text=f"")
        self.point.pack()
        
        self.pedra_button = tk.Button(root, text="pedra", command=self.pedra)
        self.pedra_button.pack()
        self.pedra_button.place(x=600, y=150)

        self.papel_button = tk.Button(root, text="papel", command=self.papel)
        self.papel_button.pack()
        self.papel_button.place(x=650, y=150)
        # Create a login button
        self.tesoura_button = tk.Button(root, text="tesoura", command=self.tesoura)
        self.tesoura_button.pack()
        self.tesoura_button.place(x=700, y=150)

        self.quit_button = tk.Button(root, text="Quit", command=quit)
        self.quit_button.pack()
        self.quit_button.place(x=650, y=200)


login = Login(root)

# Start the window's event loop
root.mainloop()
  