import os

class produto:
    def __init__(self,cod,produto,valor):
        self.cod = cod
        self.produto = produto
        self.valor = valor

loja=[]
x=0

loja.append(produto(1,"Camiseta","R$ 100,00"))
loja.append(produto(2,"Calça","R$ 150,00"))
loja.append(produto(3,"Sapato","R$ 120,00"))

def clear(): os.system('clear')

def tabela():
    print("----------------------------")
    print("|{:<3}|{:<12}|{:<12}|".format("Cod","Produto","Valor"))
    print("============================")
    for v in loja:
        print("|{:<3}|{:<12}|{:<12}|".format(v.cod,v.produto,v.valor))
    print("----------------------------")

class compra:
    def switch(self,produto):
        default = "Produto não encontrado"
        return getattr(self, 'case_'+str(produto), lambda:default)()
    def case_1(self):
        print("\nO codigo - ",opcao)
        print("\nO produto é a Camiseta")
        total = int(input("\nDigite a quantidade a ser comprada: "))
        total *= 100
        return total
    def case_2(self):
        print("\nO codigo - ",opcao)
        print("\nO produto é a Calça")
        total = int(input("\nDigite a quantidade a ser comprada: "))
        total *= 150
        return total
    def case_3(self):
        print("\nO codigo - ",opcao)
        print("\nO produto é a Sapato")
        total = int(input("\nDigite a quantidade a ser comprada: "))
        total *= 120
        return total

s=compra()
while(x==0):
    clear()
    tabela()
    opcao = int(input("\nDigite o código do produto: "))
    print("\nO total da compra é: R$",s.switch(opcao),",00")
    x=int(input("Deseja realizar outra compra? Sim (0) ou Não (0): "))
