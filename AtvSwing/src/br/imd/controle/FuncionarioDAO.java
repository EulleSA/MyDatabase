package br.imd.controle;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.imd.modelo.Funcionario;

public class FuncionarioDAO {
	private Connection conn;
	
/* Criar a conexão */
	public FuncionarioDAO() throws SQLException {
		conn  = Conex
	}	
	
	
	public void inserirFuncionario(Funcionario funcionario) throws SQLException {
		String sql = "Insert into funcionario(nome,cpf,sexo,anoNascimento,endereco,telefone) values(?,?,?,?,?,?)";
		PreparedStatement pst = conn.prepareStatement(sql);
		
		/* Adicionar mais coisas aqui */ 
		
		pst.execute();
		conn.commit();
		pst.close();
		System.out.println("Funcionario " + funcionario.getNome() + " cadastrado.");
	}
}


	public void 
