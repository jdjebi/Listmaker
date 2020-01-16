from cityselector.core import algo
from cityselector.core.csv_utils import get_csv_data

def run_selection(path):
	file_data = get_csv_data(path)	
	vectors = algo.prepare_data(file_data)
	scores = algo.run_asme2(vectors)
	data_to_export = algo.get_classement_only(file_data,scores)
	return data_to_export