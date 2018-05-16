import java.awt.EventQueue;

import br.imd.controle.Fachada;
import br.imd.persistencia.FactoryDAO;
import br.imd.visao.TelaFuncionario;
import br.imd.visao.TelaProduto;

public class LancadorSistema {
	
		public static void main(String[] args) {
			FactoryDAO fabrica = new FactoryDAO();
			Fachada fachada = new Fachada(fabrica);
			EventQueue.invokeLater(new Runnable() {
				public void run() {
					try {
						TelaProduto frame1 = new TelaProduto(fachada);
						frame1.setVisible(true);
						
						TelaFuncionario frame2 = new TelaFuncionario(fachada);
						frame2.setVisible(true);
					} catch (Exception e) {
						e.printStackTrace();
					}
				}
			});
		}

}
