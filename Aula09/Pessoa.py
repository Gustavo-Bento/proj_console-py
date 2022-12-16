class Pessoa:
      def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

empresa=[]
x=0
y=0
while(x==0):
    nome=str(input("Digite seu nome: "))
    idade=int(input("Digite sua idade: "))
    empresa.append(Pessoa(nome,idade))
    y += 1
    x = int(input("Deseja novo cadastro: \n(0) - Sim\n(1)-Não\nSua resposta: "))

def tabela():
    for x in range(0,y,1):
        print("{:<3}{:<12}{:<0}".format(x,empresa[x].nome,empresa[x].idade))
tabela()
res = int(input("Deseja alterar algo: \n(0) - Sim\n(1)-Não\nSua resposta: "))
if(res==0):
    res = int(input("Escolha o numero da pessoa: "))
    nome=str(input("Digite seu nome: "))
    idade=int(input("Digite sua idade: "))
    empresa[res] = Pessoa(nome,idade)
tabela()