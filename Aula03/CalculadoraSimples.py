import os

def clear(): os.system('clear')

class operador:
    def __init__(self,opcao,operador,info):
        self.opcao = opcao
        self.operador = operador
        self.info = info

calculadora= []

x = 0

calculadora.append(operador(1,"+","Adição"))
calculadora.append(operador(2,"-","Subtração"))
calculadora.append(operador(3,"x","Multiplicação"))
calculadora.append(operador(4,"÷","Divisão"))

def calc():
    print("-------------------------")
    print("|{:<3}|{:<3}|{:<15}|".format("Nº","Op","Informação"))
    print("|===+===+===============|")
    for v in calculadora:
        print("|{:<3}|{:<3}|{:<15}|".format(v.opcao,v.operador,v.info))
    print("-------------------------")

while(x==0):
    clear()
    calc()
    res = int(input("\nSelecione o numero da operação que realizar: "))

    class calculo:  
        
        def switch(self, operacao):
            default = "Valor não encontrado"
            return getattr(self, 'case_'+str(operacao), lambda:default)()
        def case_1(self):
            v1 = int(input("\nDigite o valor 1: "))
            v2 = int(input("Digite o valor 2: "))
            return v1+v2
        def case_2(self):
            v1 = int(input("\nDigite o valor 1: "))
            v2 = int(input("Digite o valor 2: "))
            return v1-v2
        def case_3(self):
            v1 = int(input("\nDigite o valor 1: "))
            v2 = int(input("Digite o valor 2: "))
            return v1*v2
        def case_4(self):
            v1 = int(input("\nDigite o valor 1: "))
            v2 = int(input("Digite o valor 2: "))
            return v1/v2
    
    s = calculo()
    print("\nO valor resultante é: ",s.switch(res))
    x=int(input("\nDeseja realizar outra operação? Sim (0) ou Não (1): "))
clear()
    

    


