class Pessoa:
    # Metodo construtor
    def __init__(self, nome, sexo, cpf, ativo):
        self._nome = nome
        self._sexo = sexo
        self._cpf = cpf
        self._ativo = ativo

    # Metodo desativar
    def desativar(self):
        self._ativo = False
        print("A pessoa foi desativada com sucesso!")

    # Metodo ativar
    def ativar(self):
        self._ativo = True
        print("A pessoa foi ativada com sucesso!")

    # Metodo que retorna o nome
    def get_nome(self):
        return self._nome

    # Metodo que altera o nome
    def set_nome(self, nome):
        self._nome = nome

    #Meotod que retorna o sexo
    def get_sexo(self):
        return self._sexo
    
    #MEtodo que altera o sexo
    def set_sexo(self,sexo):
        self._sexo = sexo
    
    #MEtodo que retonra o cpf
    def get_cpf(self):
        return self._cpf

    #Metodo que altera o cpf
    def set_cpf(self, cpf):
        self._cpf = cpf