""" Interface console de création de liste """
import os
import listeObject
import lmk1viewer
import lmk1creator
from cutils import br, clear, get_listdir, show_list

#============================================
# Defines
PATH_FOLDER_FILES_CREATED = "test_files_created"

# Fonctions
def base_cmd(user_input):
	if user_input == "clear":
		clear()
	else:
		return False
	return True

def get_liste_params():
	liste_name = input("Nom de la liste > ")
	cols_csv_lite_str = input("Colonnes > ")
	cols = cols_csv_lite_str.split(lmk1creator.LMK1Creator.FORMAT_SEPARATOR)
	return liste_name, cols

def create_liste():
	""" 
		Créer une liste à partir d'un formatage de colonne 
		- Créer une liste vide avec colonne
	"""
	clear("Création de liste\n")
	# Récupération des caractéristiques de la liste
	liste_name, cols = get_liste_params()
	# Création de liste
	liste = listeObject.Liste(cols)
	# Sauvegarde
	save_path = save_liste(liste,liste_name)
	print("\nListe {} créée.\n".format(save_path))

def save_liste(liste,liste_name):
	lmk_creator = lmk1creator.LMK1Creator(liste)
	lmk_creator.set_name(liste_name)
	save_path = os.path.join(PATH_FOLDER_FILES_CREATED,lmk_creator.get_filename())
	lmk_creator.save(save_path)
	return save_path

def display_all_liste():
	""" Affiche toutes les liste du dossier """
	print("\nListes crées [Dossier: {}]\n".format(PATH_FOLDER_FILES_CREATED))
	files = get_listdir(PATH_FOLDER_FILES_CREATED)
	show_list(files,style='.')
	print("\n==========================\n")

def execute_cmd(user_input):
	if base_cmd(user_input):
		pass
	elif user_input == "1":
		create_liste()
	elif user_input == "2":
		display_all_liste()
	elif user_input == "3":
		exit()
	else:
		print("Commande inconnue\n")

#===========================================
clear()
print("Listmaker - ConsoleCreator [LMK1]\n")
while True:
	print("1- Créer une liste")
	print("2- Afficher les listes créées")
	print("3- Quitter\n")
	user_input = input("> ")
	execute_cmd(user_input)