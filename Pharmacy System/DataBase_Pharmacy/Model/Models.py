class Funcionario(db.Entity):
    nome = Required(str)
    cpf = Required(int)
    sexo = Required(str)
    anoNascimento = Required(str)

