from tabulate import tabulate

class LMK1Viewer:
	TABLEFMT = "psql"
	SHOWINDEX = "always"

	def __init__(self,liste):
		self.liste = liste

	@classmethod
	def build_table(cls,lines,headers,showindex,tablefmt):
		return tabulate(lines,headers=headers,showindex=showindex,tablefmt=tablefmt)

	@classmethod
	def direct_viewer(cls,liste):
		""" Affiche un format de tableau directement à partir de la liste en paramètre """
		table_str = cls.build_table(liste.lines,liste.cols,cls.SHOWINDEX,cls.TABLEFMT)
		print(table_str)

	def get_table_str(self):
		return self.build_table(self.liste.lines,self.liste.cols,self.SHOWINDEX,self.TABLEFMT)

	def show(self):
		print(self.get_table_str())