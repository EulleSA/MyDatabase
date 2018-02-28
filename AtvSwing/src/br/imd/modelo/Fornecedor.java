package br.imd.modelo;

public class Fornecedor extends Pessoa {
	
	private double valorCredito;
	private double valorDivida;
	
	Fornecedor(String nome,String endereco ,String telefone,String sexo,int anoNascimento,double valorCredito, double valorDivida){
		super(nome,endereco,telefone,sexo,anoNascimento);
		this.valorCredito = valorCredito;
		this.valorDivida = valorDivida;
		
	}
	
	public double obterSaldo() {
		return this.valorCredito - this.valorDivida;
	}

	public double getValorCredito() {
		return valorCredito;
	}

	public void setValorCredito(double valorCredito) {
		this.valorCredito = valorCredito;
	}

	public double getValorDivida() {
		return valorDivida;
	}

	public void setValorDivida(double valorDivida) {
		this.valorDivida = valorDivida;
	}
	
	
}
