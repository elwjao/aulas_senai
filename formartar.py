def formatar_real_replace(valor):
    texto = f"R$ {valor:,.2f}"  #padrao EUA 1,234.56
    texto = texto.replace(".","X")
    texto = texto.replace(",",",")
    texto = texto.replace("X",".")
    return texto

preco =  float(input("Digite o preço: "))
print(formatar_real_replace(preco))