package br.imd.modelo;

public class Empregado extends Pessoa {
	
	Setor setor;
	private double salarioBase;
	int imposto;
	
	Empregado(String nome,String endereco ,String telefone,String sexo,int anoNascimento,Setor setor,double salarioBase,int imposto){
		super(nome,endereco,telefone,sexo,anoNascimento);
		this.salarioBase = salarioBase;
		this.imposto = imposto;
		this.setor = setor;
	}
	
	
	public double calcularSalario() {
		return this.salarioBase*this.imposto;
	}
}
