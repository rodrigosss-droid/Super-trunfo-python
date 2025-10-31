import random

# Cartas do jogo (cada carta é um dicionário com atributos)
cartas = [
    {"nome": "Dragão Flamejante", "ataque": 90, "defesa": 70, "magia": 85},
    {"nome": "Guerreiro da Luz", "ataque": 75, "defesa": 80, "magia": 60},
    {"nome": "Mago Sombrio", "ataque": 60, "defesa": 55, "magia": 95},
    {"nome": "Elfa Arqueira", "ataque": 80, "defesa": 65, "magia": 70}
]

print("🔥 Bem-vindo ao Super Trunfo - Versão Python!")
print("Escolha uma carta para jogar:\n")

# Mostra as opções para o jogador escolher
for i, carta in enumerate(cartas):
    print(f"{i+1}. {carta['nome']}")

# Jogador escolhe uma carta
escolha = int(input("\nDigite o número da carta que você quer usar: ")) - 1
carta_jogador = cartas[escolha]

# Computador escolhe uma carta aleatória
carta_pc = random.choice(cartas)

print("\n✨ Sua carta:")
print(carta_jogador)
print("\n🤖 Carta do Computador:")
print(carta_pc)

# Jogador escolhe o atributo
print("\nAtributos disponíveis: ataque, defesa, magia")
atributo = input("Qual atributo você quer usar? ").lower()

valor_jogador = carta_jogador[atributo]
valor_pc = carta_pc[atributo]

print(f"\nVocê escolheu comparar o atributo **{atributo}**!")
print(f"Sua carta: {valor_jogador} x Carta do PC: {valor_pc}")

# Decide o vencedor
if valor_jogador > valor_pc:
    print("\n✅ Você venceu! Boa escolha! 😎")
elif valor_jogador < valor_pc:
    print("\n❌ Você perdeu! O PC foi melhor dessa vez...")
else:
    print("\n🔹 Empate! Foi por pouco!")
