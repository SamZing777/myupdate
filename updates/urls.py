from django.urls import path

from .views import (
		HomePageView, 
		UserCreateUpdateView,
		StaffBroadCastEmailView,
		UpdateDetailView,
		Savest
	)

urlpatterns = [
	path('', HomePageView.as_view(), name='index'),
	path('updates/', UserCreateUpdateView.as_view(), name='update_all'),
	path('updates/<int:pk>/', UpdateDetailView.as_view(), name='update_detail'),
	path('broadcast/', StaffBroadCastEmailView.as_view(), name='broadcast'),
	path('savest/', Savest.as_view(), name='savest')
]