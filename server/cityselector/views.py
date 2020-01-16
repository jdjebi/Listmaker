"""
- Importation de fichier
- Renforcer le code
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView

from .models import CsvFile
from .core.generator import generate_etudiants
from .core.messages import Notify
from .core import algo
from .core.csv_utils import create_csv_file, get_csv_data
from .core.excel import create_xlsx_file, get_excel_download_response, get_excel_export_file_path
from .core.utils import get_filename, numerize
from .core.extras import run_selection

import os
		
MSG_CSV_FILE_NOT_FOUND = '{}: Fichier de données introuvable'

class CsvFileList(ListView):
	model = CsvFile
	template_name = 'index.html'
	context_object_name = 'csv_files'

index = CsvFileList.as_view()


class AppView(ListView):
	template_name = 'app.html'
	context_object_name = 'etudiants'
	paginate_by = 30

	def setup(self,request, *args, **kwargs):
		super().setup(request,args,**kwargs)
		self.doc_results = False

		if request.GET.get('show_results') == '1':
			self.doc_results = True

	def get_queryset(self):
		etudiants = get_csv_data(self.csv_file.path)	

		if self.doc_results:
			data = algo.prepare_data(etudiants)
			scores = algo.run_asme2(data)
			etudiants = algo.get_classement(etudiants,scores)

		etudiants = numerize(etudiants)

		return etudiants

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['csv_file'] = self.csv_file
		context['csv_files'] = CsvFile.objects.all()
		context['doc_results'] = self.doc_results
		return context

	def get(self,request,*args, **kwargs):
		self.csv_file = get_object_or_404(CsvFile,id=self.kwargs['file_id'])

		if not self.csv_file.check_local_file_exist():
			Notify.warning(request,MSG_CSV_FILE_NOT_FOUND.format(self.csv_file.get_name()))
			return redirect(index)

		return super().get(request,args,**kwargs)

app = AppView.as_view()

def new_random_tab(request):
	etudiants = generate_etudiants()

	file = CsvFile()
	file.save()

	filename = "random_table_{}.csv".format(file.id)

	file.path = create_csv_file(filename,etudiants)
	file.save()

	return redirect(index)


def delete_tab(request,file_id):
	file = get_object_or_404(CsvFile,id=file_id)
	excel_file = get_excel_export_file_path(file)

	if file.check_local_file_exist():
		os.remove(file.path)
	if os.path.exists(excel_file):
		os.remove(excel_file)
	file.delete()

	if request.GET.get('redirect_url'):
		return HttpResponseRedirect(request.get('redirect_url'))

	msg = "Fichier {} supprimé.".format(file.get_name())
	Notify.success(request,msg)

	return redirect(index)


def export_results_for_excel(request,file_id):
	file = get_object_or_404(CsvFile,id=file_id)

	if not file.check_local_file_exist():
		Notify.warning(request,MSG_CSV_FILE_NOT_FOUND.format(csv_file.get_name()))
		return redirect(index)
	else: # Création du fichier d'exportation
		results = run_selection(file.path)
		excel_file_path = get_excel_export_file_path(file)
		try:
			excel_file_data = create_xlsx_file(excel_file_path,results)
		except PermissionError:
			Notify.error(request,"Impossible d'exporter les résultats. Veuiller réassayer plus tard.")
		# Reponse de téléchargement
		return get_excel_download_response(excel_file_path,excel_file_data)