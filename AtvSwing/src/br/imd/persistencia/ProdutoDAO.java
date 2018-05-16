package br.imd.persistencia;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.imd.modelo.Produto;

public class ProdutoDAO {
	
	private Connection conn;
	
	/* Criar a conex�o */
		public ProdutoDAO() throws SQLException {
			
		}	
	
		public void inserirProduto(Produto produto)throws SQLException{
			String sql = "insert into produto " + "(nome,preco,quantidade,dataValidade,dataFabricacao)" + " values(?,?,?,?,?,?)";
			
			try{
				PreparedStatement pst = conn.prepareStatement(sql);
				
				
				pst.execute();
				conn.commit();
				pst.close();
				System.out.println("Funcionario " + produto.getNome() + " cadastrado.");
				
				}
				catch(SQLException e){
					throw new RuntimeException(e);
				}
		}
		
		public void atualizarProduto(Produto produto) throws SQLException{
			
		}
		
		public void deletarProduto(Produto produto) throws SQLException{
			
		}
}
