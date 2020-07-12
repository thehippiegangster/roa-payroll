from django.urls import path
from . import views

urlpatterns=[
	"""#webapp views
	path('', views.home, name='homepage'),
        path('getInvoices/', views.getInvoices, name='getInvoices'),
	path('search/', views.SearchView, name='search'),
	path('results/', views.ResultsView, name='results'),"""

	#admin views
	path('$/', views.estimates, name='estimates'),
	path('$/', views.extras, name='extras'),
	path('$/', views.financing, name='financing'),
	path('$/', views.helper, name='helper'),
	path('$/', views.installation, name='installation'),
	path('$/', views.installation_rates, name='installation_rates'),
	path('$/', views.installers, name='installers'),
	path('$/', views.installerspayment, name='installers_payment'),
	path('$/', views.pmabonus, name='pma_bonus'),
	path('$/', views.technician, name='technician'),
	path('$/', views.viewinvoices, name='view_invoices'),
	path('$/', views.viewinvoicesunits, name='view_invoices_units'),
	path('$/', views.warrantylabor, name='warranty_labor'),
	path('$/', views.employee, name='employee'),

]
