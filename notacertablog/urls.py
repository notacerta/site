from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('sobre', views.sobre, name='sobre'),
	path('produto', views.produto, name='produto')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)