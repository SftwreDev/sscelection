from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.BaseView.as_view(), name='base'),
	path('results/', views.ResultsView.as_view(), name='results'),
]