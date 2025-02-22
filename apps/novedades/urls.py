from django.urls import path, include
from .views import(
	ListAnuncioView,
	DetailAnuncioView,
	AnuncioList
)

app_name= 'anuncios'
urlpatterns = [
    path('serializers/', AnuncioList.as_view(), name='novedades'),
	path('', ListAnuncioView.as_view(), name='list_anuncios'),
	path('<int:pk>/', DetailAnuncioView.as_view(), name='detail_anuncio')
]


#si quiere ver la api de novedades: localhost:8000/serializers/
