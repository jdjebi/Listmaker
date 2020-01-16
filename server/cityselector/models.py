from django.db import models
import os



class CsvFile(models.Model):
	path = models.CharField(verbose_name="chemin",max_length=255,default='nopath',null=False,blank=False)
	date_creation = models.DateTimeField(auto_now_add=True)
	is_ok = models.BooleanField(verbose_name='etat du fichier de données',default=False)

	class Meta:
		verbose_name = 'Fichiers CSV'
		verbose_name_plural = 'Fichiers CSV'

		ordering = ('-date_creation',)

	def get_name(self):
		return os.path.basename(self.path)

	def get_basename(self):
		return os.path.splitext(self.get_name())[0]

	def check_local_file_exist(self):
		if os.path.exists(self.path):
			self.is_ok = True
		else:
			self.is_ok = False
		self.save()
		return self.is_ok

"""
class Tableau(models.Model)
	titre = models.CharField(max_length="255",null=False,blank=False)
	titres = models.CharField(max_length="255",null=False,blank=False)

class Ligne(models.Model):
	tableau = models.ForeignKey(Tableau,on_delete=models.CASCADE,related_name='lignes')
"""