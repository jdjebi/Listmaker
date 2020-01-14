import os
import argparse
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from setup import *
import python_core.lmk.lmk1.lmk1parser as lmk1parser

class Win(Tk): 
	def __init__(self):
		super().__init__()
		self.title("LmkViewer - ListMaker")

		self.listeObj = None
		self.container = None
		self.table = None
		self.table_columns = None
		self.vsb = None

		self.initUI()

	def initUI(self):
		self.container = Frame(self)	
		self.container.pack(side=TOP, fill=BOTH, expand=1) 	

	def view_table(self,file):
		parser = lmk1parser.LMK1PARSER(file)
		parser.parse()
		self.listeObj = parser.get_liste() 

		liste_cols = self.listeObj.get_cols()
		liste_lines = self.listeObj.get_lines()

		self.table_columns_name = [col.lower().replace(" ","_") for col in liste_cols]

		# Tableau
		table = self.table = ttk.Treeview(self.container, columns=self.table_columns_name)
		
		# Définition des colonnes du tableau
		table.column("#0", width=60, stretch=NO)
		table.heading('#0', text='n°')

		for i, column in enumerate(self.table_columns_name):
			table.heading(column, text=liste_cols[i])

		#TConfiguration des tags
		table.tag_configure("bg1", background="#E8E8E8")
		table.tag_configure("bg2", background="#fff")

		vsb = self.vsb = ttk.Scrollbar(self.container,orient="vertical",command=table.yview)
		table.configure(yscrollcommand=vsb.set)

		#Placement
		table.pack(side=LEFT, fill=BOTH, expand=1)
		vsb.pack(side=RIGHT, fill=Y)

		# Ajout des données
		for i, line_values in enumerate(liste_lines):
			tag = "bg1"

			if i % 2:
				tag = "bg2"

			self.table.insert('', 'end', text=str(i+1), values=line_values, tags=('item',tag))

def main(file):
	app = Win()
	app.view_table(file)
	app.mainloop()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--file")
	args = parser.parse_args()
	
	if args.file == None:
		print("Erreur lors de l'ouverture du fichier .lmk Il est peut être introuvable.")
	else:
		main(args.file)