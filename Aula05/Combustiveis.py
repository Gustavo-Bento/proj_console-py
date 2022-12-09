def etanol(opcao):
    print("\nCódigo selecionado: ",opcao)
    print("Produto selecionado: Etanol")
    pagamento = int(input("\nDigite (1) para o total em reais\nDigite (2) para total em litros:\n"))
    if(pagamento==1):
        valor=int(input("\nDigite o total em reais: "))
        total =float(valor/3.5)
        return print("O valor total em litros de R$",valor," é de ",total," litros.")
    else:
        litros=int(input("\nDigite o total em litros: "))
        total = float(litros*3.5)
        return print("O valor total em reais de ",litros,"litros é de R$",total,".")

def gasolina(opcao):
    print("\nCódigo selecionado: ",opcao)
    print("Produto selecionado: Gasolina")
    pagamento = int(input("\nDigite (1) para o total em reais\nDigite (2) para total em litros:\n"))
    if(pagamento==1):
        valor=int(input("\nDigite o total em reais: "))
        total =float(valor/4.65)
        return print("O valor total em litros de R$",valor," é de ",total," litros.")
    else:
        litros=int(input("\nDigite o total em litros: "))
        total = float(litros*4.65)
        return print("O valor total em reais de ",litros,"litros é de R$",total,".")

def aditivada(opcao):
    print("\nCódigo selecionado: ",opcao)
    print("Produto selecionado: Gasolina Aditivada")
    pagamento = int(input("\nDigite (1) para o total em reais\nDigite (2) para total em litros:\n"))
    if(pagamento==1):
        valor=int(input("\nDigite o total em reais: "))
        total =float(valor/4.99)
        return print("O valor total em litros de R$",valor," é de ",total," litros.")
    else:
        litros=int(input("\nDigite o total em litros: "))
        total = float(litros*4.99)
        return print("O valor total em reais de ",litros,"litros é de R$",total,".")

def s500(opcao):
    print("\nCódigo selecionado: ",opcao)
    print("Produto selecionado: Diesel S-500")
    pagamento = int(input("\nDigite (1) para o total em reais\nDigite (2) para total em litros:\n"))
    if(pagamento==1):
        valor=int(input("\nDigite o total em reais: "))
        total =float(valor/6.59)
        return print("O valor total em litros de R$",valor," é de ",total," litros.")
    else:
        litros=int(input("\nDigite o total em litros: "))
        total = float(litros*6.59)
        return print("O valor total em reais de ",litros,"litros é de R$",total,".")

def s10(opcao):
    print("\nCódigo selecionado: ",opcao)
    print("Produto selecionado: Diesel S-10")
    pagamento = int(input("\nDigite (1) para o total em reais\nDigite (2) para total em litros:\n"))
    if(pagamento==1):
        valor=float(input("\nDigite o total em reais: "))
        total =float(valor/6.29)
        return print(f'O valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
    else:
        litros=float(input("\nDigite o total em litros: "))
        total = float(litros*6.29)
        return print(f'O valor total em reais de {litros: .2f}litros é de R${total: .2f}')
