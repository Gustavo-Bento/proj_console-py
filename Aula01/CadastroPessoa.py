print("-----------------------------------------")
print("---------CADASTRO DE PESSOAS-------------")
print("-----------------------------------------\n")

res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: "))

class pessoa:
    def __init__(self, nome, idade, cargo, cidade):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.cidade = cidade

cadastro =[]
x=0

while(res == 1):

    cadNome = input("Digite o seu nome: ")
    cadIdade = input("Digite a sua idade: ")
    cadCargo = input("Digite o seu cargo atual: ")
    cadCidade = input("Digite sua cidade: ")

    cadastro.append(pessoa(
        cadNome,
        cadIdade,
        cadCargo,
        cadCidade
    ))

    cadastro.sort(key=lambda x: x.nome)

    print("\n{:<10} {:<6} {:<16} {:<12}".format("Nome","Idade","Cargo","Cidade"))

    y=0
    while(y<=x):
        for v in cadastro:
            print("{:<10} {:<6} {:<16} {:<12}".format(v.nome, v.idade, v.cargo, v.cidade))
            y += 1
    x += 1
    res = int(input("\nDeseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: "))

