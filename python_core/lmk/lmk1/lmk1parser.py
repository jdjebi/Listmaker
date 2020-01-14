from . import listeObject

class LMK1PARSER:

	LMK1_SEPARATOR = ";"

	def __init__(self,path):
		self.path = path
		self.cols = []
		self.lines = []
		
	def parse(self):
		file = open(self.path,encoding='utf-8')

		# Extraction des données
		data = []
		file_lines = file.readlines()

		for line in file_lines:
			line = line.replace('\n','')
			line_elm = line.split(self.LMK1_SEPARATOR)
			data.append(line_elm)

		# Récupération des données
		self.cols = data[0] # colonnes
		self.lines = data[1:]

		file.close()

		return self.get_liste()

	def get_path(self):
		return self.path

	def get_cols(self):
		return self.cols

	def get_lines(self):
		return self.lines

	def get_liste(self):		
		return listeObject.Liste(self.cols,self.lines)

	