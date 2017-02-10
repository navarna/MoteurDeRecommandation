//AUTEUR  : Navarna 
import java.io.File;


public class mainEcriture {

	/**
	 * @param args
	 */
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Ecriture e = new Ecriture () ;
		File rep = new File("DonneeSuite");
	File[] fichiers = rep.listFiles();
		System.out.println("nbFichier : " + fichiers.length); 
		for (int i = 0 ; i < fichiers.length ; i++){
			e.tabletitle("DonneeSuite/"+fichiers[i].getName());
			e.justeGenre("DonneeSuite/"+fichiers[i].getName());
			e.tableDesc("DonneeSuite/"+fichiers[i].getName());
		}
		e.fermeture (); 
		e.finish();
		
	}

}
