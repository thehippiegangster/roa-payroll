from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.db.models import Q, Sum, F
from django.template import RequestContext
from django.urls import reverse_lazy
from django.db.models import FloatField
from django.db.models.functions import Cast

from .models import InvoiceSale, Salesled, Technician, Helper, Recled, Financing, Extra, InstallationRate, Employee


# Create your views here.

def home(request):
	return TemplateResponse(request, 'index.html')

def getInvoices(request):
	return TemplateResponse(request, 'GetInvoices.html')

'''def SearchView(request):
	return TemplateResponse(request, 'search.html', {'invoices': InvoiceSale.objects.all(), 'employees': Technician.objects.all()})'''

'''def ResultsView(request):
	return TemplateResponse(request, 'results.html', context=InvoiceSale)'''

class SearchView(TemplateView):
	template_name = 'search.html'

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context['invoices'] = InvoiceSale.objects.all()
		context['employees'] = Employee.objects.all()
		
		return context

class SearchCreateView(CreateView):
	template_name = 'search.html'
	success_url = reverse_lazy('search')

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context['invoices'] = InvoiceSale.objects.all()
		context['employees'] = Employee.objects.all()
		
		return context


class SearchUpdateView(UpdateView):
	template_name = 'search.html'
	success_url = reverse_lazy('search')

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context['invoices'] = InvoiceSale.objects.all()
		context['employees'] = Employee.objects.all()
		
		return context

def load_employees(request):

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context['invoices'] = InvoiceSale.objects.all()
		context['employees'] = Employee.objects.all()
		
		return context

	startDate = request.GET.get('startDate')
	endDate = request.GET.get('endDate')
	tech_inv = InvoiceSale.objects.filter(
		Q(invdate__gt=startDate) & 
		Q(invdate__lt=endDate)
		).values('salesman').distinct()
	tech_inv = InvoiceSale.objects.filter(
		Q(invdate__gt=startDate) & 
		Q(invdate__lt=endDate)
		).values('clerk').distinct()

	
	employees = Employee.objects.filter(Q(employee_id__in=tech_inv) | Q(employee_id__in=clerk_inv))
	

	return render(request, 'emp_dropdown_list_options.html', {'employees': employees})

class ResultsView(ListView):
	
	template_name = 'results.html'
	#emp_invoices = []
	
	def get_context_data(self, **kwargs):
		context = super(ResultsView, self).get_context_data(**kwargs)
		context['invoices'] = InvoiceSale.objects.all()
		context['technicians'] = Technician.objects.all()
		context['helper'] = Helper.objects.all()
		context['employees'] = Employee.objects.all()
		context['financing'] = Financing.objects.all()
		context['pending'] = self.get_pending_invoices
		context['payments'] = self.get_payments
		context['pmas'] = self.get_pma_invoices
		context['extras'] = self.get_extras
		context['hourly'] = self.get_hourly
		context['paymentfees'] = self.get_pmt_fee
		context['splits'] = self.get_splits
		context['rate'] = self.get_rate
		'''context.update({
			'pending': self.get_pending_invoices
			})'''

		return context

	def get_queryset(self): # new
		startDate = self.request.GET.get('start')
		endDate = self.request.GET.get('end')
		employee = self.request.GET.get('employee')
		invoices = []

		emp_invoices = InvoiceSale.objects.filter(
			Q(invdate__gt=startDate) & 
			Q(invdate__lt=endDate) &
			(Q(salesman__employee_id=employee) | 
			Q(clerk__employee_id=employee))
		)	

		return emp_invoices

	def get_pending_invoices(self):
		emp_invoices = self.get_queryset()

		pendList = Salesled.objects.filter(
			Q(invoice__in=emp_invoices) &
			Q(desc__icontains='PENDING')
		)

		return pendList

	def get_pma_invoices(self):
		emp_invoices = self.get_queryset()
		
		pmaList = Salesled.objects.filter(
			Q(invoice__in=emp_invoices) &
			Q(desc__icontains='PREVENTATIVE MAINTENANCE AGREEMENT')
		)

		return pmaList

	def get_pmt_fee(self):
		financefees = []
		costs = Recled.objects.annotate(
			cost_as_float=Cast(
				'paymethod__cost', output_field=FloatField())
			)

		'''for c in costs:
			financefee = c.cost_as_float/100
			financefees.append(financefee)'''

		return costs

	def get_payments(self):
		emp_invoices = self.get_queryset()
		
		payments = Recled.objects.filter(invoice__in=emp_invoices)
		
		return payments

		#Sales.MatCost + (RecLed.PayMethod = financing type).desc
		#return payments
		
	def get_extras(self):
		emp_invoices = self.get_queryset()

		extras = Salesled.objects.filter(invoice__in=emp_invoices).exclude(
			Q(desc__icontains='PMA') |
			Q(desc__icontains='PREVENTATIVE MAINTENANCE AGREEMENT') | 
			Q(desc__icontains='PENDING')
		)

		return extras

	def get_hourly(self):
		
		employee = self.request.GET.get('employee')
		hourly = Technician.objects.filter(employee_id=employee)

		for emp in hourly:
			return emp.hourly

	def get_splits(self):
		emp_invoices = self.get_queryset()

		splits = Salesled.objects.filter(
			Q(invoice__in=emp_invoices) &
			(Q(desc__icontains='SPLIT SYSTEM') |
			Q(desc__icontains='PACKAGE UNIT') | 
			Q(desc__icontains='NEW LINESET') |
			Q(desc__icontains='NEW DUCT RUN') |
			Q(desc__icontains='EXISTING DUCT RUN REPLACED') |
			Q(desc__icontains='NEW T-STAT WIRE'))
		)

		return splits

	def get_rate(self):
		employee = self.request.GET.get('employee')
		rate = InstallationRate.objects.filter(employee_id=employee)
		if(rate != None and rate.count() > 0):
			return rate[0]
		else: 
			return None



