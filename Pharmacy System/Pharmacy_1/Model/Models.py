class Funcionario:
    def __init__(self,nome,cpf,sexo,anoNascimento):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.anoNascimento = anoNascimento

    def __str__(self):
        return self.nome

class Fornecedor:
    def __init__(self,nome,cnpj,funcionario):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionario = funcionario
    
    def __str__(self):
        return self.nome

class Produto:
    def __init__(self,nome,preco,quantidade,fornecedor,funcionario):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        self.funcionario = funcionario
        #self.dataFabricacao = dataFabricacao
        #self.dataValidade = dataValidade

    def __str__(self):
        return self.nome
