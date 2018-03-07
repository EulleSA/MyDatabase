package br.imd.visao;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JRadioButton;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Font;
import javax.swing.JToolBar;
import javax.swing.JList;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ContainerAdapter;
import java.awt.event.ContainerEvent;

public class TelaPrincipal extends JFrame {

	private JPanel contentPane;
	private JTextField txtnome;
	private JTextField txtcpf;
	private JTextField txtdataNascimento;
	private JTextField txttelefone;
	private JTextField txtendereco;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TelaPrincipal frame = new TelaPrincipal();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public TelaPrincipal() {
		setAutoRequestFocus(false);
		setTitle("Cadastro Pessoa");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 455, 312);
		contentPane = new JPanel();
		contentPane.setToolTipText("");
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Nome :");
		lblNewLabel.setFont(new Font("Open Sans", Font.PLAIN, 12));
		lblNewLabel.setBounds(10, 39, 46, 14);
		contentPane.add(lblNewLabel);
		
		txtnome = new JTextField();
		txtnome.setBounds(58, 37, 270, 20);
		contentPane.add(txtnome);
		txtnome.setColumns(10);
		
		JLabel lblCpf = new JLabel("CPF :");
		lblCpf.setFont(new Font("Open Sans", Font.PLAIN, 12));
		lblCpf.setBounds(10, 64, 46, 14);
		contentPane.add(lblCpf);
		
		txtcpf = new JTextField();
		txtcpf.setBounds(58, 64, 142, 20);
		contentPane.add(txtcpf);
		txtcpf.setColumns(10);
		
		JLabel lblDataNascimento = new JLabel("Data Nascimento :");
		lblDataNascimento.setFont(new Font("Open Sans", Font.PLAIN, 12));
		lblDataNascimento.setBounds(10, 89, 108, 14);
		contentPane.add(lblDataNascimento);
		
		txtdataNascimento = new JTextField();
		txtdataNascimento.setBounds(121, 87, 101, 20);
		contentPane.add(txtdataNascimento);
		txtdataNascimento.setColumns(10);
		
		JLabel lblTelefone = new JLabel("Telefone :");
		lblTelefone.setFont(new Font("Open Sans", Font.PLAIN, 12));
		lblTelefone.setBounds(10, 144, 69, 14);
		contentPane.add(lblTelefone);
		
		txttelefone = new JTextField();
		txttelefone.setBounds(72, 142, 128, 20);
		contentPane.add(txttelefone);
		txttelefone.setColumns(10);
		
		JLabel sexo = new JLabel("Sexo :");
		sexo.setFont(new Font("Open Sans", Font.PLAIN, 12));
		sexo.setBounds(10, 169, 46, 14);
		contentPane.add(sexo);
		
		JRadioButton rdbtnNewRadioButton = new JRadioButton("M");
		rdbtnNewRadioButton.setBounds(20, 190, 46, 23);
		contentPane.add(rdbtnNewRadioButton);
		
		JRadioButton rdbtnNewRadioButton_1 = new JRadioButton("F");
		rdbtnNewRadioButton_1.setBounds(72, 190, 46, 23);
		contentPane.add(rdbtnNewRadioButton_1);
		
		JRadioButton rdbtnOutro = new JRadioButton("Outro");
		rdbtnOutro.setBounds(120, 190, 53, 23);
		contentPane.add(rdbtnOutro);
		
		JButton btnCadastrar = new JButton("Cadastrar");
		btnCadastrar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
			}
		});
		btnCadastrar.setBounds(161, 233, 117, 23);
		contentPane.add(btnCadastrar);
		
		JLabel lblEndereo = new JLabel("Endere\u00E7o :");
		lblEndereo.setFont(new Font("Open Sans", Font.PLAIN, 12));
		lblEndereo.setBounds(10, 114, 69, 14);
		contentPane.add(lblEndereo);
		
		txtendereco = new JTextField();
		txtendereco.setBounds(74, 112, 239, 20);
		contentPane.add(txtendereco);
		txtendereco.setColumns(10);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.setBounds(0, 0, 439, 21);
		contentPane.add(menuBar);
		
		JMenu menuItem1 = new JMenu("Cadastrar");
		menuBar.add(menuItem1);
		
		JMenuItem mntmCliente = new JMenuItem("Cliente");
		menuItem1.add(mntmCliente);
		
		JMenuItem mntmFuncionario = new JMenuItem("Funcionario");
		mntmFuncionario.addContainerListener(new ContainerAdapter() {
			@Override
			public void componentAdded(ContainerEvent arg0) {
			
				setAutoRequestFocus(false);
				setTitle("Cadastro Funcionario");
				setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				setBounds(100, 100, 455, 312);
				contentPane = new JPanel();
				contentPane.setToolTipText("");
				contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
				setContentPane(contentPane);
				contentPane.setLayout(null);
			}
			
		});
		menuItem1.add(mntmFuncionario);
		
		JMenuItem mntmFornecedor = new JMenuItem("Fornecedor");
		menuItem1.add(mntmFornecedor);
	}
}
