import os
from Combustiveis import *

def clear(): 
    os.system('clear')

def tabela():
    print("---------------------------")
    print("|{:<3}|{:<12}|{:<7}|".format("Cod","Combustivel","Valor"))
    print("===========================")
    for v in posto:
        print("|{:<3}|{:<12}|{:<7}|".format(v.cod,v.combustivel,v.valor))
    print("---------------------------")

class combustivel:
    def __init__(self,cod,combustivel,valor):
        self.cod = cod
        self.combustivel = combustivel
        self.valor = valor

class abastecer:
    def switch(self,combustivel):
        default = "Combustivel não encontrado"
        return getattr(self, 'case_'+str(combustivel), lambda:default)()
    
    def case_1(self):
        etanol(opcao)
    
    def case_2(self):
        gasolina(opcao)
    
    def case_3(self):
        aditivada(opcao)

posto=[]
x=0

posto.append(combustivel(1,"Etanol","R$ 3,50"))
posto.append(combustivel(2,"Gasolina", "R$ 4,65"))
posto.append(combustivel(3,"G. Aditivada","R$ 4,99"))
posto.append(combustivel(4,"Diesel S500", "R$ 6,59"))
posto.append(combustivel(5,"Diesel S10","R$ 6,29"))

s=abastecer()
while(x==0):
    clear()
    tabela()
    opcao = int(input("\nDigite o código do produto: "))
    print("\nSegue o resultado: ",s.switch(opcao))
    x=int(input("Deseja realizar novo abastecimento? Sim (0) ou Não (1): "))