from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import settings
from . import views

urlpatterns = [
   	path('',views.index,name='select'),
   	
    path('app/v1/<int:file_id>/',views.app,name='app'),
   	path('app/v1/nouveau/tableau-random/', views.new_random_tab,name='new_random_tab'),
   	path('app/v1/delete/<int:file_id>/', views.delete_tab,name='delete_tab'),
   	path('app/v1/export_results/<int:file_id>/', views.export_results_for_excel,name='export_results'),

   	path('admin/', admin.site.urls),
] 

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
