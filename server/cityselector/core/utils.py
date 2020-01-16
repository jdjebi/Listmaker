import os

def get_filename(filename):
	return os.path.splitext(filename)[0]


def numerize(tab):
	tab_numerize = []
	for i, row in enumerate(tab):
		tab_numerize.append([i+1] + row)
	return tab_numerize