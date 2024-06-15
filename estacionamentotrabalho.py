
# Aplicação de Estacionamento
# Autor:Murilo Ganzala
# Data de Criação: 14/06/2024


# Lista para armazenar os veículos estacionados
carros_estacionados = []

# Lista para armazenar o histórico de entradas e saídas de veículos
historico = []

def estacionar_carro(placa, marca, modelo, cor, proprietario):
   
   # Função para estacionar um veículo no estacionamento.

    
    
    # Adiciona o veículo à lista de carros estacionados
    carros = {
        'placa': placa,
        'marca': marca,
        'modelo': modelo,
        'cor': cor,
        'proprietario': proprietario
    }
    carros_estacionados.append(carros)
    # Registra a entrada do veículo no histórico

    historico.append((placa, 'entrada'))
    print(f"Veículo com placa {placa} estacionado com sucesso.")

def retirar_veiculo(placa):
   
    # Função para retirar um veículo do estacionamento.

    
    
    veiculo_encontrado = next((veiculo for veiculo in carros_estacionados if veiculo['placa'] == placa), None)
    if veiculo_encontrado:
        carros_estacionados.remove(veiculo_encontrado)
        historico.append((placa, 'saida'))
        print(f"Veículo com placa {placa} retirado com sucesso.")
    else:
        print(f"Veículo com placa {placa} não encontrado no estacionamento.")

def listar_veiculos_estacionados():
    
    # Função para listar todos os veículos atualmente estacionados.

    if carros_estacionados:
        print("Veículos estacionados:")
        for veiculo in carros_estacionados:
            print(f"Placa: {veiculo['placa']}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Cor: {veiculo['cor']}, Proprietário: {veiculo['proprietario']}")
    else:
        print("Nenhum veículo estacionado no momento.")

def verificar_estacionamento(placa):
   
   # Função para verificar se um veículo está estacionado.

   
    if any(registro[0] == placa for registro in historico if registro[1] == 'entrada'):
        print(f"Veículo com placa {placa} está estacionado.")
    else:
        print(f"Veículo com placa {placa} não está estacionado.")

def listar_historico():
  
   # Função para listar o histórico de entradas e saídas de veículos.
    
    if historico:
        print("Histórico de entradas e saídas:")
        print("\n".join([f"Placa: {registro[0]}, Ação: {registro[1]}" for registro in historico]))
    else:
        print("Nenhum registro no histórico.")

def menu():
    
   # Função que exibe o menu e chama as funções correspondentes conforme a escolha do usuário.

    while True:
        print("\nMenu do Estacionamento:")
        print("1 - Estacionar veículo")
        print("2 - Retirar veículo")
        print("3 - Veículos estacionados")
        print("4 - Está estacionado?")
        print("5 - Histórico de entradas e saídas")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            placa = input("Digite a placa do veículo: ")
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            cor = input("Digite a cor do veículo: ")
            proprietario = input("Digite o nome do proprietário: ")
            estacionar_carro(placa, marca, modelo, cor, proprietario)
        elif opcao == '2':
            placa = input("Digite a placa do veículo a ser retirado: ")
            retirar_veiculo(placa)
        elif opcao == '3':
            listar_veiculos_estacionados()
        elif opcao == '4':
            placa = input("Digite a placa do veículo para verificar: ")
            verificar_estacionamento(placa)
        elif opcao == '5':
            listar_historico()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def inicializar():
    
  #  Função para inicializar o sistema com um carro padrão estacionado.
    
    placa = 'ABC1234'
    marca = 'Fiat'
    modelo = 'Uno'
    cor = 'Preto'
    proprietario = 'Seu Nome'
    estacionar_carro(placa, marca, modelo, cor, proprietario)

# Inicializa o sistema com um carro padrão
inicializar()

# Chama a função do menu principal
menu()
