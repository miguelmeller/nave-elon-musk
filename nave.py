##Definir as varíaveis
combustivel = 100
tripulantes = []

## Definir funções:

def viajar():
    ##aqui coloca o código
    global combustivel ##Avisa a função que vamos modificar um variavel externa
    if(combustivel >=30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustível o suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! ⛽")

def status_nave():
    ##Moste a quantidade de combustível e os tripulantes
    print("\n------ STATUS DA NAVE -----")
    print(f"Temos {combustivel} de combustível")
    print(f"Os tripulantes da nave são: {tripulantes} ")
    print("------------------------------------\n")

def registrarTripulante():
    ##Essa funções pergunta o mome do tripulante e adicona na lista de tripulantes
    novoTripulante = input("Qual o nome do novo tripulante?: ") ##Pergunta quem
    tripulantes.append(novoTripulante) ##Inserimos o fulano
    print("Tripulante inserido com sucesso! 🚀")


##Criar um menu

while True: ##Esse loop roda para sempre!
    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção: ")
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()
    else:
        print("Viagem encerrada!")
        break


# status_nave()
# registrarTripulante()
# registrarTripulante()
# status_nave()


# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()