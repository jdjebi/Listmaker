class Liste:
	def __init__(self,cols=[],lines=[]):
		self.cols = cols
		self.lines = lines

	def __str__(self):
		cols = ",".join(self.cols)
		return "ListeObject({})".format(cols)

	def config_cols(self,cols):
		self.cols = cols

	def config_lines(self,lines):
		self.lines = lines

	def add_line(self,line):
		self.lines.append(line)

	def get_cols(self):
		return self.cols

	def get_lines(self):
		return self.lines

	def get_nbr_cols(self):
		return len(self.cols)

	def get_nbr_lines(self):
		return len(self.lines)

	def get_size(self):
		return self.get_nbr_cols(), self.get_nbr_lines()