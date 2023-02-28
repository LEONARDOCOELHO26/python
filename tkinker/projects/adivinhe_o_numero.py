import random
def guess(x):
    x = int(input("limite"))
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"numero é entre 1 e {x}"))
        if guess < random_number:
            print("este numero é muito pequeno")
        elif guess > random_number:
            print("este numero é muito grande")
        
    print(f"voce acertou o numero é {random_number}")

guess(10)