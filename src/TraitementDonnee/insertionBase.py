//AUTEUR  : Navarna 
import mysql.connector 


def baseDonnee (nom) :
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    f = open(nom, "r")
    contenu = f.read() 
    contenuEnLigne = contenu.split("\n")
    for ligne in contenuEnLigne:
        ajout = ligne 
        try :
            cursor.execute(ligne)
        except Exception as e:
            print type(e)     # the exception instance
            print e.args      # arguments stored in .args
            print e           # __str__ allows args to be printed directly  
    conn.commit() 
    cursor.close() 
    conn.close()
    print("fini" ) 

def test () : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Title ; """)
    for (id2 , titre ,PlatformID , Sortie)  in cursor :
        print (id2 ) 
    cursor.close()
    conn.close()
  
 
baseDonnee("../SQL/Information.sql")
baseDonnee("../SQL/Description.sql") 
baseDonnee("../SQL/Title.sql")
baseDonnee("../SQL/Genre.sql")  
