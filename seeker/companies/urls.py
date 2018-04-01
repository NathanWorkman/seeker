from django.urls import path
from .views import CompanyDetailView, CompanyListView


urlpatterns = [
    path('<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('', CompanyListView.as_view(), name='company_list'),
]
