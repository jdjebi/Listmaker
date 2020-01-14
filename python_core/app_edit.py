""" Interface console de création de liste """
import os
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

def editor(liste,parser):
	""" Editeur  liste """
	# Initialisation
	close_str = "--Fermer--"
	liste_has_changed = False
	clear()
	while True:
		extra_edit_label = "\n"
		if liste_has_changed :
			extra_edit_label = "[liste modifiée]\n\n"
		print("{}Edition : \n{} \n".format(extra_edit_label,parser.get_path()))
		print("1- Afficher la liste")
		print("2- Insérer une ligne")
		print("3- Enregistrer")
		print("--------------------")
		print("4- Quitter l'édition")
		user_input = input("> ")
		#user_input = "2"
		if user_input == "4":
			break
		elif user_input == "1":
			lmk1viewer.LMK1Viewer.direct_viewer(liste)
			input(close_str)
		elif user_input == "3":
			if liste_has_changed:
				lmk_creator = lmk1creator.LMK1Creator(liste)
				lmk_creator.save(parser.get_path())
				print("Modifications enregistrées")
				liste_has_changed = False
			else:
				print("Aucune modification éffectuée")
				input("--OK--")
		elif user_input == "2":
			# Ajout d'une ligne
			cols = liste.get_cols() 
			nbr_col = len(cols)
			index_col = 0
			new_lines = []
			print("Champs: ",' | '.join(cols))
			while index_col < nbr_col: 
				data = input("{} > ".format(cols[index_col]))
				if data == "@skip":
					data = " "
				else:
					new_lines.append(data) 
				index_col += 1
			liste.add_line(new_lines)
			lmk1viewer.LMK1Viewer.direct_viewer(liste)
			liste_has_changed = True
			input(close_str)
		clear()
	print("\n==============================\n")

def execute_cmd(user_input,liste_files):
	if try_base_cmd(user_input):
		pass
	else:
		# Ouverture de la liste pour edition
		file = liste_files[int(user_input) - 1]
		path = os.path.join(PATH_FOLDER_FILES_CREATED,file)
		parser = lmk1parser.LMK1PARSER(path)
		liste = parser.parse()
		editor(liste,parser)
#===========================================
clear("Listmaker - ConsoleEditor [LMK1]\n")
liste_files = get_listdir(PATH_FOLDER_FILES_CREATED)
while True:
	print("Sélectionnez une liste\n")
	# Sélection d'une liste
	show_list(liste_files)
	print("\n(exit pour quitter)\n")
	user_input = input("> ")
	execute_cmd(user_input,liste_files)
	#execute_cmd("1")