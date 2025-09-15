# Sprint 3 - Computational Thinking with Python
# Sistema de cadastro de atletas no Bola pra Frente
# -----------------------------------------------

# Função para cadastrar uma atleta
def cadastrar_atleta():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    posicao = input("Posição: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    atleta = {
        "nome": nome,
        "idade": idade,
        "posição": posicao,
        "peso": peso,
        "altura": altura,
        "cidade": cidade,
        "estado": estado
    }
    return atleta


# Função para exibir todas as atletas cadastradas
def listar_atletas(lista):
    if len(lista) == 0:
        print("\nNenhuma atleta cadastrada ainda.\n")
    else:
        print("\n===== LISTA DE ATLETAS CADASTRADAS =====")
        for i, atleta in enumerate(lista, start=1):
            print(f"\nAtleta {i}:")
            for chave, valor in atleta.items():
                print(f"  {chave.capitalize()}: {valor}")


# Função para buscar atleta pelo nome
def buscar_atleta(lista, nome):
    for atleta in lista:
        if atleta["nome"].lower() == nome.lower():
            return atleta
    return None


# Programa principal
def main():
    atletas = []  # Lista para armazenar os cadastros
    while True:
        print("\n===== MENU BOLA PRA FRENTE =====")
        print("1 - Cadastrar atleta")
        print("2 - Listar atletas")
        print("3 - Buscar atleta por nome")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            atleta = cadastrar_atleta()
            atletas.append(atleta)
            print(f"\n Atleta {atleta['nome']} cadastrada com sucesso!!")
        elif escolha == "2":
            listar_atletas(atletas)
        elif escolha == "3":
            nome = input("Digite o nome da atleta: ")
            resultado = buscar_atleta(atletas, nome)
            if resultado:
                print("\nAtleta encontrada:")
                for chave, valor in resultado.items():
                    print(f"  {chave.capitalize()}: {valor}")
            else:
                print("\n Atleta não encontrada.")
        elif escolha == "4":
            print("\nSaindo... Até logo!!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")



# Executar o programa
if __name__ == "__main__":
    main()
