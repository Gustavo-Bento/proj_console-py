import os

def clear():
    os.system('clear')

def tabela():
    print("{:<4}{:<14}{:<9}{:<5}".format("cod","Produto","Valor","Qtd"))
    print("===============================")
    for v in mercadinho:
        print("{:<4}{:<14}R${:.2f} {:>4}".format(v.cod,v.produto,v.valor,v.quantidade))
    print("\n")

class produtos:
    def __init__(self, cod,produto,valor,quantidade):
        self.cod=cod
        self.produto=produto
        self.valor=valor
        self.quantidade=quantidade


clear()
x=1
mercadinho=[]
codigo=0
while (x==1):
    produto=str(input("\nDigite um produto: "))
    valor=float(input("Digite o valor: "))
    quantidade=int(input("Digite a quantidade: "))
    mercadinho.append(produtos(codigo,produto,valor,quantidade))
    codigo +=1
    clear()
    tabela()
    x=int(input("\nDeseja cadastrar outro produto?\n 1 - Sim\n 0 - Não\n\nSua opção foi: "))
    clear()
tabela()

