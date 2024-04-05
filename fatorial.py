x = int(input("escolha um número: "))
def fatorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    elif x < 0:
        return "Isso aí existe, não, meu fi"
    else:
        return x * fatorial(x-1)

print(fatorial(x))
