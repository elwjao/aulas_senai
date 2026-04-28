def exibir_info_usuario(info):
    print("Informações do usuário:")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

info_usario = {}

print("Digite a chave (ou 'sair' para encerrar): ")


while True:
    chave = input("Nome do campo (ex: Profissão): ")
    if chave.lower() == 'sair':
        break
    valor = input(f"Salario {chave}: ")
    info_usario[chave] = valor

exibir_info_usuario(info_usario)