package br.imd.persistencia;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.imd.modelo.Funcionario;

public class FuncionarioDAO {
	private Connection conn;
	
/* Criar a conex�o */
	public FuncionarioDAO(Connection conn) throws SQLException {
		this.conn = conn;
	}	
	
	
	public void inserirFuncionario(Funcionario funcionario) throws SQLException {
		String sql = "insert into funcionario " + "(nome,cpf,sexo,anoNascimento,endereco,telefone)" + " values(?,?,?,?,?,?)";
		try{
		PreparedStatement pst = conn.prepareStatement(sql);
		
		pst.setString(1,funcionario.getNome());
		pst.setString(2,funcionario.getCpf());
		pst.setString(3,funcionario.getSexo());
		pst.setString(4, funcionario.getAnoNascimento());
		pst.setString(5, funcionario.getEndereco());
		pst.setString(6, funcionario.getTelefone());
		
		pst.execute();
		conn.commit();
		
		pst.close();
		System.out.println("Funcionario " + funcionario.getNome() + " cadastrado.");
		
		}
		catch(SQLException e){
			throw new RuntimeException(e);
		}
	}


	public void deletarFuncionario(Funcionario funcionario) throws SQLException{
		
	}
	

	public void listarFuncionarios(){
		
	}

}	


	
