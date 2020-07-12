from django import forms
from .models import InvoiceSales, Technician

class PayrollSearchForm(forms.ModelForm):
    class Meta:
        model = InvoiceSales
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salesman'].queryset = Technician.objects.none()

        if 'start' and 'end' in self.data:
            try:
                startDate = date(self.data.get('start'))
		endDate = date(self.data.get('end'))
		fil_inv = InvoiceSale.objects.filter(
		Q(invdate__gt=startDate) & 
		Q(invdate__lt=endDate)
		)
                self.fields['salesman'].queryset = Technician.objects.filter(technician=fil_inv.salesman__technician)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['salesman'].queryset = Technician.objects.none()