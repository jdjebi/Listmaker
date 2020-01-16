from django.http import HttpResponse

import os
import xlsxwriter

from cityselector.core.defines import EXCEL_FILES_FOLDER

def create_xlsx_file(path,data):
	workbook = xlsxwriter.Workbook(path)
	worksheet = workbook.add_worksheet()
	max_row = len(data)
	max_col = len(data[0])

	for i in range(0, max_row):
		for j in range(0, max_col):
			worksheet.write(i,j,data[i][j])
	workbook.close()

	with open(path,mode='rb') as excel:
		data = excel.read()
	return data


def get_excel_export_file_path(file):
	excel_filename = 'excel_' + file.get_basename() + '.xlsx'
	if not os.path.exists(EXCEL_FILES_FOLDER):
		os.makedirs(EXCEL_FILES_FOLDER)
	excel_file_path = os.path.join(EXCEL_FILES_FOLDER,excel_filename)
	return excel_file_path


def get_excel_download_response(path,data):
	response = HttpResponse(data,content_type='application/ms-excel')
	response['X-Sendfile'] = path
	response['Content-Length'] = os.stat(path).st_size
	response['Content-Disposition'] = 'attachement; filename="{}"'.format(os.path.basename(path))
	return response