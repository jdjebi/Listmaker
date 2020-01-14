""" Interface console de création de liste """
import listeObject
import lmk1viewer
import lmk1creator
import lmk1parser
from cutils import *

#============================================
# Defines
PATH_FOLDER_FILES_CREATED = "test_files_created"

# Fonctions
def try_base_cmd(user_input):
	if user_input == "clear":
		clear()
	elif user_input == "exit":
		exit()
	else:
		return False
	return True

def execute_cmd(user_input,liste_files):
	try:
		int(user_input)
	except:
		br()
		if try_base_cmd(user_input):
			pass
		else:
			print("Commande inconnue\n")
		print("Listes:\n")
	else:
		liste_id = int(user_input) - 1
		file = liste_files[liste_id]
		# Affichage de la liste
		path = os.path.join(PATH_FOLDER_FILES_CREATED,file)
		parser = lmk1parser.LMK1PARSER(path)
		liste = parser.parse()
		print("\nAffichage de liste:",path,"\n")
		viewer = lmk1viewer.LMK1Viewer.direct_viewer(liste)
		input("Continuer...")
		print("\n==============================\n")
		print("Autre liste: \n")

#===========================================
clear("Listmaker - ConsoleReader [LMK1]\n")
liste_files = get_listdir(PATH_FOLDER_FILES_CREATED)
while True:
	# Sélection d'une liste
	show_list(liste_files)
	print("\n(exit pour quitter)")
	user_input = input("> ")
	execute_cmd(user_input,liste_files)