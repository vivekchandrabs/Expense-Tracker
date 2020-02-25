"""expense_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from tracker.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("expense/", get_all_expense),
    path("income/", get_all_income),
    path("create_expense/", create_expense),
    path("delete_expense/<int:expense_id>/", delete_expense),
    path("expense/<int:expense_id>/", get_expense),
    path("expense_edit/<int:expense_id>/", expense_edit),
]
