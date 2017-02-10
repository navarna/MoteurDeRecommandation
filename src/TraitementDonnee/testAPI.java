//AUTEUR  : Navarna 
import com.mashape.unirest.http.*;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.mashape.unirest.request.HttpRequestWithBody;
import java.io.*;


public class testAPI {
 
	public static void ecrireFile (String e, int nb){
		
		//File f  = new File (nom) ; 
			try  { 
				if(e!= null){
					BufferedWriter bw = new BufferedWriter (new FileWriter("./DonneeSuite/jeu"+nb+".xml"));
					bw.write(e);
					bw.flush();
					bw.newLine();
					bw.close() ; 
				}
			}
			catch (IOException io){
				System.out.println("erreur d ecriture");
			}
	}
	
    public static void main(String[] args) throws UnirestException {
    	int nb = 1 ; 
    	while (nb < 36000){
	    		try {
			    	String recu ; 
			    	HttpRequestWithBody request = Unirest.post("http://thegamesdb.net/api/GetGame.php?id="+(nb)) ; 
			    	HttpResponse<String> file = request
			                .asString();
			    		System.out.println(" lol nb =" + nb+ " -> "+ file.getStatus());
			        recu = file.getBody() ; 
			        ecrireFile(recu, nb);
			        nb++ ; 
	    		}
	    		catch (Exception e){
	    		
	    		}
    		}
    	}
}

