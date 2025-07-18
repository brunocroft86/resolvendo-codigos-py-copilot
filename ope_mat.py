num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == '+':
    print  (num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Operaçaõ inválida.")
