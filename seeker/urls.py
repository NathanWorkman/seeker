"""seeker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from seeker.job import views as job_views

router = routers.DefaultRouter(trailing_slash=False)
router.register('jobs', job_views.JobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job_views.JobListView.as_view(), name="jobs"),
    path('<int:pk>/', job_views.JobDetailView.as_view(), name="job_detail"),
    path('search/', job_views.SearchResultsView.as_view(), name="search_results"),
    path('feed/', job_views.JobsFeed(), name="rss"),
    path('api/v1/', include(router.urls)),
]

import seeker.jobs  # noqa
