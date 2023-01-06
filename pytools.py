#função de limpesa de console
import os

def clear_console():
    os.system('cls')

clear_console()

#calendar
import calendar
year = int(input("Digite o ano "))
month = int(input("Digite o mes "))

clear_console()
print(calendar.month (year, month))

#gerador de senhas

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*?/|çÇ()_- "

size = int(input("qual o tamanho da senha "))
clear_console()
Use_for =lower_case + upper_case + number + symbols
length_for_pass = size
password = "".join(random.sample(Use_for, length_for_pass))

print("senha:", password)

#internet speed test


import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()
print("Download",int(down_speed))
print("Upload",int(up_speed))

