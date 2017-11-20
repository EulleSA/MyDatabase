
--Busca o numero de funcionario pelos diferentes sexos
select sexo, count(sexo) 
from funcionario 
group by sexo

--Busca o numero de funcionario pelos diferentes cargos
select cargo, count(cargo)
from funcionario
group by cargo 

--Busca o numero de clientes pelos diferentes sexos
select sexo, count(sexo)
from cliente
group by sexo

--Agrupa os clientes pela idade
select date_trunc('year',age(current_date,dataNascimento)), count(date_trunc('year',age(current_date,dataNascimento)))
from cliente
group by date_trunc('year',age(current_date,dataNascimento))

--Nome dos medico que venderam algum remedio
select nomemedico from pedido inner join receita 
on pedido.idReceita = receita.idReceita
inner join medico on receita.crm = medico.crm
where pedido.quantidade > 0

--Relatorio de venda

--Quanto foi vendido pelas diferetes formas de pagamento

select * from forma_pagamento_vw 

--Venda realizada por cada funcionario

select * from venda_por_func_vw

--Funcionarios que não realizaram venda

select * from func_sem_venda_vw

--Produtos vendidos
select nomeproduto, sum(quantidade)
from venda inner join pedido
on venda.idpedido = pedido.idpedido
inner join produto
on pedido.idproduto = produto.idproduto
group by nomeproduto


--Relatorio devolução

--Nome dos produtos devolvidos, seu motivo e valor.
select nomeproduto, motivo, valortotal from produto inner join devolucao
on produto.idproduto = devolucao.iddevolucao
inner join venda
on devolucao.idvenda = venda.idvenda

--Soma do valor total de produtos devolvidos
select sum(valortotal) from produto inner join devolucao
on produto.idproduto = devolucao.iddevolucao
inner join venda
on devolucao.idvenda = venda.idvenda
