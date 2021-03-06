//AUTEUR  : Navarna 
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.ArrayList;


import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;


import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class Ecriture {
	
	ArrayList<String> tag = new ArrayList<String>() ;  
	int nbErreur = 0 ; 
	public static void rechercheNull (String nom ){ 
	      try {	
	         File inputFile = new File(nom);
	         DocumentBuilderFactory dbFactory 
	            = DocumentBuilderFactory.newInstance();
	         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	         Document doc = dBuilder.parse(inputFile);
	         doc.getDocumentElement().normalize();
	         NodeList nList = doc.getElementsByTagName("Game");
	         if(nList.getLength()< 3) System.out.println("list null");
	            Node nNode = nList.item(0);
	            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
	               Element eElement = (Element) nNode;
	               String id =  eElement.getElementsByTagName("id").item(0).getTextContent();
	               String GameTitle =  eElement.getElementsByTagName("GameTitle").item(0).getTextContent();
	               String PlatformId =  eElement.getElementsByTagName("PlatformId").item(0).getTextContent();
	               String releaseDate =  eElement.getElementsByTagName("ReleaseDate").item(0).getTextContent();
	               String Overvieuw =  eElement.getElementsByTagName("Overview").item(0).getTextContent();
	               String ESRB =  eElement.getElementsByTagName("ESRB").item(0).getTextContent();
	               String  Players=  eElement.getElementsByTagName("Players").item(0).getTextContent();
	               String Coop =  eElement.getElementsByTagName("Co-op").item(0).getTextContent();
	               String Publisher =  eElement.getElementsByTagName("Publisher").item(0).getTextContent();
	               String Developer =  eElement.getElementsByTagName("Developer").item(0).getTextContent();
	               String Rating =  eElement.getElementsByTagName("Rating").item(0).getTextContent();
	               String genre =  doc.getElementsByTagName("genre").item(0).getTextContent();
	              //	int intid = Integer.parseInt(id); 
	              	System.out.println(id+ ": " );
	              	System.out.println("titre : " +GameTitle);
	              	System.out.println("platforme : " + PlatformId);
	              	System.out.println("date sortie : " + releaseDate);
	              	System.out.println( "description :" + Overvieuw);
	              	System.out.println("ESRB? :" + ESRB);
	              	System.out.println("nb joueur : " + Players);
	              	System.out.println("Coop : " + Coop);
	              	System.out.println("Publieur : " + Publisher);
	              	System.out.println("Developeur : "+ Developer);
	              	System.out.println("Note : " + Rating);
	              	System.out.println("Genre : " + genre);
	            	}
	      	} 
	      	catch (Exception e) {
	         e.printStackTrace();
	      	}
	      
	}
	BufferedWriter bw  = null; 
	BufferedWriter bwtitle  = null; 
	BufferedWriter bwDes = null ; 
	BufferedWriter bwInfo = null ; 
	public Ecriture () {
		try  {
			bw = new BufferedWriter(new FileWriter("SQL/Genre.sql"));
			bwtitle = new BufferedWriter(new FileWriter("SQL/Title.sql"));
			bwDes = new BufferedWriter(new FileWriter("SQL/Description.sql"));
			bwInfo =  new BufferedWriter(new FileWriter("SQL/Information.sql"));
		}
		catch(IOException io){
			System.out.println("erreur ouverture fichier SQL");
		}
	}
	
	public void fermeture () {
		try {
			bw.close() ; 
			bwtitle.close() ; 
			bwDes.close() ; 
			bwInfo.close(); 
		}
		catch (IOException io){
			System.out.println("Erreur fermer"); 
		}
	}
	
	public static String translate(String src) {
        StringBuffer result = new StringBuffer();
        if(src!=null && src.length()!=0) {
            int index = -1;
            char c = (char)0;
            String chars= "àâäéèêëîïôöùûüç&\"\'#|§%-_()`£$µ~{}[]*+=\n\r\t";
            String replace= "aaaeeeeiioouuuc                                                        ";
            for(int i=0; i<src.length(); i++) {
                c = src.charAt(i);
                if( (index=chars.indexOf(c))!=-1 ){
                	int c0 = (int)c ;
                	if(c0 > 122)
                		result.append("");
                	else 
                    result.append(replace.charAt(index));
                    
                }
                else
                    result.append(c);
            }
        }
        return result.toString();
    }
	
	public static String translate2(String src) {
        StringBuffer result = new StringBuffer();
        if(src!=null && src.length()!=0) {
            int index = -1;
            char c = (char)0;
            String chars= "&\"\'#|§ %";
            String replace= " ";
            for(int i=0; i<src.length(); i++) {
                c = src.charAt(i);
                if( (index=chars.indexOf(c))!=-1 )
                    result.append(replace);
                else
                    result.append(c);
            }
        }
        return result.toString();
    }
	
	public String treatement(String des){
		String rep = translate(des) ; 
		return rep ;  
		
	}
	
	public void tableDesc (String nom) {
		 try {	
	         File inputFile = new File(nom);
	         DocumentBuilderFactory dbFactory 
	            = DocumentBuilderFactory.newInstance();
	         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	         Document doc = dBuilder.parse(inputFile);
	         doc.getDocumentElement().normalize();
	         NodeList nList = doc.getElementsByTagName("Game");
	         if(nList.getLength()< 1) System.out.println("list null");
	            Node nNode = nList.item(0);
	            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
	            	 Element eElement = (Element) nNode;
		               String id =  eElement.getElementsByTagName("id").item(0).getTextContent();
		               String Overvieuw = null ; 
		               try {
		            	   Overvieuw =  eElement.getElementsByTagName("Overview").item(0).getTextContent();
		            	   Overvieuw = treatement(Overvieuw);
		               }
		               catch(Exception io){}
		               
		               ecrireDes(id,Overvieuw);
		               String ESRB = null; 
		               try {
		            	   ESRB =  eElement.getElementsByTagName("ESRB").item(0).getTextContent();
		            	   ESRB = ESRB.replaceAll("\'", " ");
		               }
		               catch(Exception io){
		               }
		               String  Players= null ; 
		               try {
		            	   Players=  eElement.getElementsByTagName("Players").item(0).getTextContent();
		               }
		               catch(Exception io){
		               }
		               String  Coop= null ; 
		               try {
		            	   Coop =  eElement.getElementsByTagName("Co-op").item(0).getTextContent();
		               }
		               catch(Exception io){
		               }
		               String  Publisher = null; 
		               try {
		            	   Publisher =  eElement.getElementsByTagName("Publisher").item(0).getTextContent();
		            	   Publisher = Publisher.replaceAll("\'", " ");
		               }
		               catch(Exception io){
		               }
		               String Developer = null;
		               try {
		            	   Developer =  eElement.getElementsByTagName("Developer").item(0).getTextContent();
		            	   Developer = Developer.replaceAll("\'", " ");
		               }
		               catch(Exception io){
		               }
		               String Rating = null ;
		               try {
		            	   Rating =  eElement.getElementsByTagName("Rating").item(0).getTextContent();
		               }
		               catch(Exception io){
		               }
		               ecrireInfo (id,ESRB,Publisher , Developer ,Players,Coop, Rating );
	            }
      }
      catch(Exception e){
    	  System.out.println("erreur + " + nom + " \n" );
    	  e.printStackTrace(); 
    	  nbErreur ++ ; 
      }
	}
	public void ecrireInfo (String id, String ER , String Pub , String dev , String pla , String coo , String rat){
			String  insertion= "INSERT INTO Information VALUES("+id+",";
			if(ER == null){
				insertion += "NULL," ; 
			}
			else 
				insertion+=	"\'"+ER+"\',";
			if(Pub == null){
				insertion+="NULL,";
			}
			else 
				insertion +="\'"+Pub+"\'," ;
			if(dev == null){
				insertion+="NULL,";
			}
			else 
				insertion += "\'"+dev+"\',";
			if(pla == null){
				insertion+="NULL,";
			}
			else{
				 if (pla.equals("4+"))
						insertion += 10+"," ;
				 else {	
				try {
					int i = Integer.parseInt(pla);
					if( i > 4 )
						System.out.println(" + grand  : " + i ) ; 
					}
				catch (Exception e){
					System.out.println(" pas un nombre " + pla) ; 
					
				}
				insertion += pla+"," ; 
				 }
			}
			if(coo == null)
				insertion+="NULL,";
			else {
				if(coo.equals("Yes"))
					insertion += "True," ;
				else if (coo.equals("No"))
					insertion += "False," ;
				else {
					System.out.println("coo : "+ coo );
					insertion +="\'"+coo+"\',";	
				}
			}
			if(rat == null)
				insertion+="NULL";
			else 
				insertion += rat ;
			
			insertion += ");" ; 
			try {
				bwInfo.write(insertion);
				bwInfo.flush();
				bwInfo.newLine();
			}
			catch (IOException io){
				System.out.println("erreur ecriture Genre "); 
			}
	}
	public void ecrireDes (String id , String des){
		String  insertion= "INSERT INTO Description VALUES("+id+",";
		if(des == null){
			insertion += "NULL" ; 
		}
		else 
			insertion+=	"\'"+des+"\'";
		insertion += ");" ; 
		try {
			bwDes.write(insertion);
			bwDes.flush();
			bwDes.newLine();
		}
		catch (IOException io){
			System.out.println("erreur ecriture Genre "); 
		}
	}
	
	public void tabletitle (String nom){
	      try {	
		         File inputFile = new File(nom);
		         DocumentBuilderFactory dbFactory 
		            = DocumentBuilderFactory.newInstance();
		         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
		         Document doc = dBuilder.parse(inputFile);
		         doc.getDocumentElement().normalize();
		         NodeList nList = doc.getElementsByTagName("Game");
		         if(nList.getLength()< 1) System.out.println("list null");
		            Node nNode = nList.item(0);
		            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
		               Element eElement = (Element) nNode;
		               String id =  eElement.getElementsByTagName("id").item(0).getTextContent();
		               String GameTitle =  eElement.getElementsByTagName("GameTitle").item(0).getTextContent();
		               GameTitle = GameTitle.replaceAll("\'", " ");
		               String PlatformId =  eElement.getElementsByTagName("PlatformId").item(0).getTextContent();
		               String releaseDate = null ; 
		               try {
		            	   releaseDate =  eElement.getElementsByTagName("ReleaseDate").item(0).getTextContent();
		               }
		               catch (Exception e){
		            	 //  System.out.println("pas de date"); 
		               }
		               ecrireTitle(id,GameTitle,PlatformId,releaseDate);
		            }
	      }
	      catch(Exception e){
	    	  System.out.println("erreur + " + nom + " \n" );
	    	  e.printStackTrace(); 
	    	  nbErreur ++ ; 
	    	  File  f = new File(nom);
	    	  f.delete();
	      }
	}
	
	public void ecrireTitle (String id , String title , String platform , String date){
		String  insertion= "INSERT INTO Title VALUES("+id+",\'"+title+"\',"+platform +",";
		if(date == null){
			insertion += "NULL" ; 
		}
		else {
			//System.out.println("taille date : "+date.length() + " | " +date);
			if(date.length() == 10)
				insertion +=date.substring(6);
			else if (date.length() == 9)
				insertion +=date.substring(5);
			else if (date.length() ==8)
				insertion +=date.substring(4);
			else 
				insertion+= "'"+ date+"'" ; 
		}
		insertion += ");" ; 
		try {
			bwtitle.write(insertion);
			bwtitle.flush();
			bwtitle.newLine();
		}
		catch (IOException io){
			System.out.println("erreur ecriture Genre "); 
		}
	}
	public void ecrireGenre (String id , int [] tab) {
		String  insertion= "INSERT INTO Genre VALUES("+id+"," ;
		for (int i = 0 ; i < tab.length ; i ++){
			insertion += tab[i] ; 
			if(i != tab.length -1){
				insertion+="," ; 
			}
		}
		insertion += ");" ; 
		try {
			bw.write(insertion);
			bw.flush();
			bw.newLine();
		}
		catch (IOException io){
			System.out.println("erreur ecriture Genre "); 
		}
	}
	public boolean justeGenre (String nom){
		  try {	
		         File inputFile = new File(nom);
		         DocumentBuilderFactory dbFactory 
		            = DocumentBuilderFactory.newInstance();
		         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
		         Document doc = dBuilder.parse(inputFile);
		         doc.getDocumentElement().normalize();
		         NodeList nList = doc.getElementsByTagName("genre");
		        // if(nList.getLength()> 1) System.out.println("2 genre");
		         int [] tabg = new int [19] ;
		         for (int i = 0 ; i < nList.getLength() ; i++) {
		            Node nNode = nList.item(i);
		            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
		              // Element eElement = (Element) nNode;
		               String un =  nNode.getTextContent();
		               //String GameTitle =  eElement.getElementsByTagName("GameTitle").item(0).getTextContent();
		              // System.out.println("un :" + un); 
		               //ajoutGenres(un);
		               boolean trouver = classeGenre(un,tabg);
		               if(!trouver){
		            	   System.out.println("genre non trouver");
		               }
		            }
		            
		         }
		         String id = doc.getElementsByTagName("id").item(0).getTextContent() ; 
		         ecrireGenre(id,tabg); 
		  }
		  catch (Exception io){
			  System.out.print("erreur : " + nom + " \n");io.printStackTrace() ;
			  nbErreur ++ ;
			  return false ; 
		  }
		  return true; 
	}
	
	public  void ajoutGenres (String genre) {
		if(!tag.contains(genre)){
			tag.add(genre);
		}
		
	}
	
	public boolean classeGenre (String nom , int [] tab){
		//int [] tab = new int [19]; 
		if( nom.equals("Adventure")){
			tab[0] = 1 ;
			return true ; 
		}
		else if (nom.equals("Role-Playing")){
			tab[1] = 1 ; 
			return true; 
		}
		else if(nom.equals("Action")){
			tab[2] = 1 ; 
			return true ; 
		}
		else if(nom.equals("Puzzle")){
			tab[3] = 1 ; 
			return true ;
		}
		else if (nom.equals("Shooter")){
			tab[4] = 1 ; 
			return true ; 
		}
		else if (nom.equals("Sports")){
			tab[5] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Platform")){
			tab[6] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Strategy")){
			tab[7] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Fighting")){
			tab[8] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Stealth")){
			tab[9] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Racing")){
			tab[10] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Flight Simulator")){
			tab[11] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("MMO")){
			tab[12] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Sandbox")){
			tab[13] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Horror")){
			tab[14] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Construction and Management Simulation")){
			tab[15] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Life Simulation")){
			tab[16] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Music")){
			tab[17] = 1 ; 
			return true  ; 
		}
		else if (nom.equals("Vehicle Simulation")){
			tab[18] = 1 ; 
			return true  ; 
		}
		else 
			return false  ; 
	}
	
	public void finish () {
		System.out.println("taille : " + tag.size());
		int i = 0 ; 
		for (String e : tag){
			System.out.println(i + " : " +e );
			i++ ; 
		}
		System.out.println("nberreur : " + nbErreur);
	}
	public void insertNom (String id , String nom){
		
	}

}
