//AUTEUR  : Navarna 
import mysql.connector 
from random import sample
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def LesPlusPopulaires() : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    cursor.execute ("""SELECT MAX(note) FROM Information ; """) 
    maximum = cursor.fetchone()
    cursor.execute("""SELECT id,titre , note FROM Information NATURAL JOIN Title where note = %s; """,maximum )
    info = []  
    L = []
    for x in cursor :
        info.append(x )
    if(len(info) > 14) :
        L = sample(info , 15 )
    else :
        cursor.execute("""SELECT id, titre ,note FROM Information NATURAL JOIN Title where note IS NOT NULL ORDER BY note DESC; """ )
        i = 0 
        for x in cursor :
            if( i  < 15 ) :
                L.append(x) 
                i  = i +1 
    cursor.close()
    conn.close()
    return L 


def clientLesPlusPopulaires () :
    L = LesPlusPopulaires() 
    for e in L:
        print("id : "+(str)(e[0])+"  -> titre : "+e[1]+" -> note : "+(str)(e[2])+" " ) 
    

def choixGenre () :
    print("Choix des genres : Entrer 1 pour montrer que vous aimers , 0 sinon ") 
    genre = () 
    reponse = () 
    try : 
            genre  = genre + (input(" Adventure\n"),) 
            genre = genre + (input("Role-Playing\n"),)
            genre  = genre + (input("Action\n"),)
            genre = genre + (input ("Puzzle\n" ),) 
            genre  =  genre +(input("Shooter\n"),)
            genre  = genre  + (input("Sports\n"),)
            genre = genre +(input("Platform\n"),)
            genre = genre +(input ("Strategy\n"),)
            genre = genre + (input("Fighting\n"),)
            genre = genre + (input("Stealth\n") ,)
            genre = genre + (input("Racing\n") ,)   
            genre = genre + (input("Flight Simulator\n"),)
            genre = genre + (input("MMO\n"),)
            genre = genre + (input("Sandbox\n"),)
            genre = genre + (input("Horror\n"),)
            genre = genre + (input("Construction and Management Simulation\n"),)
            genre = genre + (input("Life Simulation\n"),)
            genre = genre + (input("Music\n"),)
            genre = genre + (input("Vehicle Simulation\n"),)
            for e in genre : 
                if(e != 1 ) : 
                    reponse = reponse + (0,)
                else :
                    reponse = reponse + (e,) 
    except Exception as e : 
        print("erreur dans les Entrer , aucun genre Choisie par defaut ") 
        reponse = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    return reponse

def InteractionCreationClient(pseudo) :
    print(" Questionnaires du client " ) 
    if(pseudo == "" ) :  
        pseudo = raw_input("Entrez Votre pseudo : (si c est votre premieres fois le pseudo sera cree)\n")
        if(pseudo == "") :
            print ("Pseudo non correct" ) 
            return 
    genre = choixGenre()
    esbrVal  = ("E - Everyone","E10+ - Everyone 10+","EC - Early Childhood","M - Mature","RP - Rating Pending","T - Teen")
    Esbr = raw_input("Entrez Un ESBR si vous le souhaiter sinon ne rien entrer\n ESBR possible :\n" +esbrVal[0]+"\n"+esbrVal[1]+"\n"+esbrVal[2]+"\n"+esbrVal[3]+"\n"+esbrVal[4]+"\n"+esbrVal[5]+"\n")
    if(Esbr not in esbrVal) :
        Esbr = "NULL" 
    try :
        nbJoueur = input ("Entrer le nombre de joueurs prefere  de 1 a 3 ou 10 si vous souhaiter un jeu sans nombre maximun ,si vous ne souhaiter pas remplir cette case entrer 0 \n")
    except Exception as e :
        nbJoueur = "NULL" 
        System.out.println("entree incorrect , pas de choix enregistrer pour le nombre de joueur " )
    nbJoueurVal = (1,2,3,10)
    if(nbJoueur not in nbJoueurVal):
        nbJoueur = "NULL"
    coop = raw_input ("Entrer si vous souhaiter un jeu en ligne 'Yes' ou 'No' ou 'NULL' si vous passez cette information ") 
    coopVal = ("Yes" , "No" , "NULL" ) 
    if( coop not in coopVal) :
        coop  =  "NULL"
    insertion_update (pseudo , genre , Esbr , nbJoueur , coop) 
    return pseudo 

def insertion_update (pseudo , genre , Esbr , nbJoueur , coop ) : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    use = (pseudo,) 
    cursor.execute ("""Select * from Client where Pseudo = %s ;""", use)
    trouver = False 
    for e in cursor  :
        trouver  = True
    if(trouver)  : 
        use = (genre[0],genre[1],genre[2],genre[3],genre[4],genre[5],genre[6],genre[7],genre[8],genre[9],genre[10],genre[11],genre[12],genre[13],genre[14],genre[15],genre[16],genre[17],genre[18],Esbr , nbJoueur , coop , pseudo)
        cursor.execute( """ Update Client set Adventure = %s , Role_Playing = %s , Actions = %s ,Puzzle = %s ,Shooter = %s ,Sports = %s ,Platform = %s ,Strategy = %s , Fighting = %s ,Stealth = %s, Racing = %s,Flight_Simulator = %s ,MMO = %s ,SandBox = %s ,horror= %s ,Construction_and_Management_Simulation = %s , Life_Simulation = %s ,Music = %s ,Vehicle_Simulation = %s , ESBR1 = %s ,  nbJoueur  = %s , coop = %s where Pseudo = %s ;""",use)
        conn.commit() 
    else :
        user = (pseudo,)
        cursor.execute ("""insert into Client(Pseudo)  values (%s)""",user) 
        conn.commit() 
        use = (genre[0],genre[1],genre[2],genre[3],genre[4],genre[5],genre[6],genre[7],genre[8],genre[9],genre[10],genre[11],genre[12],genre[13],genre[14],genre[15],genre[16],genre[17],genre[18],Esbr , nbJoueur , coop , pseudo)
        cursor.execute( """ Update Client set Adventure = %s , Role_Playing = %s , Actions = %s ,Puzzle = %s ,Shooter = %s ,Sports = %s ,Platform = %s ,Strategy = %s , Fighting = %s ,Stealth = %s, Racing = %s,Flight_Simulator = %s ,MMO = %s ,SandBox = %s ,horror= %s ,Construction_and_Management_Simulation = %s , Life_Simulation = %s ,Music = %s ,Vehicle_Simulation = %s , ESBR1 = %s ,  nbJoueur  = %s , coop = %s where Pseudo = %s ;""",use)
    conn.commit() 
    cursor.close()
    conn.close()
            




def LesChoixDuClient (pseudo) :
    L = [] 
    variable  = ("id" , "pseudo" ,"Adventure" , "Role_Playing", "Actions","Puzzle","Shooter","Sports","Platform","Strategy", "Fighting","Stealth","Racing","Flight_Simulator","MMO","SandBox","horror","Construction_and_Management_Simulation" , "Life_Simulation","Music" ,"Vehicle_Simulation", "ESBR", "nbJoueur", "coop")
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    use = (pseudo,) 
    cursor.execute ("""Select * from Client where Pseudo = %s ;""", use)
    trouver = False 
    der = () 
    for e in cursor  :
        trouver  = True
        der = e ;
    if(trouver) :
        for i  in range (2, 21) :
            if (der[i] == 1 ) :
                option = (variable[i],der[i])
                lol = "Select Genre.id,note from Genre,Information where "+option[0]+"= "+ str(der[i])+ " AND Genre.id = Information.id;" 
                cursor.execute (lol)
                for e,u in cursor :
                    a = 10
                    if(u != None) :
                       a  = float(u)/7 +2 
                    L.append((e,a))
        for i in range (21,24):
            if((der[i] != None )and (der[i] != 0))  :
                option = (variable[i],der[i])
                option2 = (der[i],)
                lol  =  "Select Genre.id,note from Genre,Information where "+option[0]+"= "
                lol2 = " AND Genre.id = Information.id;"
                cursor.execute (lol+" %s " + lol2 , option2)
                for e,u in cursor :
                    a = 9
                    if(u != None) :
                        a = float(u)/7 +1 
                    L.append((e,a))
        reponse = [] 
        enr = []
        for e,v in L :
            if(e not in enr) :
                enr.append(e) 
                reponse.append((e,v) ) 
            else :
                var = enr.index(e) 
                (re,rv) = reponse[var]
                reponse[var] = (re, rv+v)
        L2 = sorted(reponse,key=itemgetter(1), reverse = True)
        if(len(L2) > 15):
            L2 = L2[:15] 
        L3 = []
        for e in L2 :
             option = (e[0],)
             cursor.execute (""" Select id,Titre, note from Title Natural Join Information  where Title.id = %s;""",option)
             for res in cursor :
                 L3.append(res)
        cursor.close()
        conn.close()
        return L3 
    else :
        cursor.close()
        conn.close()
        return L 

def compareTitre (e) :
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT titre FROM Title where id = %s; """,option)
    L = [] 
    enr = [] 
    for el in cursor : 
        if( el[0] == None ):
            return {}
        L.append(el[0] ) 
        enr.append(e)
    cursor.execute("""SELECT titre,id FROM Title where id != %s; """,option)
    for el in cursor : 
        L.append(el[0])
        enr.append(el[1])
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(L)
    #print (tfidf) 
    # pairwise_similarity = (tfidf * tfidf.T).A
    pairwise_similarity = cosine_similarity(tfidf[0:1], tfidf)
    #print (pairwise_similarity) 
    reponse = {} 
    for i in range (0, len(L)):
        reponse[enr[i]] = pairwise_similarity[0][i]
    cursor.close()
    conn.close()
    return reponse 

def comparePlatforme(e) : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT PlatformID FROM Title where id = %s; """,option)
    L = [] 
    enr = [] 
    for el in cursor :
        if (el[0] == None) :
            return {}
        L.append(el[0] ) 
        enr.append(e)
    cursor.execute("""SELECT PlatformID,id FROM Title where id != %s; """,option)
    for el in cursor : 
        L.append(el[0])
        enr.append(el[1])
    val  = L[0]
    reponse = {}
    for i in range (0,len(L)) :
        if( val == L[i] ) :
            reponse[enr[i]] = 1 
        else :
            reponse[enr[i]] = 0 
    cursor.close()
    conn.close()
    return reponse 

def compareAnnee(e) :
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT Sortie FROM Title where id = %s; """,option)
    L = [] 
    enr = [] 
    for el in cursor :
        if(el[0] == None) :
            return {}
        L.append(el[0] ) 
        enr.append(e)
    cursor.execute("""SELECT Sortie,id FROM Title where id != %s; """,option)
    for el in cursor : 
        L.append(el[0])
        enr.append(el[1])
    cursor.execute("""select (max(Sortie) - min(Sortie) )from Title ;""")
    maximumDifference = () 
    for m in cursor :
        maximumDifference = m
    val  = L[0]
    reponse = {}
    for i in range (0,len(L)) :
        valeur  = 0 
        if(L[i] != None) :
            deduction = (max(val,L[i]) - min (val,L[i]))
            valeur = (float(maximumDifference[0] - deduction)) / maximumDifference[0]   
        reponse[enr[i]] = valeur 
    cursor.close()
    conn.close()
    return reponse 
        
def compareGenre (e) : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT * FROM Genre where id = %s; """,option)
    L = [] 
    enr = [] 
    for el in cursor : 
        val = () 
        for i in  range(0, len(el)):
            if( i != 0 ):
                val = val + (el[i] ,) 
            else :
                enr.append(el[0])
        L.append(val) 
    cursor.execute("""SELECT * FROM Genre where id != %s; """,option)
    for el in cursor : 
        val = () 
        for i in  range(0, len(el)):
            if( i != 0 ):
                val = val + (el[i] ,) 
            else :
                enr.append(el[0])
        L.append(val ) 
    pairwise_similarity = cosine_similarity(L[0:1], L)
    reponse = {}
    for i in range (0 , len(L) ):
        reponse[enr[i]] =  pairwise_similarity[0][i]
    cursor.close()
    conn.close()
    return reponse 


def compareDescription (e) :
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT Description FROM Description where id = %s; """,option)
    L = [] 
    enr = [] 
    for el in cursor : 
        if(el[0] != None): 
            L.append(el[0] ) 
            enr.append(e)
    
    cursor.execute("""SELECT Description,id FROM Description where id != %s; """,option)
    for el in cursor : 
        if(el[0] != None):
            L.append(el[0])
            enr.append(el[1])
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(L)
    pairwise_similarity = cosine_similarity(tfidf[0:1], tfidf)
    reponse = {}
    for i in range (0, len(L)):
        reponse[enr[i]]= pairwise_similarity[0][i]
    cursor.close()
    conn.close()
    return reponse 

def compareInformation (e) : 
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT * FROM Information where id = %s; """,option)
    L = []
    enr = []
    for el in cursor : 
        enr.append(e)
        L.append(el) 
    cursor.execute("""SELECT * FROM Information where id != %s; """,option)
    for el in cursor : 
            L.append(el)
            enr.append(el[0])
    val  = L[0]
    reponseMulti = {}
    indice=  0 
    for el in L :
        valTotal  = 0 
        for i in range(0,len(el)) :
            if((i != 0 ) and (i != len(el)-1)):
                if(val[i] == el[i]) : 
                    valTotal = valTotal +1 
        valTotal = float(valTotal)/5
        reponseMulti[enr[indice]] = valTotal 
        indice = indice +1 
    cursor.close()
    conn.close()
    return reponseMulti 

def itemSimilaire(e) :
    dtitre = compareTitre(e) 
    dplatforme = comparePlatforme(e) 
    dannee  = compareAnnee(e) 
    dgenre = compareGenre(e) 
    ddescription = compareDescription(e)
    dInformation = compareInformation(e)
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    option = (e,) 
    cursor.execute("""SELECT id FROM Title; """)
    L = []
    for el in cursor : 
        L.append(el[0]) 
    reponse = []
    for i in range (0, len(L) ) :
        valTitre = 0 
        valPlat = 0
        valAnnee = 0 
        valGenre = 0 
        valDesc = 0
        valInfo = 0 
        if(dtitre.has_key(L[i])):
            valTitre = dtitre[L[i]]
        if(dplatforme.has_key(L[i])):
            valPlat = dplatforme[L[i]]
        if(dannee.has_key(L[i])) :
            valAnnee = dannee[L[i]]
        if(dgenre.has_key(L[i])) :
            valGenre = dgenre[L[i]]
        if(ddescription.has_key(L[i])) :
            valDesc = ddescription[L[i]]
        if(dInformation.has_key(L[i])) :
            valInfo = dInformation[L[i]]
        dTotal = (2*valTitre + 2*valPlat + valAnnee + 3*valDesc + 4*valGenre +  3*valInfo)/15 ;
        reponse.append((L[i], dTotal) ) 
    cursor.close()
    conn.close()
    return reponse


def JeuxSimilaireDecoup(L) :
    L1 = [] 
    for e in L :
        item  = itemSimilaire(e) 
        for en in item :
            L1.append(en) 
    reponse = [] 
    enr = []
    
    for e,v  in L1 :
        if(e not in enr) :
            enr.append(e) 
            reponse.append((e,v) ) 
        else :
            var = enr.index(e) 
            (re,rv) = reponse[var]
            reponse[var] = (re, rv+v)
    L2 = sorted(reponse,key=itemgetter(1), reverse = True)
    if(len(L2) > 15):
        L2 = L2[:15] 
    L3 = []
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    for e in L2 :
        option = (e[0],)
        cursor.execute (""" Select id,Titre, note from Title Natural Join Information  where Title.id = %s;""",option)
        for res in cursor :
            L3.append(res) 
    cursor.close()
    conn.close()
    return L3 

def JeuxSimilaire(pseudo) :
    if(pseudo == "") :
        return [] 
    else :
        conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
        cursor = conn.cursor()
        use = (pseudo,) 
        cursor.execute ("""Select id from Favoris where idClient =( Select idClient from Client where Pseudo = %s) ;""", use)
        trouver = False 
        der = () 
        for e in cursor  :
            der = e ;
        cursor.close()
        conn.close()
        L = JeuxSimilaireDecoup(der) 
        return L 



def connection(pseudo):
    if(pseudo == "") :
        return False 
    else :
        conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
        cursor = conn.cursor()
        use = (pseudo,) 
        cursor.execute ("""Select idClient from Client where Pseudo = %s ;""", use)
        trouver = False 
        for e in cursor  :
            trouver = True 
        cursor.close()
        conn.close()
        return trouver

def connexion() :
    quest = raw_input("Avez vous deja un compte ? (oui/non)")
    if(quest == "oui"):
        quest = raw_input("Entrer votre pseudo :\n")
        ok   = connection(quest) 
        if(ok) :
            return quest 
        else :
            print ("compte non trouver\n")
            return "" 
    else  :
        return InteractionCreationClient("") 

def changerPreferance (pseudo ) : 
    if (pseudo == "" ) :
        print ("Vous n'etes pas connecter" ) 
    else :
        InteractionCreationClient(pseudo) 

def ClientLesChoixDuClient(pseudo):
    if(pseudo == "") :
        print ("Vous n'etes pas connecter" ) 
    else :
         L = LesChoixDuClient (pseudo)
         for e in L:
             print("id : "+(str)(e[0])+"  | titre : "+e[1]+" | note : "+(str)(e[2])+" " ) 


def verifID (idc ) :
    if(idc == 0) :
        return False 
    else :
        conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
        cursor = conn.cursor()
        use = (idc,) 
        cursor.execute ("""Select * from Title where id = %s ;""", use)
        trouver = False 
        for e in cursor  :
            trouver = True 
        cursor.close()
        conn.close()
        return trouver

def ClientItemSimilaire()  :
    idC = 0 
    try: 
        idC = input ("entrer l'id du film etant la base de la recherche\n") 
    except Exception  :
        print ("Entrer incorrect" ) 
        return 
    if(verifID(idC)):
        L = itemSimilaire(idC) 
        L= sorted(L,key=itemgetter(1), reverse = True)
        L = L[:15]
        L3 = [] 
        conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
        cursor = conn.cursor()
        for e in L :
            option = (e[0],)
            cursor.execute (""" Select id,Titre, note from Title Natural Join Information  where Title.id = %s;""",option)
            for res in cursor :
                L3.append(res)
        for e in L3:
            print("id : "+(str)(e[0])+"  -> titre : "+e[1]+" -> note : "+(str)(e[2])+" " )
        cursor.close()
        conn.close()
    else : 
        print("ID inconnu ") 
        

def ClientJeuxSimilaire(pseudo) :
    if(pseudo == "") :
        print ("Vous n'etes pas connecter" ) 
    else :
        L = JeuxSimilaire(pseudo)
        for e in L:
            print("id : "+(str)(e[0])+"  ->  titre : "+e[1]+" -> note : "+(str)(e[2])+" " )

def inserer_Favoris( pseudo , idC , note) :
    print ("pseudo : " + str(pseudo ) + " id : " + str(idC) + " note " + str(note))
    conn = mysql.connector.connect(host="localhost",user="root",password="doliprane", database="BDFouille")
    cursor = conn.cursor()
    use = (pseudo,) 
    cursor.execute ("""Select * from Client where Pseudo = %s ;""", use)
    trouver = False
    id2 = 0
    for e in cursor  :
        trouver  = True
        id2 = e[0]
    if(trouver)  :
        use = (idC,id2)
        cursor.execute ("""Select * from Favoris where id =%s AND idClient =%s ;""", use)
        for e in cursor  :
            trouver= False 
    
    if(trouver) :
        user = (idC,id2,note)
        cursor.execute ("""insert into Favoris values (%s,%s,%s)""",user) 
        conn.commit() 
    else :
        user = (note,idC,id2)
        cursor.execute( """ Update Favoris set note = %s where id = %s AND idClient = %s;""",user)
        conn.commit() 
    cursor.close()
    conn.close()


def AjouterFavoris (pseudo) :
    if(pseudo == "") :
        print ("Vous n'etes pas connecter" ) 
    else :
        idC = 0 
        try: 
            idC = input ("entrer l'id du film etant la base de la recherche\n") 
        except Exception  :
            print ("Entrer incorrect" ) 
            return 
        if(verifID(idC)):
            note = 0 
            try: 
                note = input ("entrer l'id du film etant la base de la recherche de 1 a 5\n") 
            except Exception  :
                print ("Entrer incorrect" ) 
                return 
            inserer_Favoris(pseudo,idC,note)


def menu (): 
    pseudo  = ""
    fini = False 
    while ( not fini):
        print("Choissiser vos recommandation : entrer des nombres")
        print("        1.   Jeux les plus populaires");
        print("        2.   Jeux correspondant aux preference de votre profil")
        print("        3.   Jeux similaires a un autre Jeux") 
        print("        4.   Jeux que vous pourrez aimer") 
        print("        5.   Se connecter (necessaires pour 2 et 4)")
        print("        6.   Changer ses preference")
        print("        7.   Ajouter un film au favoris") 
        print("        8.   Quitter")
        rep = 0 
        try : 
          rep = input()
        except Exception :
            print("Entrer non valide\n") 
        if(rep == 1 ):
            clientLesPlusPopulaires() 
        elif (rep == 2 ) :
            ClientLesChoixDuClient(pseudo)
        elif(rep == 3 ) :
            ClientItemSimilaire() 
        elif (rep == 4 ) :
            ClientJeuxSimilaire(pseudo) 
        elif (rep == 5 ) :
            pseudo = connexion() 
            if(pseudo != "") :
                print("connexion reussi") 
        elif (rep == 6 ) :
            changerPreferance(pseudo) 
        elif(rep == 7 ) :
            AjouterFavoris(pseudo) 
        elif(rep ==8) :
            fini = True 
        else :
            print("Entrer non valide\n" ) 
menu()
