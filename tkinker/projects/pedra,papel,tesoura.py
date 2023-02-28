import random
def guess():
    bot = 0 
    player = 0
    while True:
        random_number = random.randint(0, 2)
        guess = int(input(f"escolha entre pedra(0), papel(1), tesoura(2): "))
        if guess == 0 and random_number == 0 or guess == 1 and random_number == 1 or guess == 2 and random_number == 2:
            print("empate")
            print(f"\nbot:{bot} | player:{player}")
        elif guess == 0 and random_number == 2:
            print("pedra ganhou")
            player = player + 1
            print(f"\nbot:{bot} | player:{player}")
        elif random_number == 0 and guess == 2:
            print("pedra ganhou")
            bot = bot + 1
            print(f"\nbot:{bot} | player:{player}")
        elif guess == 2 and random_number == 1 :
            print("tesoura ganhou")
            player = player + 1
            print(f"\nbot:{bot} | player:{player}")
        elif random_number == 2 and guess == 1:
            print("tesoura ganhou")
            bot = bot + 1
            print(f"\nbot:{bot} | player:{player}")
        elif guess == 0 and random_number == 1 :
            print("papel ganhou")
            player = player + 1
            print(f"\nbot:{bot} | player:{player}")      
        elif random_number == 0 and guess == 1:
            print("papel ganhou") 
            bot = bot + 1
            print(f"\nbot:{bot} | player:{player}") 
        elif guess >= 3:
            print("numero invalido")

guess()