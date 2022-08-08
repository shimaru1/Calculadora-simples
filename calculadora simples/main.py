# Calculadora Simples
numero1 = 0
numero2 = 0
resultado = 0
operacao = ''
while true:
    numero1 = int(input("Digite o Primeiro numero"))
    operacao = input('Digite a operação')
    numero2 = int(input("Digite o Segundo numero"))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    else:
        resultado = "Operaçõa invalida"
    print(str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = ' + str(resultado))

