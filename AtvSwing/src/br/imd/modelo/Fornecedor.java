 	package br.imd.modelo;

public class Fornecedor {
	
	private String nomeForncedor;
	private String cnpj;
	
	public Fornecedor(String nomeFornecedor,String cnpj) {
		this.nomeForncedor = nomeForncedor;
		this.cnpj = cnpj;
	}

	public String getNomeForncedor() {
		return nomeForncedor;
	}

	public void setNomeForncedor(String nomeForncedor) {
		this.nomeForncedor = nomeForncedor;
	}

	public String getCnpj() {
		return cnpj;
	}

	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	
	
}
