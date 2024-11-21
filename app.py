import math


print("Seja bem vindo a calculadora web!!")
print("Por favor escolha uma das opções a seguir:")

while True:
    escolha = input("Digite 'C' para definir o comprimento dos dois lados de um triângulo retângulo, ou 'A' para definr o comprimento de um lado e o ângulo: ")

    if escolha == "C" or escolha == "c":
        x = float(input("Digite o valor de x: "))
        y = float(input("Digite o valor de y: "))
        z = math.sqrt(math.pow(x,2) + math.pow(y,2))

        pit = math.floor(z)
        print(f'O valor de z é: {pit}')
        
    elif escolha == "A" or escolha == "a":
        x = float(input("Digite o valor do lado (a): "))
        angA = float(input("Digite o valor do ângulo A (em graus): "))  

        # Verifica se os valores são válidos
        if x <= 0 or angA <= 0 or angA >= 180:
         print("O lado deve ser maior que zero e o ângulo deve estar entre 0 e 180 graus.")

        # Converte o ângulo A de graus para radianos
        angA_rad = math.radians(angA)

        # Calcula o comprimento de y usando a Lei dos Senos
        y = (x * math.sin(math.radians(90))) / math.sin(angA_rad)

        # Calcula o ângulo B usando a Lei dos Senos
        angB_rad = math.asin((y * math.sin(angA_rad)) / x)
        angB = math.degrees(angB_rad)

        # Calcula o ângulo C
        angC = 180 - angA - angB

        # Calcula o comprimento do lado C usando a Lei dos Cossenos
        z = math.sqrt(math.pow(x,2) + math.pow(y,2)- 2 * x * y * math.cos(math.radians(angC)))
        

        print("\nResultados:")
        print(f"Lado A: {math.floor(x)}")
        print(f"Lado B: {math.floor(y)}")
        print(f"Lado C: {math.floor(z)}")
        print(f"Ângulo A: {math.floor(angA)} graus")
        print(f"Ângulo B: {math.floor(angB)} graus")
        print(f"Ângulo C: {math.floor(angC)} graus")

    else:
        print("Opção inválida")
        break
