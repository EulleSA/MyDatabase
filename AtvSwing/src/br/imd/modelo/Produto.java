package br.imd.modelo;

public class Produto {
	private String nome;
	private String tipo;
	

	private String preco;
	private String quantidade;
	private String dataValidade;
	private String dataFabricacao;
	
	public Produto(String nome,String tipo,String preco,String quantidade,String dataValidade,String dataFabricacao) {
		this.nome = nome;
		this.tipo = tipo;
		this.preco = preco;
		this.quantidade = quantidade;
		this.dataValidade = dataValidade;
		this.dataFabricacao = dataFabricacao;
	
}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
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