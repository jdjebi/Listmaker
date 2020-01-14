import os

def get_all_lmk_data(path_dir_list):
	files_path = []
	for path_dir in path_dir_list:
		abs_path_dir = os.path.abspath(path_dir)
		files = os.listdir(abs_path_dir)
		for file in files:
			path = os.path.join(abs_path_dir,file)
			files_path.append(path)
	return files_path
