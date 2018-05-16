class Fornecedor:
    def __init__(self,nome,cnpj):
        self.nome = nome
        self.cnpj = cnpj


    def __str__(self):
        return self.nome


class Funcionario:
    def __init__(self,nome,cpf,sexo,anoNascimento):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo 
        self.anoNascimento = anoNascimento

    def __str__(self):
        return self.nome


class Produto:
    def __init__(self,nome,tipo,preco,quantidade,dataValidade,dataFabricacao):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.quantidade = quantidade
        self.dataValidade = dataValidade
        self.dataFabricacao = dataFabricacao


    def __str__(self):
        return self.nome

