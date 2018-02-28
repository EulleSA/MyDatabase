package br.imd.modelo;

public class Pessoa {
	protected String nome;
	protected String endereco;
	protected String telefone;
	protected String sexo;
	protected int anoNascimento ;
	
	
	Pessoa(String nome, String endereco, String telefone, String sexo, int anoNascimento) {
		this.nome = nome;
		this.endereco = endereco;
		this.telefone = telefone;
		this.sexo = sexo;
		this.anoNascimento = anoNascimento;
	}
	
	public int calcularIdade(int ano) {
		int idade;
		idade = ano - this.anoNascimento;
		return idade;
		
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEndereco() {
		return endereco;
	}

	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getSexo() {
		return sexo;
	}

	public void setSexo(String sexo) {
		this.sexo = sexo;
	}

	public int getAnoNascimento() {
		return anoNascimento;
	}

	public void setAnoNascimento(int anoNascimento) {
		this.anoNascimento = anoNascimento;
	}
	
}
