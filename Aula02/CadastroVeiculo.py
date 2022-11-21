import os


class veiculo:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


cadastro = []
x = 0


def tela():
    def clear(): return os.system('clear')
    clear()
    print("-------------------------------")
    print("------CADASTRO DE VEICULO------")
    print("-------------------------------\n")

    cadastro.sort(key=lambda x: x.marca)

    print("{:<10} {:<19} {:<6} {:<8}".format(
        "Marca", "Modelo", "Ano", "Placa"))

    y = 0
    while (y <= x):
        for v in cadastro:
            print("{:<10} {:<10} {:<6} {:<8}".format(
                v.marca, v.modelo, v.ano, v.placa))
            y += 1
