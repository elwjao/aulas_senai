def somar_tudo(numeros):
    return sum(numeros)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

soma = somar_tudo([num1, num2, num3])
print("A soma dos números é:", soma)