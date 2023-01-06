maior_idade = 18
idade_especial = 17

import os

def clear_console():
    os.system('cls')

##função curta
status = "sUCESSO" if saldo == sque else "falha"

idade = int(input("informe sua idade"))

if idade >= maior_idade:
    print("pode tirar a CNH")
if idade < maior_idade:
    print("não pode tirar a CNH")


if idade >= maior_idade:
    print("pode tirar a CNH")
else:
    print("não pode tirar a CNH")

if idade >= maior_idade:
    print("pode tirar a CNH")
elif idade == idade_especial:
    print(" pode fazer aulas teoricas")
else:
    print("não pode tirar a CNH")

