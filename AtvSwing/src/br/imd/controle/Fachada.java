package br.imd.controle;

import br.imd.modelo.Produto;
import br.imd.persistencia.FactoryDAO;
import br.imd.persistencia.ForncedorDAO;
import br.imd.persistencia.FuncionarioDAO;
import br.imd.persistencia.ProdutoDAO;

public class Fachada {
	ForncedorDAO fornDao;
	FuncionarioDAO funcDao;
	ProdutoDAO produtoDAO;
	
	public Fachada(FactoryDAO fabrica) {
		super();
		this.fornDao = fabrica.criarForncedorDAO();
		this.funcDao = fabrica.criarFuncionarioDAO();
		this.produtoDAO = fabrica.criarProdutoDAO();
	}
	
	
	public void cadastrarProduto(Produto produto){
		
		produtoDAO.inserirProduto(produto);
	}

	
}
