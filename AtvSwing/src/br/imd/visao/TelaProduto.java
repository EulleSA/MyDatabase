package br.imd.visao;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import br.imd.controle.Fachada;
import br.imd.modelo.Funcionario;
import br.imd.modelo.Produto;

import javax.swing.JToolBar;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TelaProduto extends JFrame {

	private JPanel contentPane;
	private JTextField txtNome;
	private JTextField txtTipo;
	private JTextField txtPreco;
	private JTextField txtQuantidade;
	private JTextField txtDatavalidade;
	private JTextField txtDatafabricacao;
	Fachada fachada;


	/**
	 * Create the frame.
	 */
	public TelaProduto(Fachada fachada) {
		this.fachada = fachada;
		setTitle("Cadastro Produto");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.setBounds(0, 0, 450, 21);
		contentPane.add(menuBar);
		
		JMenu mnCadastrar = new JMenu("Opções");
		menuBar.add(mnCadastrar);
		
		JMenu mnCadastrar_1 = new JMenu("Cadastrar");
		mnCadastrar.add(mnCadastrar_1);
		
		JLabel lblNome = new JLabel("Nome :");
		lblNome.setBounds(10, 43, 70, 15);
		contentPane.add(lblNome);
		
		txtNome = new JTextField();
		txtNome.setBounds(71, 41, 181, 19);
		contentPane.add(txtNome);
		txtNome.setColumns(10);
		
		JLabel lblDescrio = new JLabel("Tipo :");
		lblDescrio.setBounds(20, 70, 80, 15);
		contentPane.add(lblDescrio);
		
		txtTipo = new JTextField();
		txtTipo.setBounds(71, 70, 238, 19);
		contentPane.add(txtTipo);
		txtTipo.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("Preço :");
		lblNewLabel.setBounds(10, 97, 70, 15);
		contentPane.add(lblNewLabel);
		
		txtPreco = new JTextField();
		txtPreco.setBounds(71, 97, 140, 19);
		contentPane.add(txtPreco);
		txtPreco.setColumns(10);
		
		JLabel lblQuantidade = new JLabel("Quantidade :");
		lblQuantidade.setBounds(12, 183, 98, 15);
		contentPane.add(lblQuantidade);
		
		txtQuantidade = new JTextField();
		txtQuantidade.setBounds(114, 181, 114, 19);
		contentPane.add(txtQuantidade);
		txtQuantidade.setColumns(10);
		
		JLabel lblDataDeValidade = new JLabel("Data de Validade :");
		lblDataDeValidade.setBounds(10, 124, 158, 15);
		contentPane.add(lblDataDeValidade);
		
		txtDatavalidade = new JTextField();
		txtDatavalidade.setBounds(151, 122, 114, 19);
		contentPane.add(txtDatavalidade);
		txtDatavalidade.setColumns(10);
		
		JLabel lblDataDeFabricao = new JLabel("Data de Fabricação :");
		lblDataDeFabricao.setBounds(10, 151, 158, 15);
		contentPane.add(lblDataDeFabricao);
		
		txtDatafabricacao = new JTextField();
		txtDatafabricacao.setBounds(161, 151, 114, 19);
		contentPane.add(txtDatafabricacao);
		txtDatafabricacao.setColumns(10);
		
		JButton btnCadastrar = new JButton("Cadastrar");
		btnCadastrar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nome = txtNome.getText();
				String tipo = txtTipo.getText();
				String preco = txtPreco.getText();
				String quantidade = txtQuantidade.getText();
				String dataValidade = txtDatavalidade.getText();
				String dataFabricacao = txtDatafabricacao.getText();
				
				
				Produto newProduto = new Produto(nome,tipo,preco,quantidade,dataValidade,dataFabricacao);
				fachada.cadastrarProduto(newProduto);
			}
		});
		btnCadastrar.setBounds(161, 235, 117, 25);
		contentPane.add(btnCadastrar);
	}
}
