"""payroll URL Configuration

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
from django.urls import path, include
from payrollsite import views



import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    #path('payroll/', include('payrollsite.urls')),
    #webapp views
    path('', views.home, name='homepage'),
    path('getInvoices/', views.getInvoices, name='getInvoices'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('add/', views.SearchCreateView.as_view(), name='emp_add'),
    path('<int:pk>/', views.SearchUpdateView.as_view(), name='emp_change'),
    path('ajax/load_employees/', views.load_employees, name='load_employees'),
    path('results/', views.ResultsView.as_view(), name='results'),
]