package br.imd.modelo;

public class Produto {
	private String nome;
<<<<<<< HEAD
	private String preco;
	private String quantidade;
	private String dataValidade;
	private String dataFabricacao;
	
	public Produto(String nome,String preco,String quantidade,String dataValidade,String dataFabricacao) {
		this.nome = nome;
		this.preco = preco;
		this.quantidade = quantidade;
		this.dataValidade = dataValidade;
		this.dataFabricacao = dataFabricacao;
=======
	private int preco;
	private int quantidade;
	private String dataValidade;
	private String dataFabricacao;
	
	Produto(){
		
>>>>>>> cde7d7585d882405f7cc69ecfa8953645f1a4207
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

<<<<<<< HEAD
	public String getPreco() {
		return preco;
	}

	public void setPreco(String preco) {
		this.preco = preco;
	}

	public String getQuantidade() {
		return quantidade;
	}

	public void setQuantidade(String quantidade) {
=======
	public int getPreco() {
		return preco;
	}

	public void setPreco(int preco) {
		this.preco = preco;
	}

	public int getQuantidade() {
		return quantidade;
	}

	public void setQuantidade(int quantidade) {
>>>>>>> cde7d7585d882405f7cc69ecfa8953645f1a4207
		this.quantidade = quantidade;
	}

	public String getDataValidade() {
		return dataValidade;
	}

	public void setDataValidade(String dataValidade) {
		this.dataValidade = dataValidade;
	}

	public String getDataFabricacao() {
		return dataFabricacao;
	}

	public void setDataFabricacao(String dataFabricacao) {
		this.dataFabricacao = dataFabricacao;
	}
	
	
}
