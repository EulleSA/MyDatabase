import Model.Models
from pony.orm import *

class Funcionario_ORM:
    #CRUD - INSERTION
    @db_session
    def add_funcionario(nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=nome, cpf=cpf, sexo=sexo, anoNascimento=anoNascimento)
    
    #CRUD - READ
    @db_session
    def get_fuc_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.cpf))
    #CRUD - DELETE
    @db_session
    def delete_one_func(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        tree.delete(curItem)
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].delete()
    
    #CRUD - EDIT
    @db_session
    def edit_func_nome(tree,get_name):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].nome = get_name
    @db_session
    def edit_func_cpf(tree,get_cpf):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].cpf = get_cpf
    @db_session
    def edit_func_sexo(tree,get_sexo):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].sexo = get_sexo
    @db_session
    def edit_func_anoNascimento(tree,get_anoNascimento):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        row = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario WHERE id=%s' % selecteditem)
        row[0].anoNascimento = get_anoNascimento



class Fornecedor_ORM:
    #CRUD - INSERTION
    @db_session
    def add_fornecedor(nome,cnpj):
        Model.Models.Fornecedor(nome=nome,cnpj=cnpj)

    #CRUD - READ
    @db_session
    def get_forn_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.cnpj))

    #CRUD - DELETE
    @db_session
    def delete_one_forn(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        tree.delete(curItem)
        row = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor WHERE id=%s' % selecteditem)
        row[0].delete()
    #CRUD - EDIT
    @db_session
    def edit_forn_nome(tree,get_name):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor WHERE id=%s' % selecteditem)
        row[0].nome = get_name

    @db_session
    def edit_forn_cnpj(tree,get_cnpj):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Fornecedor.select_by_sql('SELECT * FROM Fornecedor WHERE id=%s' % selecteditem)
        row[0].cnpj = get_cnpj

class Produto_ORM:
    
    #CRUD - INSERTION
    @db_session
    def add_produto(nome,preco,quantidade):
        Model.Models.Produto(nome=nome,preco=preco,quantidade=quantidade)
    
    #CRUD - READ
    @db_session
    def get_prod_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        db_rows = Model.Models.Produto.select_by_sql('SELECT * FROM Produto')
        for row in db_rows:
            tree.insert('','end',text=row.id,values=(row.nome,row.preco))
    #CRUD - DELETE
    @db_session
    def delete_one_prod(tree):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Produto.select_by_sql('SELECT * FROM Produto WHERE id=%s' % selecteditem)
        row[0].delete()


    #CRUD - EDIT
    @db_session
    def edit_prod_nome(tree,get_name):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Produto.select_by_sql('SELECT * FROM Produto WHERE id=%s' % selecteditem)
        row[0].nome = get_name
    
    @db_session
    def edit_prod_price(tree,get_price):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Produto.select_by_sql('SELECT * FROM Produto WHERE id=%s' % selecteditem)
        row[0].preco = get_price
    
    @db_session
    def edit_prod_quant(tree,get_quant):
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['text']
        
        row = Model.Models.Produto.select_by_sql('SELECT * FROM Produto WHERE id=%s' % selecteditem)
        row[0].quantidade = get_quant