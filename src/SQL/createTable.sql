\echo "creationTable" 

CREATE TABLE IF NOT EXISTS Title (
       id INT PRIMARY KEY ,
       titre VARCHAR(100) NOT NULL,
       PlatformID INT,
       Sortie INT
      );

	CREATE TABLE IF NOT EXISTS Description (
	       id INT NOT NULL PRIMARY KEY,
	       Description VARCHAR(8000) 
	       
	);

CREATE TABLE IF NOT EXISTS  Genre (
       id INT NOT NULL PRIMARY KEY , 
       Adventure INT ,
       Role_Playing INT , 
       Actions INT ,
       Puzzle INT ,
       Shooter INT ,
       Sports  INT ,
       Platform INT ,
       Strategy INT,
       Fighting INT, 
       Stealth INT,
       Racing INT,
       Flight_Simulator INT ,
       MMO INT ,
       Sandbox INT ,
       Horror INT ,
       Construction_and_Management_Simulation INT,
       Life_Simulation INT ,
       Music INT ,
       Vehicle_Simulation INT
);


CREATE TABLE IF NOT EXISTS Information (
       id INT NOT NULL PRIMARY KEY ,
       ESBR VARCHAR(50) , 
       Producteur VARCHAR(100) ,
       Developer VARCHAR(100) ,
       nbJoueur INT ,
       coop VARCHAR (10) ,
       note FLOAT 
);

CREATE TABLE IF NOT EXISTS  Client (
       idClient INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	Pseudo VARCHAR(50),
       Adventure INT ,
       Role_Playing INT , 
       Actions INT ,
       Puzzle INT ,
       Shooter INT ,
       Sports  INT ,
       Platform INT ,
       Strategy INT,
       Fighting INT, 
       Stealth INT,
       Racing INT,
       Flight_Simulator INT ,
       MMO INT ,
       Sandbox INT ,
       Horror INT ,
       Construction_and_Management_Simulation INT,
       Life_Simulation INT ,
       Music INT ,
       Vehicle_Simulation INT,
	ESBR1 varchar(50),
	nbJoueur INT  ,
	coop varchar(10)
	
);


CREATE TABLE IF NOT EXISTS Favoris (
	id int, 
	idClient int, 
	note int,
	primary key(id,idClient) 

);
