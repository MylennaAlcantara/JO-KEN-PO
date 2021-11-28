from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

jogador = int(input("Qual a sua jogada? "))
print("#=#" *15)
print("Você jogou: {}" .format(itens[jogador]))
print('Computador joga: {}' .format(itens[computador]))
print("#=#" *15)

print("#=#" *15)
if itens[computador] == itens[0] and itens[jogador] == itens[1]:
    print("VOCÊ GANHOU!!")
elif itens[computador] == itens[0] and itens[jogador] == itens[2]:
    print("COMPUTADOR GANHOU!!")
elif itens[computador] == itens[1] and itens[jogador] == itens[0]:
    print("COMPUTADOR GANHOU!!")
elif itens[computador] == itens[1] and itens[jogador] == itens[2]:
    print("VOCÊ GANHOU!!")
elif itens[computador] == itens[2] and itens[jogador] == itens[1]:
    print("COMPUTADOR GANHOU!!")
elif itens[computador] == itens[2] and itens[jogador] == itens[3]:
    print("VOCÊ GANHOU!!")
else:
    print("EMPATE!!")

print("#=#" *15)