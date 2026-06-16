fila_espera = []
clientes_atendidos = 0

while True:
    print("\n=== LISTA DE ESPERA DO RESTAURANTE ===")
    print("1 - Adicionar cliente")
    print("2 - Chamar próximo cliente")
    print("3 - Desistência")
    print("4 - Mostrar fila de espera")
    print("5 - Fechar restaurante")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ").strip()

        if nome in fila_espera:
            print("Esse cliente já está na fila.")
        else:
            fila_espera.append(nome)
            print(f"{nome} foi adicionado à fila de espera.")

    elif opcao == "2":
        if len(fila_espera) == 0:
            print("Não há ninguém esperando.")
        else:
            proximo = fila_espera.pop(0)
            clientes_atendidos += 1
            print(f"Cliente chamado: {proximo}")

    elif opcao == "3":
        nome = input("Digite o nome do cliente que desistiu: ").strip()

        if nome in fila_espera:
            fila_espera.remove(nome)
            print(f"{nome} foi removido da fila.")
        else:
            print("Cliente não encontrado na fila.")

    elif opcao == "4":
        if len(fila_espera) == 0:
            print("Não há ninguém na fila de espera.")
        else:
            print("\n--- FILA DE ESPERA ---")

            posicao = 1
            for cliente in fila_espera:
                print(f"{posicao}º - {cliente}")
                posicao += 1

    elif opcao == "5":
        print("\n=== RESTAURANTE FECHADO ===")

        print(f"Clientes restantes na fila: {len(fila_espera)}")

        if len(fila_espera) > 0:
            print("Clientes que ficaram sem atendimento:")

            for cliente in fila_espera:
                print(cliente)
        else:
            print("Nenhum cliente ficou na fila.")

        print(f"Total de clientes atendidos: {clientes_atendidos}")

        break

    else:
        print("Opção inválida. Tente novamente.")