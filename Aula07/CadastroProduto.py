from Produtos import *
import os

def clear():
    os.system('clear')

pratileira=[]

def cadastrar():
    x=0
    y=0
    while(x==0):
        produto = str(input("Digite o nome do produto: "))
        qtd = int(input("Digite a quantidade: "))
        valor= float(input("Digite o valor unitario: "))
        pratileira.append(Produtos(y,produto,valor,qtd,Produtos.estoque('',qtd)))
        y += 1
        tabela()
        x=int(input('Deseja cadastrar novo produto?\n 0 - (Sim)\n 1 - (Não)\nSua decisão foi: '))

def tabela():
    Produtos.cabecalho()
    for v in pratileira:
        print("{:<4}{:<14}{:<9}{:<5}{:<5}".format(v.cod,v.produto,v.valor,v.quantidade,v.disponivel))