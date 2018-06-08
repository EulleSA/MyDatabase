import Model.Models
from pony.orm import *

class Funcionario_ORM:

    @db_session
    def add_funcionario(nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=nome, cpf=cpf, sexo=sexo, anoNascimento=anoNascimento)
    

    @db_session
    def get_fuc_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.cpf))

    @db_session
    def delete_one_func(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        tree.delete(curItem)
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].delete()

    @db_session
    def edit_func(tree,get_name,nome):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        funcionario = row
        

class Fornecedor_ORM:
    @db_session
    def add_fornecedor(nome,cnpj):
        Model.Models.Fornecedor(nome=nome,cnpj=cnpj)


    @db_session
    def get_forn_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.cnpj))


    @db_session
    def delete_one_forn(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        tree.delete(curItem)
        row = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor WHERE id=%s' % selecteditem)
        row[0].delete()

class Produto_ORM:
    @db_session
    def add_produto(nome,preco,quantidade):
        Model.Models.Produto(nome=nome,preco=preco,quantidade=quantidade)
    

    @db_session
    def get_prod_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Produto.select_by_sql('SELECT * FROM Produto')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.preco))
    
    @db_session
    def delete_one_prod(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        tree.delete(curItem)
        row = Model.Models.Produto.select_by_sql('SELECT * FROM Produto WHERE id=%s' % selecteditem)
        row[0].delete()