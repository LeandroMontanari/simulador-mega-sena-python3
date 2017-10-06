################################################
##### PROGRAMADO POR: LEANDRO L. MONTANARI #####
################################################

# Importações
from random import randint

# Variáveis Iniciais
listadechutes = []
sorteio = 0

### SORTEIO INICIAL ###

# Lista de Bolas
listadebolas = []

# Sorteio das Bolas 1 a 6
bola1 = randint(1,60)
bola2 = randint(1,60)
bola3 = randint(1,60)
bola4 = randint(1,60)
bola5 = randint(1,60)
bola6 = randint(1,60)

# Sorteio da Bola 2 novamente se for repetida
while bola2 == bola1:
    bola2 = randint(1,60)

# Sorteio da Bola 3 novamente se for repetida
while bola3 == bola2 or bola3 == bola1:
    bola3 = randint(1,60)

# Sorteio da Bola 4 novamente se for repetida
while bola4 == bola3 or bola4 == bola2 or bola4 == bola1:
    bola4 = randint(1,60)

# Sorteio da Bola 5 novamente se for repetida
while bola5 == bola4 or bola5 == bola3 or bola5 == bola2 or bola5 == bola1:
    bola5 = randint(1,60)

# Sorteio da Bola 6 novamente se for repetida
while bola6 == bola5 or bola6 == bola4 or bola6 == bola3 or bola6 == bola2 or bola6 == bola1:
    bola6 = randint(1,60)

# Inclusão das bolas na lista
listadebolas.append(bola1)
listadebolas.append(bola2)
listadebolas.append(bola3)
listadebolas.append(bola4)
listadebolas.append(bola5)
listadebolas.append(bola6)

### CHUTES ###

# Texto explicativo
print("""
#############################################
##### SIMULADOR DE APOSTAS NA MEGA SENA #####
#############################################
      """)
print("Digite os números que deseja apostar (de 1 a 60 em cada bola, sem repeti-los):")
print("")

# Chute da Bola 1
while True:
    try:
        chute1 = int(input("Bola 1: "))

        # Verifica se o valor digitado é entre 1 e 60
        while chute1 < 1 or chute1 > 60:
            print("")
            print("Número inválido! Digite um número de 1 a 60.")
            print("")
            chute1 = int(input("Bola 1: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Chute da Bola 2
while True:
    try:
        chute2 = int(input("Bola 2: "))

        # Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while chute2 < 1 or chute2 > 60 or chute2 == chute1:
            print("")
            print("Número inválido ou repetido! Digite um número de 1 a 60, sem repetir os anteriores.")
            print("")
            chute2 = int(input("Bola 2: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Chute da Bola 3
while True:
    try:
        chute3 = int(input("Bola 3: "))

        # Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while chute3 < 1 or chute3 > 60 or chute3 == chute2 or chute3 == chute1:
            print("")
            print("Número inválido ou repetido! Digite um número de 1 a 60, sem repetir os anteriores.")
            print("")
            chute3 = int(input("Bola 3: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Chute da Bola 4
while True:
    try:
        chute4 = int(input("Bola 4: "))

        # Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while chute4 < 1 or chute4 > 60 or chute4 == chute3 or chute4 == chute2 or chute4 == chute1:
            print("")
            print("Número inválido ou repetido! Digite um número de 1 a 60, sem repetir os anteriores.")
            print("")
            chute4 = int(input("Bola 4: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Chute da Bola 5
while True:
    try:
        chute5 = int(input("Bola 5: "))

        # Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while chute5 < 1 or chute5 > 60 or chute5 == chute4 or chute5 == chute3 or chute5 == chute2 or chute5 == chute1:
            print("")
            print("Número inválido ou repetido! Digite um número de 1 a 60, sem repetir os anteriores.")
            print("")
            chute5 = int(input("Bola 5: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Chute da Bola 6
while True:
    try:
        chute6 = int(input("Bola 6: "))

        # Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while chute6 < 1 or chute6 > 60 or chute6 == chute5 or chute6 == chute4 or chute6 == chute3 or chute6 == chute2 or chute6 == chute1:
            print("")
            print("Número inválido ou repetido! Digite um número de 1 a 60, sem repetir os anteriores.")
            print("")
            chute6 = int(input("Bola 6: "))
        
        break

    # Verifica se o valor digitado é um número inteiro
    except ValueError:
        print("")
        print("Valor inválido! Digite um número de 1 a 60.")
        print("")

# Espaço
print("")

# Inclusão dos chutes na lista
listadechutes.append(chute1)
listadechutes.append(chute2)
listadechutes.append(chute3)
listadechutes.append(chute4)
listadechutes.append(chute5)
listadechutes.append(chute6)

# Organização das listas
org_chutes = sorted(listadechutes)
org_bolas = sorted(listadebolas)

### REPETIÇÃO DO SORTEIO ###

print("Calculando a quantidade de sorteios necessários para você ganhar com as bolas {}...".format(org_chutes))
print("\nEste processo pode demorar desde poucos segundos até vários minutos. Seja paciente!\n")

while org_chutes != org_bolas:
    sorteio += 1

    # Lista de Bolas
    listadebolas = []

    # Sorteio das Bolas 1 a 6
    bola1 = randint(1,60)
    bola2 = randint(1,60)
    bola3 = randint(1,60)
    bola4 = randint(1,60)
    bola5 = randint(1,60)
    bola6 = randint(1,60)

    # Sorteio da Bola 2 novamente se for repetida
    while bola2 == bola1:
        bola2 = randint(1,60)

    # Sorteio da Bola 3 novamente se for repetida
    while bola3 == bola2 or bola3 == bola1:
        bola3 = randint(1,60)

    # Sorteio da Bola 4 novamente se for repetida
    while bola4 == bola3 or bola4 == bola2 or bola4 == bola1:
        bola4 = randint(1,60)

    # Sorteio da Bola 5 novamente se for repetida
    while bola5 == bola4 or bola5 == bola3 or bola5 == bola2 or bola5 == bola1:
        bola5 = randint(1,60)

    # Sorteio da Bola 6 novamente se for repetida
    while bola6 == bola5 or bola6 == bola4 or bola6 == bola3 or bola6 == bola2 or bola6 == bola1:
        bola6 = randint(1,60)

    # Inclusão das bolas na lista
    listadebolas.append(bola1)
    listadebolas.append(bola2)
    listadebolas.append(bola3)
    listadebolas.append(bola4)
    listadebolas.append(bola5)
    listadebolas.append(bola6)

    # Organização das bolas em ordem crescente
    org_bolas = sorted(listadebolas)

else:
    sorteio += 1
    # Exibição dos chutes e das bolas sorteadas
    print("Suas Bolas (em ordem crescente)     :", org_chutes[0], org_chutes[1], org_chutes[2], org_chutes[3], org_chutes[4], org_chutes[5])
    print("Bolas Sorteadas (em ordem crescente):", org_bolas[0], org_bolas[1], org_bolas[2], org_bolas[3], org_bolas[4], org_bolas[5])
    print("")
    print("Após",sorteio,"tentativas, você acertou!")
    input("")
