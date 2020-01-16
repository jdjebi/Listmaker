import csv
import os
from cityselector.core.defines import CSV_FILES_FOLDER

def get_csv_data(path):
	file = open(path,mode='r')

	data = [l for l in csv.reader(file)]

	return data


def create_csv_file(file_name,tab):

	if not os.path.exists(CSV_FILES_FOLDER):
		os.makedirs(CSV_FILES_FOLDER)

	csv_file_path = os.path.join(CSV_FILES_FOLDER,file_name)

	with open(csv_file_path, 'w',newline='') as csvfile:
	    writer = csv.writer(csvfile)

	    for row in tab:
	    	writer.writerow(row)

	return csv_file_path		