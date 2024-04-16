from random import randint

computador = randint(0, 10)
print("Sou seu computador")
print("Acabei de pensar em um número entre 0 e 10.")
acertou = False
palpite = 0

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print(f"Acertou! O número que pensei foi {computador}")
print(f"Você acertou na {palpite}ª tentativa.")