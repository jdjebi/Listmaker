import os
import re
import sys
import webbrowser
import subprocess
import threading
import signal

from setup import *
import python_core.lmk.lmk1.listeObject as listeObject
import python_core.lmk.lmk1.lmk1creator as lmk1creator
import python_core.lmk.lmk1.lmk1parser as lmk1parser
from python_core.lmk.lmk1.viewer import LMK1Viewer
from python_core.cutils import *
from python_core import get_all_lmk_data

# Fonctions
def get_files():
	return get_all_lmk_data(LMK_DATA_DIR)


def get_file_by_str_id(str_id):
	liste = get_files()
	return liste[int(str_id) - 1]

def get_file_path(filename):
	return os.path.join(PATH_FOLDER_FILES_CREATED,filename)

def get_file_object_by_str_id(liste_id):
	filename = get_file_by_str_id(liste_id)
	path = get_file_path(filename)
	parser = lmk1parser.LMK1PARSER(path)
	return parser.parse(), os.path.abspath(path)

# Commandes
def view_all():
	print("\nListes:",PATH_FOLDER_FILES_CREATED)
	show_list(get_files())

def view(liste_id):
	liste, path = get_file_object_by_str_id(liste_id) 
	print("Fichier:{}".format(path))
	LMK1Viewer.direct_viewer(liste)

def open_cmd(liste_id):
	liste, path = get_file_object_by_str_id(liste_id)
	cmd = "python {} -f {}".format(CONFIG["GUI_LMK_VIEWER"],path)
	os.system(cmd)

def info(liste_id):
	liste, path = get_file_object_by_str_id(liste_id) 
	print("\nID:",liste_id)
	print("Liste:",path)
	print("Colonnes:",", ".join(liste.get_cols()))
	print("Nombres de lignes:",liste.get_nbr_lines())

def create_liste_cmd(liste_name):
	# Créer de la liste: Définition des colonnes
	cols_csv_lite_str = input("Colonnes > ")
	if cols_csv_lite_str == "@t":
		cols = ["A","B","C"]
	else:
		cols = cols_csv_lite_str.split(lmk1creator.LMK1Creator.FORMAT_SEPARATOR)
	liste = listeObject.Liste(cols)
	# Sauvegarde view_table
	lmk_creator = lmk1creator.LMK1Creator(liste)
	lmk_creator.set_name(liste_name)
	save_path = get_file_path(lmk_creator.get_filename())
	lmk_creator.save(save_path)
	print("Liste {} créée.".format(save_path))

def insert():
	global Manager
	# Ajout d'une ligne
	cols = Manager.liste_object_selected.get_cols() 
	nbr_col = len(cols)
	index_col = 0
	can_save = True
	new_lines = []
	print("\nChamps: ",' | '.join(cols))
	while index_col < nbr_col: 
		data = input("{}: ".format(cols[index_col]))
		if data == "@skip":
			data = " "
		elif data == "@stop":
			can_save = False
			break
		else:
			new_lines.append(data) 
		index_col += 1
	if can_save == True:
		Manager.liste_object_selected.add_line(new_lines)
		LMK1Viewer.direct_viewer(Manager.liste_object_selected)
		Manager.liste_has_changed = True	

def save():
	global Manager
	if Manager.liste_has_changed:
		lmk_creator = lmk1creator.LMK1Creator(Manager.liste_object_selected)
		lmk_creator.save(parser.get_path())
		print("Modifications enregistrées")
		Manager.liste_has_changed = False
	else:
		print("Aucune modification éffectuée")
		input("--OK--")

def create_liste():
	# Créer de la liste: Définition des colonnes
	liste_name = input("Nom de la liste > ")
	create_liste_cmd(liste_name)

def del_cmd(liste_id):
	liste, path = get_file_object_by_str_id(liste_id) 
	LMK1Viewer.direct_viewer(liste)
	print("\nVoulez vous vraiment supprimer cette liste ? (Oui/Non)")
	user_input = input("> ")
	if user_input == "Oui":
		os.remove(path)
		print("Liste {} supprimée".format(path))
	else:
		print("\nSupression annulée")

# Fin commandes
liste_selected = ""
liste_id_selected = ""
liste_object_selected = None
liste_has_changed = False

# tests
class test:
	@classmethod
	def cmd_open(cls):
		files = get_files()
		files_path = [os.path.abspath(get_file_path(filename)) for filename in files]
		rtel1_file_path = files_path[4]

		try:
			open(rtel1_file_path)
		except FileNotFoundError:
			print("Fichier introuvable: {}".format(rtel1_file_path))
		else:
			cmd = "python LmkViewer1.py open -f {}".format(rtel1_file_path)
			os.system(cmd)

	@classmethod
	def django_server(cls):
		os.system("start python CitySelector\\manage.py runserver")

	@classmethod
	def django_server_subprocess(cls):
		def open_webviewer():
			p = subprocess.Popen(["python","CitySelector\\manage.py","runserver"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
		#threading.Thread(target=open_webviewer,args=()).start()



class CliManager:
	def __init__(self):
		self.init()

	def init(self):
		self.liste_selected = ""
		self.liste_id_selected = ""
		self.liste_object_selected = None
		self.liste_has_changed = False

Manager = CliManager()

def main():
	global Manager

	clear("ListMaker CLI 2")
	while True:
		if Manager.liste_selected:
			if Manager.liste_has_changed:
				extra_tag = "~ "
			else:
				extra_tag = ""
			print("\n{}Fichier: {}".format(extra_tag,Manager.liste_selected))
			user_input = input("> ")
		else:
			user_input = input("\n> ")

		if user_input == "exit":
			break

		elif user_input == "clear":
			clear()
		
		elif user_input == "list":
			view_all()

		elif re.match("^select: (.)+",user_input):
			Manager.liste_id_selected = user_input[8:]
			Manager.liste_selected = get_file_by_str_id(Manager.liste_id_selected)
			path = get_file_path(Manager.liste_selected)
			parser = lmk1parser.LMK1PARSER(path)
			Manager.liste_object_selected = parser.parse()

		elif user_input == "unselect":
			Manager.init()

		elif re.match("^view: [0-9]+",user_input):
			view(user_input[6:])

		elif re.match("^open: [0-9]+",user_input):
			open_cmd(user_input[6:])

		elif re.match("^info: [0-9]+",user_input):
			info(user_input[6:])

		elif re.match("^create: (.)+",user_input):
			print("Nouvelle liste:")
			create_liste_cmd(user_input[8:])

		elif re.match("^del: [0-9]+",user_input):
			del_cmd(user_input[5:])

		elif re.match("^runserver",user_input):
			os.system("start python server\\manage.py runserver 0.0.0.0:8000")
			print("Serveur ListMaker lancé")
			url	= "http://{host}/".format(host="localhost:8000")
			webbrowser.open(url)

		elif Manager.liste_selected != "":
			if re.match("^view",user_input):
				view(Manager.liste_id_selected)
			elif re.match("^open",user_input):
				open_cmd(Manager.liste_id_selected)
			elif re.match("^info",user_input):
				info(Manager.liste_id_selected)
			elif re.match("^insert",user_input):
				insert()
			elif re.match("^save",user_input):
				save()
			else:
				print("Commande inconnue")
		else:
			print("Commande inconnue")

if __name__ == "__main__":
	main()
	#get_all_lmk_data(LMK_DATA_DIR)