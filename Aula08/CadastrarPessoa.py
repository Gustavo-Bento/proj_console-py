from Pessoa import *
import os

def clear():
    os.system('clear')

pessoa1 = Pessoa("Gustavo","M","123456",True)
pessoa2 = Pessoa("Makenson","M","654321",True)

clear()
pessoa2.set_nome("Ana")
pessoa2.set_sexo("F")
pessoa2.set_cpf("567890")
pessoa2.desativar()

print(pessoa2.get_nome(),pessoa2.get_sexo(),pessoa2.get_cpf(),pessoa2._ativo)
print(pessoa1.get_nome(),pessoa1.get_sexo(),pessoa1.get_cpf(),pessoa1._ativo)