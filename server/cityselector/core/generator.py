import string
from random import choice, randint, sample, randrange

def generate_etudiants():

	indices = list(string.ascii_uppercase + (string.ascii_uppercase).lower() + "0123456789") 
	#indices = list(string.ascii_uppercase) 

	titles = ['Nom','Sexe','Age','Niveau','Moyenne annuelle','Vie associative']

	etudiants = []

	sexes = ['F','M']
	niveaux_etude = ['L1','L2','L3','M1','M2']
	a_redouble = [0,1]
	moyennes_annuelle = list(range(10,20))
	vie_associative = ['CID','BASKET','FOOT']
		
	for indice in indices: 
		person_name = "Personne " + indice
		person_sexe = str(choice(sexes))
		person_niveau = str(choice(niveaux_etude))
		person_a_redouble = choice(a_redouble)
		person_moyenne_annuelle = str(choice(moyennes_annuelle)) + "." + str(randrange(0,99))
		person_age = str(randint(16,24))
		person_vie_scolaire_nbr_activitees = choice([0,1,2,3])
		person_vie_associative = "AUCUNE"

		if person_vie_scolaire_nbr_activitees != 0:
			person_vie_associative = "-".join(sample(vie_associative,k=person_vie_scolaire_nbr_activitees))	

		etudiants.append([person_name,person_sexe,person_age,person_niveau,person_moyenne_annuelle,person_vie_associative])

	return etudiants

	