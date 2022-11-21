import os


class veiculo:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


cadastro = []
x = 0

def clear(): os.system('clear')

def tela():
    print("\n-------------------------------------")
    print("---------CADASTRO DE VEICULO---------")
    print("-------------------------------------\n")

    cadastro.sort(key=lambda x: x.marca)

    print("{:<12} {:<8} {:<6} {:<8}".format(
        "Marca", "Modelo", "Ano", "Placa"))
    print("-------------------------------------")

    y = 0
    while (y <= x):
        for v in cadastro:
            print("{:<12} {:<8} {:<6} {:<8}".format(
                v.marca, v.modelo, v.ano, v.placa))
            y += 1


res = int(input("\nDeseja cadastrar um novo veículo? Sim(1) / Não(0): "))

while (res == 1):
    cadMarca = input("\nDigite a marca do veículo: ")
    cadModelo = input("Digite o modelo do veículo: ")
    cadAno = input("Digite o ano do veículo: ")
    cadPlaca = input("Digite a placa do veículo: ")

    cadastro.append(veiculo(cadMarca, cadModelo, cadAno, cadPlaca))
    clear()
    tela()
    x += 1
    res = int(input("\nDeseja cadastrar um novo veículo? Sim(1) / Não(0): "))
