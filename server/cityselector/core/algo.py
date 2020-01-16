import numpy as np

def prepare_data(data):
	vectors = []
	licences = {'L1':1,'L2':2,"L3":3,"M1":4,"M2":5}
	sexe_pt = {'M':1,'F':2}
	vie_scolaire_tag = "AUCUNE"

	for row in data:
		sexe = sexe_pt[row[1].strip()]
		age = float(row[2])
		licence = licences[row[3].strip()]
		moyenne = float(row[4])
		_vie_scolaire = row[5].strip()
		if vie_scolaire_tag == _vie_scolaire:
			vie_scolaire = 0
		else:
			vie_scolaire = len(_vie_scolaire.split('-'))
		vectors.append([sexe,age,licence,moyenne,vie_scolaire])

	return vectors


def run_asme2(vectors):
	COLS_TO_MINIMATE = [2,3]

	matrice_poids = [
		[1, 400, 400, 400, 400],
		[1/400, 1, 1/80, 6, 3],
		[1/400, 80, 1, 80, 80],
		[1/400, 1/6, 1/80, 1, 2],
		[1/400, 1/3, 1/80, 1/2, 1],
	]

	POIDS = np.sum(matrice_poids,axis=1)

	return ASME2(vectors,POIDS,COLS_TO_MINIMATE)


def get_classement(etudiants,scores):
	classement = []

	for i, row in enumerate(etudiants):
		row.append(scores[i])
		classement.append(row)

	classement.sort(key=lambda e: e[-1],reverse=True)

	return classement

def get_classement_only(etudiants,scores):
	""" Retourne les résultats sans le score """
	classement = []
	tmp_classement = get_classement(etudiants,scores)

	# On rétire les scores
	for e in tmp_classement:
		classement.append(e[0:-1])

	return classement


def minimize(vectors,cols_to_minimate):
	""" Effectue la minimisation des critères décroissant """
	if cols_to_minimate:
		max_row, max_col = vectors.shape
		for col_num in cols_to_minimate:
			J = col_num - 1
			mx_col_action = vectors.max(0)[J]
			for i in range(0, max_row):
				vectors[i][J] = mx_col_action - vectors[i][J]
	return vectors


def WPM_normalize(vectors):
	""" Normanilisation relatives des actions """
	max_row, max_col = vectors.shape
	cols_sum_val = np.sum(vectors,axis=0)

	for i in range(0,max_row):
		for j in range(0,max_col):
			vectors[i][j] = vectors[i][j] / cols_sum_val[j]

	return vectors


def SommePondere(vectors, poids_):
	""" Détermine les scores: Agrégation complète, Somme des ratios"""
	scores = []
	max_row, max_col = vectors.shape
	for i in range(0, max_row):
		R = 0
		for j in range(0, max_col):
			R += poids_[j] * vectors[i][j]
		scores.append(R)
	return scores


def ASME2(vectors,poids,cols_to_minimate):
	# Initialisation
	action_vectors = np.array(vectors)

	# Minimisation
	action_vectors = minimize(action_vectors,cols_to_minimate)

	# Normalisation des aij
	action_vectors =  WPM_normalize(action_vectors)

	# Normalisation des poids
	poids_ = poids / np.sum(poids)

	# Somme pondérée
	scores = SommePondere(action_vectors,poids_)

	return scores