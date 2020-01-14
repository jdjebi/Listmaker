import sys

class LMK1Creator:

	FORMAT_SEPARATOR = ";"
	FILE_EXTENSION = ".lmk"

	def __init__(self,liste):
		self.liste_name = ""
		self.liste = liste
		self.save_path = ""

	def set_name(self,liste_name):
		self.liste_name = liste_name

	def set_save_path(self,path):
		self.save_path = path

	def get_filename(self):
		return self.liste_name + self.FILE_EXTENSION

	def get_save_path(self):
		return self.save_path

	def save(self, save_path=None):

		if not save_path:
			save_path = self.save_path

		cols_fmt = self.FORMAT_SEPARATOR.join(self.liste.cols)
		file = open(save_path,encoding='utf-8',mode="w")
		print(cols_fmt,file=file)
		for line in self.liste.lines:
			line_str = ";".join(line)
			print(line_str,file=file)
		file.close()