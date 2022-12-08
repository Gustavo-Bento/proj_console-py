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