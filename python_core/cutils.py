import os

def br():
	print()

def clear(msg=""):
	os.system("cls")
	if msg:
		print(msg)

def get_listdir(path):
	return os.listdir(path)

def show_list(lst,showindex=True,style="-"):
	index = ""
	for i, elm in enumerate(lst):
		if showindex:
			index = i + 1
		print("{index}{style} {elm}".format(index=index,style=style,elm=elm))


