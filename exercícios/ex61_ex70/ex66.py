n = s = cont =  0

while True:
    n = int(input('Digite um número [999 é para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f"Foi digitado {cont} e a soma de todos os números é {s}")