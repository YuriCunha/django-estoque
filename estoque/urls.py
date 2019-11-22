from django.contrib import admin
from django.urls import path, include

from core.views import index, cor, corNews, corDelete, corUpdate

urlpatterns = [
    path('', index, name='index'),
    path('cor/', cor, name='cor'),
    path('corNews/', corNews, name='corNews' ),
    path('corDelete/<int:pk>/', corDelete, name='corDelete'),
    path('corUpdate/<int:pk>/', corUpdate, name='corUpdate'),
    path('entrada/', include('notaEntrada.urls', namespace='notaEntrada')),
    path('admin/', admin.site.urls),
]
