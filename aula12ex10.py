"""Crie um programa que faça o computador jogar jokenpô com você"""

from random import randint
from time import sleep

print("\n\n=========== VAMOS JOGAR JOKENPÔ ===========")
print("\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura")
opcao = int(input("Escolha: "))
auxopcao = opcao - 1

seuJogo = opcao - 1
if seuJogo == 0:
    seuJogo = "Pedra"
elif seuJogo == 1:
    seuJogo = "Papel"
else:
    seuJogo = "Tesoura"

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")

print("\nVocê escolheu: {}".format(seuJogo))

itens = ("Pedra", "Papel", "Tesoura")
PC = randint (0, 2)

print("Computador escolheu:", itens[PC])

"""if auxopcao == 0 and PC == 2:
    print("\nVOCÊ VENCEU!")
elif auxopcao == 0 and PC == 1:
    print("\nVOCÊ PERDEU!")
elif auxopcao == 1 and PC == 0:
    print("\nVOCÊ VENCEU!")
elif auxopcao == 1 and PC == 2:
    print("\nVOCÊ PERDEU!")
elif auxopcao == 2 and PC == 1:
    print("\nVOCÊ VENCEU!")
elif auxopcao == 2 and PC == 0:
    print("\nVOCÊ PERDEU!")
elif auxopcao == PC:
    print("\nEMPATE!")"""

#Código otimizado

if (auxopcao == 0 and PC == 2) or (auxopcao == 1 and PC == 0) or (auxopcao == 2 and PC == 1):
    print("\nVOCÊ VENCEU!")
elif (auxopcao == 0 and PC == 1) or (auxopcao == 1 and PC == 2) or (auxopcao == 2 and PC == 0):
    print("\nVOCÊ PERDEU!")
elif auxopcao == PC:
    print("\nEMPATE!")