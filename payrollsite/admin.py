from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#from liststyle import ListStyleAdminMixin

from payrollsite.models import Customer
from payrollsite.models import Extra
from payrollsite.models import Financing
from payrollsite.models import Helper
from payrollsite.models import InstallationRate
from payrollsite.models import Pmabonus
from payrollsite.models import Technician
from payrollsite.models import InvoiceSale
from payrollsite.models import Salesled
from payrollsite.models import WarrantyLabor
from payrollsite.models import Recled
from payrollsite.models import Employee

#admin models
class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        exclude_id = ('id',)
        import_id_fields = ('employee_id',)

class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ('employee_id', 'name', 'position')
    search_fields = ('employee_id', 'name')

class HelperAdmin(admin.ModelAdmin):
    list_display = ('helper', 'helper_emp_id', 'tech', 'tech_emp_id', 'tech_minimum', 'helper_minimum')
    search_fields = ('helper', 'tech', 'helper_emp_id') 

class TechnicianResource(resources.ModelResource):
    class Meta:
        model = Technician

class TechnicianAdmin(ImportExportModelAdmin):
    resource_class = TechnicianResource
    list_display = ('employee_id','technician', 'position', 'high_55', 'high_75', 'high_100', 'low_100', 'per_unit', 'weekly_minimum', 'effective_date', 'end_date', 'hourly', 'salary')
    search_fields = ('technician', 'position', 'employee_id')

class FinancingResource(resources.ModelResource):
    class Meta:
        model = Financing
   
    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None
class FinancingAdmin(ImportExportModelAdmin):
    resource_class = FinancingResource
    list_display = ('paymethod', 'type', 'desc', 'cost')
    search_fields = ('paymethod', 'type', 'desc')
    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custno', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname') 

class InvoiceSaleAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'invdate', 'salesman','clerk', 'customer', 'invamount', 'matcost')
    search_fields = ['invoice', 'salesman__technician', 'clerk__helper'] 
    #search_fields = ['invoice']

    '''def show_salesman(self, obj):
        return "\n".join([a.technician for a in obj.Technician_set.all()])'''

class SalesledAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'desc','quan', 'price', 'amount', 'warranty')
    search_fields = ['desc', 'invoice']

class RecledAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'custno','amount', 'paymethod') #need to finish adding fields
    search_fields = ['invoice', 'custno', 'paymethod']

class InstallRateAdmin(admin.ModelAdmin):
    list_display = ('name', 'package_unit', 'split_system', 'rate_percent', 'team_num')
    search_fields = ('name', 'team_num')

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Extra)
admin.site.register(Financing, FinancingAdmin)
admin.site.register(Helper, HelperAdmin)
admin.site.register(Technician, TechnicianAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(InvoiceSale, InvoiceSaleAdmin)
admin.site.register(Salesled, SalesledAdmin)
admin.site.register(Recled, RecledAdmin)
admin.site.register(InstallationRate, InstallRateAdmin)
admin.site.register(Pmabonus)
admin.site.register(WarrantyLabor)

