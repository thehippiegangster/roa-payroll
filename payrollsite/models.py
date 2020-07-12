# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remfove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=65)
    position = models.CharField(max_length=26)

    def __str__(self):
        return '%s %s' % (self.name, self.employee_id)

class Customer(models.Model):
    custno = models.CharField(db_column='CustNo', unique=True, max_length=7, primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    customerinactive = models.SmallIntegerField(db_column='CustomerInactive')  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateTimeField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=65, unique=True)  # Field name made lowercase.

    def __str__(self):
        return self.firstname+ ' ' + self.lastname

    class Meta:
        managed = False
        db_table = 'Customer'


class Financing(models.Model):
    paymethod = models.CharField(db_column='PayMethod', blank=False, unique=True, max_length=10, primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=10, default='0000')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=50, blank=True)  # Field name made lowercase.
    cost = models.CharField(db_column='Cost', blank=True, max_length=36)

    
    class Meta:
        managed = True
        db_table = 'Financing'
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"

    def __str__(self):
        return "%s %s" % (self.paymethod, self.cost)


class Helper(models.Model):
    tech = models.CharField(db_column='Tech', max_length=50)  # Field name made lowercase.
    helper = models.CharField(db_column='Helper', max_length=50)  # Field name made lowercase.
    tech_minimum = models.FloatField(db_column='Tech_Minimum')  # Field name made lowercase.
    helper_minimum = models.FloatField(db_column='Helper_Minimum')  # Field name made lowercase.
    tech_emp_id = models.CharField(max_length=5, blank=True)
    helper_emp_id = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return '%s %s' % (self.helper, self.helper_emp_id)    

    class Meta:
        managed = True
        db_table = 'Helper'


class InstallationRate(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True)
    name = models.CharField(max_length=50)
    package_unit = models.DecimalField(max_digits=6, decimal_places=2)
    split_system = models.DecimalField(max_digits=6, decimal_places=2)
    rate_percent = models.FloatField(null=True)
    team_num = models.IntegerField(null=True)

    def __str__(self):
        return '%s %s' % (self.employee_id, self.rate_percent)

    class Meta:
        managed = True
        db_table = 'InstallationRates'
        ordering = ['team_num']


class Installer(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=10)
    matCost = models.FloatField(db_column='MatCost', null=True, blank=True)
    total_cost = models.FloatField(db_column='Total_Cost', null=True, blank=True)
    invDate = models.DateField(db_column='InvDate', null=True, blank=True)
    employee = models.CharField(db_column='Employee', max_length=41, null=True, blank=True)
    payCash_amount = models.FloatField(db_column='PayCash_Amount', null=True, blank=True)
    payCheck_amount = models.FloatField(db_column='PayCheck_Amount', null=True, blank=True)
    payCC_amount = models.FloatField(db_column='PayCC_Amount', null=True, blank=True)
    payCredit_amount = models.FloatField(db_column='PayCredit_Amount', null=True, blank=True)
    payOther_amount = models.FloatField(db_column='PayOther_Amount', null=True, blank=True)
    collected = models.DecimalField(db_column='Collected', null=True, blank=True, max_digits=10, decimal_places=2)
    fullName = models.CharField(db_column='Fullname', max_length=65, null=True, blank=True)
    price = models.DecimalField(db_column='Price', null=True, blank=True, max_digits=10, decimal_places=2)
    pma_checks = models.FloatField(db_column='PMA_Checks', null=True, blank=True)
    split_with_amount = models.FloatField(db_column='SPLIT_WITH_Amount', null=True, blank=True)
    split_from_amount = models.FloatField(db_column='SPLIT_FROM_Amount', null=True, blank=True)
    pma_years = models.IntegerField(db_column='PMA_Years', null=True, blank=True)
    pma_quan = models.FloatField(db_column='PMA_Quan', null=True, blank=True)
    pma_amount = models.FloatField(db_column='PMA_Amount', null=False)
    splitFrom = models.CharField(db_column='SplitFrom', max_length=50, null=True, blank=True)
    splitWith = models.CharField(db_column='SplitWith', max_length=50, null=True, blank=True)
    payMethod = models.CharField(db_column='PayMethod', max_length=50, null=True, blank=True)
    pendUntil = models.DateField(db_column='PendUntil', null=True, blank=True)
    tech = models.CharField(db_column='Tech', max_length=50, null=True, blank=True)
    helper = models.CharField(db_column='Helper', max_length=50, null=True, blank=True)
    
    class Meta: 
       managed = True
       db_table = 'Installers'


class Pmabonus(models.Model):
    units = models.CharField(max_length=1)
    years = models.CharField(max_length=2)
    price = models.CharField(max_length=4)
    bonus = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'PMABonus'
        verbose_name = "PMA Bonus"
        verbose_name_plural = "PMA Bonuses"


class Technician(models.Model):
    technician = models.CharField(db_column='Technician', max_length=50)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=20)  # Field name made lowercase.
    high_55 = models.FloatField(db_column='HIGH_55', max_length=2)  # Field name made lowercase.
    high_75 = models.FloatField(db_column='HIGH_75', max_length=2)  # Field name made lowercase.
    high_100 = models.FloatField(db_column='HIGH_100', max_length=2)  # Field name made lowercase.
    low_100 = models.FloatField(db_column='LOW_100', max_length=2)  # Field name made lowercase.
    per_unit = models.FloatField(db_column='PER_UNIT', max_length=2)  # Field name made lowercase.
    weekly_minimum = models.CharField(db_column='WEEKLY_MINIMUM', max_length=10)  # Field name made lowercase.
    effective_date = models.DateField(db_column='EFFECTIVE_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', null=True)  # Field name made lowercase.
    hourly = models.FloatField(db_column='HOURLY', blank=True, null=True)  # Field name made lowercase.
    salary = models.FloatField(db_column='SALARY', null=True)  # Field name made lowercase.
    employee_id = models.CharField(max_length=5, blank=True, primary_key=True)


    def __str__(self):
        return '%s %s' % (self.technician, self.employee_id)

    class Meta:
        managed = True
        db_table = 'Technician'


class InvoiceSale(models.Model):
    invoice = models.CharField(db_column='Invoice', unique=True, max_length=10, primary_key=True)  # Field name made lowercase.
    regid = models.CharField(db_column='RegID', max_length=2)  # Field name made lowercase.
    #line_item = models.ManyToManyField('Salesled')
    #salesman = models.CharField(db_column='Salesman', max_length=4)
    salesman = models.ForeignKey(Employee, related_name='salesman', db_column='Salesman', max_length=4, on_delete=models.PROTECT, blank=True, null=True)
    #clerk = models.CharField(db_column='Clerk', max_length=4)
    clerk = models.ForeignKey(Employee, related_name='clerk', db_column='Clerk', max_length=4, on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
    dispatch = models.CharField(db_column='Dispatch', max_length=15)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, db_column='CustNo', on_delete=models.PROTECT)
    #custno = models.CharField(db_column='CustNo', max_length=7)  # Field name made lowercase.
    locno = models.CharField(db_column='LocNo', max_length=5)  # Field name made lowercase.
    pricecode = models.CharField(db_column='PriceCode', max_length=1)  # Field name made lowercase.
    dept = models.CharField(db_column='Dept', max_length=2)  # Field name made lowercase.
    invdate = models.DateField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    entdate = models.DateField(db_column='EntDate', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=6)  # Field name made lowercase.
    billloc = models.CharField(db_column='BillLoc', max_length=5)  # Field name made lowercase.
    invtype = models.CharField(db_column='InvType', max_length=21)  # Field name made lowercase.
    agrmtno = models.CharField(db_column='AgrmtNo', max_length=7)  # Field name made lowercase.
    wh = models.CharField(db_column='WH', max_length=4)  # Field name made lowercase.
    taxcode = models.CharField(db_column='TaxCode', max_length=8)  # Field name made lowercase.
    laborcost = models.FloatField(db_column='LaborCost')  # Field name made lowercase.
    printed = models.IntegerField(db_column='Printed')  # Field name made lowercase.
    amtcash = models.FloatField(db_column='AmtCash')  # Field name made lowercase.
    amtcharge = models.FloatField(db_column='AmtCharge')  # Field name made lowercase.
    amtcheck = models.FloatField(db_column='AmtCheck')  # Field name made lowercase.
    amtcreditc = models.FloatField(db_column='AmtCreditC')  # Field name made lowercase.
    amtchng = models.FloatField(db_column='AmtChng')  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=1)  # Field name made lowercase.
    exempt = models.FloatField(db_column='Exempt')  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=30)  # Field name made lowercase.
    txnid = models.TextField(db_column='TxnID')  # Field name made lowercase.
    invamount = models.FloatField(db_column='InvAmount')  # Field name made lowercase.
    quoteorg = models.CharField(db_column='QuoteOrg', max_length=10)  # Field name made lowercase.
    billcompl = models.SmallIntegerField(db_column='BillCompl')  # Field name made lowercase.
    billamount = models.FloatField(db_column='BillAmount')  # Field name made lowercase.
    matcost = models.FloatField(db_column='MatCost')  # Field name made lowercase.
    othercost = models.FloatField(db_column='OtherCost')  # Field name made lowercase.
    slterms = models.CharField(db_column='SlTerms', max_length=31)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    dispnotes = models.SmallIntegerField(db_column='DispNotes')  # Field name made lowercase.
    dispparts = models.SmallIntegerField(db_column='DispParts')  # Field name made lowercase.
    transid = models.CharField(db_column='TransID', unique=True, max_length=36)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    amtappliedcredits = models.FloatField(db_column='AmtAppliedCredits')  # Field name made lowercase.
    authorizeid = models.CharField(db_column='AuthorizeID', max_length=36)  # Field name made lowercase.
    acceptanceid = models.CharField(db_column='AcceptanceID', max_length=36)  # Field name made lowercase.

    @property
    def collected(self):
        return self.amtcash + self.amtcharge + self.amtcheck + self.amtcreditc
    
    def __str__(self):
        return '%s' % (self.invoice)
    
    class Meta:
        managed = False
        db_table = 'Sales'
        ordering = ['-invdate']
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"


class Salesled(models.Model):
    entryId = models.CharField(db_column='EntryID', max_length=36, primary_key=True)
    invoice = models.ForeignKey(InvoiceSale, db_column='Invoice', max_length=10, on_delete=models.PROTECT)  # Field name made lowercase.
    count = models.CharField(db_column='Count', max_length=3)  # Field name made lowercase.
    prod = models.CharField(db_column='Prod', max_length=36)  # Field name made lowercase.
    firstline = models.IntegerField(db_column='FirstLine')  # Field name made lowercase.
    desc = models.TextField(db_column='Desc')  # Field name made lowercase.
    quan = models.FloatField(db_column='Quan')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    wh = models.CharField(db_column='WH', max_length=4)  # Field name made lowercase.
    ptype = models.CharField(db_column='PType', max_length=1)  # Field name made lowercase.
    jbclass = models.CharField(db_column='JBClass', max_length=40)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=36)  # Field name made lowercase.
    sdebit = models.CharField(db_column='SDebit', max_length=10)  # Field name made lowercase.
    scredit = models.CharField(db_column='SCredit', max_length=10)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost')  # Field name made lowercase.
    cdebit = models.CharField(db_column='CDebit', max_length=10)  # Field name made lowercase.
    ccredit = models.CharField(db_column='CCredit', max_length=10)  # Field name made lowercase.
    tax1 = models.FloatField(db_column='Tax1')  # Field name made lowercase.
    tax2 = models.FloatField(db_column='Tax2')  # Field name made lowercase.
    tax3 = models.FloatField(db_column='Tax3')  # Field name made lowercase.
    tax4 = models.FloatField(db_column='Tax4')  # Field name made lowercase.
    epa = models.FloatField(db_column='EPA')  # Field name made lowercase.
    miscnum = models.FloatField(db_column='MiscNum')  # Field name made lowercase.
    warranty = models.DateTimeField(db_column='Warranty', blank=True, null=True)  # Field name made lowercase.
 
    '''def __str__(self):
        return self.InvoiceSale.invoice + ' ' + self.price'''
    def __unicode__(self):
        return "%s %s %s" % (self.invoice, self.price, self.desc)


    class Meta:
        managed = False
        db_table = 'SalesLed'
        #unique_together = (('invoice', 'count'),)
        ordering = ['-invoice__invdate']
        verbose_name = "Line Item"
        verbose_name_plural = "Line Items"


class Recled(models.Model):
    custno = models.ForeignKey(Customer, db_column='CustNo', max_length=7, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    invoice = models.ForeignKey(InvoiceSale, db_column='Invoice', max_length=10, on_delete=models.PROTECT)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=1)  # Field name made lowercase.
    counter = models.CharField(db_column='Counter', max_length=5)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    ckno = models.CharField(db_column='CkNo', max_length=12)  # Field name made lowercase.
    ckdate = models.DateTimeField(db_column='CkDate', blank=True, null=True)  # Field name made lowercase.
    depno = models.CharField(db_column='DepNo', max_length=10)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=6)  # Field name made lowercase.
    debit = models.CharField(db_column='Debit', max_length=10)  # Field name made lowercase.
    credit = models.CharField(db_column='Credit', max_length=10)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.
    crserial = models.CharField(db_column='CrSerial', max_length=5)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=1)  # Field name made lowercase.
    #paymethod = models.CharField(max_length=36)
    paymethod = models.ForeignKey(Financing, db_column='PayMethod', max_length=10, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    entryid = models.CharField(db_column='EntryID', unique=True, max_length=36, primary_key=True)  # Field name made lowercase.
    depositdate = models.DateTimeField(db_column='DepositDate', blank=True, null=True)  # Field name made lowercase.
    appliedfromid = models.CharField(db_column='AppliedFromID', max_length=36)  # Field name made lowercase.
    qbcredittxnid = models.CharField(db_column='QBCreditTxnID', max_length=36)  # Field name made lowercase.
    paymentid = models.CharField(db_column='PaymentID', max_length=36)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'RecLed'
        unique_together = (('custno', 'invoice', 'counter'),)
        ordering = ['-invoice__invdate']
        verbose_name = "Received Payment"
        verbose_name_plural = "Received Payments"

    def __unicode__(self):
        return "%s %s" % (self.invoice, self.amount)


class WarrantyLabor(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=16)  # Field name made lowercase.
    quan = models.FloatField(db_column='Quan')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'WarrantyLabor'

class Extra(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=16)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Extras'

class EmployeeInvoices(models.Model):
    invoice = models.ForeignKey(InvoiceSale, on_delete=models.DO_NOTHING, related_name='empinvoice')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Salesled, on_delete=models.DO_NOTHING)
    #saleamt = models.ForeignKey(InvoiceSale, on_delete=models.DO_NOTHING, related_name='saleamt')
    #parts = models.ForeignKey()
    #profit = models.ForeignKey()
    #pma = models.ForeignKey(Salesled, on_delete=models.DO_NOTHING)
    #extras = models.ForeignKey(Salesled, on_delete=models.DO_NOTHING)
    technician = models.ForeignKey(Technician, on_delete=models.DO_NOTHING)
    #flatrate = models.ForeignKey()
    def hourly(self):
        return technician.hourly

    @property
    def sales(self):
        return self.invoice.invamt
    
    @property
    def collected(self):
        return self.invoice.amtcash + self.invoice.amtcharge + self.invoice.amtcheck + self.invoice.amtcreditc

    @property
    def earnings(self):
        invoice.invamt + 2700
        return self.earnings

class ViewInvoice(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=10)  # Field name made lowercase.
    matcost = models.FloatField(db_column='MatCost', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.FloatField(db_column='Total_Cost', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=41, blank=True, null=True)  # Field name made lowercase.
    paycash_amount = models.FloatField(db_column='PayCash_Amount', blank=True, null=True)  # Field name made lowercase.
    paycheck_amount = models.FloatField(db_column='PayCheck_Amount', blank=True, null=True)  # Field name made lowercase.
    paycc_amount = models.FloatField(db_column='PayCC_Amount', blank=True, null=True)  # Field name made lowercase.
    paytrade_amount = models.FloatField(db_column='PayTrade_Amount', blank=True, null=True)  # Field name made lowercase.
    paycredit_amount = models.FloatField(db_column='PayCredit_Amount', blank=True, null=True)  # Field name made lowercase.
    payother_amount = models.FloatField(db_column='PayOther_Amount', blank=True, null=True)  # Field name made lowercase.
    collected = models.FloatField(db_column='Collected', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=65, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    pma_checks = models.FloatField(db_column='PMA_Checks', blank=True, null=True)  # Field name made lowercase.
    split_with_amount = models.FloatField(db_column='SPLIT_WITH_Amount', blank=True, null=True)  # Field name made lowercase.
    split_from_amount = models.FloatField(db_column='SPLIT_FROM_Amount', blank=True, null=True)  # Field name made lowercase.
    pma_years = models.IntegerField(db_column='PMA_Years', blank=True, null=True)  # Field name made lowercase.
    pma_quan = models.FloatField(db_column='PMA_Quan', blank=True, null=True)  # Field name made lowercase.
    pma_amount = models.FloatField(db_column='PMA_Amount')  # Field name made lowercase.
    splitfrom = models.CharField(db_column='SplitFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splitwith = models.CharField(db_column='SplitWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymethod = models.CharField(db_column='PayMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    penduntil = models.DateField(db_column='PendUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ViewInvoices'


class ViewInvoicesUnit(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=10)  # Field name made lowercase.
    matcost = models.FloatField(db_column='MatCost', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.FloatField(db_column='Total_Cost', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=41, blank=True, null=True)  # Field name made lowercase.
    paycash_amount = models.FloatField(db_column='PayCash_Amount', blank=True, null=True)  # Field name made lowercase.
    paycheck_amount = models.FloatField(db_column='PayCheck_Amount', blank=True, null=True)  # Field name made lowercase.
    paycc_amount = models.FloatField(db_column='PayCC_Amount', blank=True, null=True)  # Field name made lowercase.
    paytrade_amount = models.FloatField(db_column='PayTrade_Amount', blank=True, null=True)  # Field name made lowercase.
    paycredit_amount = models.FloatField(db_column='PayCredit_Amount', blank=True, null=True)  # Field name made lowercase.
    payother_amount = models.FloatField(db_column='PayOther_Amount', blank=True, null=True)  # Field name made lowercase.
    collected = models.DecimalField(db_column='Collected', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=65, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pma_checks = models.FloatField(db_column='PMA_Checks', blank=True, null=True)  # Field name made lowercase.
    split_with_amount = models.FloatField(db_column='SPLIT_WITH_Amount', blank=True, null=True)  # Field name made lowercase.
    split_from_amount = models.FloatField(db_column='SPLIT_FROM_Amount', blank=True, null=True)  # Field name made lowercase.
    pma_years = models.IntegerField(db_column='PMA_Years', blank=True, null=True)  # Field name made lowercase.
    pma_quan = models.FloatField(db_column='PMA_Quan', blank=True, null=True)  # Field name made lowercase.
    pma_amount = models.FloatField(db_column='PMA_Amount')  # Field name made lowercase.
    splitfrom = models.CharField(db_column='SplitFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splitwith = models.CharField(db_column='SplitWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymethod = models.CharField(db_column='PayMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    penduntil = models.DateField(db_column='PendUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ViewInvoicesUnits'


class ShowSplits(models.Model):
    invoice_with = models.CharField(db_column='Invoice_With', max_length=10, null=False)
    invoice_from = models.CharField(db_column='Invoice_From', max_length=10, null=True)
    collected_with = models.DecimalField(db_column='Collected_With', null=True, blank=True, max_digits=10, decimal_places = 2)
    collected_from = models.DecimalField(db_column='Collected_From', null=True, blank=True, max_digits=10, decimal_places = 2)
    matCost_with = models.FloatField(db_column='MatCost_With', null=True, blank=True)
    matCost_from = models.FloatField(db_column='MatCost_From', null=True, blank=True)
    employee_with = models.CharField(db_column='Employee_With', max_length=41, null=True, blank=True)
    employee_from = models.CharField(db_column='Employee_From', max_length=41, null=True, blank=True)

    class Meta:
       managed = False
       db_table= 'ShowSplits'


class Splits(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=10)
    matCost = models.FloatField(db_column='MatCost', null=True, blank=True)
    total_cost = models.FloatField(db_column='Total_Cost', null=True, blank=True)
    invDate = models.DateField(db_column='InvDate', null=True, blank=True)
    employee = models.CharField(db_column='Employee', max_length=41, null=True, blank=True)
    payCash_amount = models.FloatField(db_column='PayCash_Amount', null=True, blank=True)
    payCheck_amount = models.FloatField(db_column='PayCheck_Amount', null=True, blank=True)
    payCC_amount = models.FloatField(db_column='PayCC_Amount', null=True, blank=True)
    payCredit_amount = models.FloatField(db_column='PayCredit_Amount', null=True, blank=True)
    payOther_amount = models.FloatField(db_column='PayOther_Amount', null=True, blank=True)
    collected = models.DecimalField(db_column='Collected', null=True, blank=True, max_digits=10, decimal_places=2)
    fullName = models.CharField(db_column='Fullname', max_length=65, null=True, blank=True)
    price = models.DecimalField(db_column='Price', null=True, blank=True, max_digits=10, decimal_places=2)
    pma_checks = models.FloatField(db_column='PMA_Checks', null=True, blank=True)
    split_with_amount = models.FloatField(db_column='SPLIT_WITH_Amount', null=True, blank=True)
    split_from_amount = models.FloatField(db_column='SPLIT_FROM_Amount', null=True, blank=True)
    pma_years = models.IntegerField(db_column='PMA_Years', null=True, blank=True)
    pma_quan = models.FloatField(db_column='PMA_Quan', null=True, blank=True)
    pma_amount = models.FloatField(db_column='PMA_Amount', null=False)
    splitFrom = models.CharField(db_column='SplitFrom', max_length=50, null=True, blank=True)
    splitWith = models.CharField(db_column='SplitWith', max_length=50, null=True, blank=True)
    payMethod = models.CharField(db_column='PayMethod', max_length=50, null=True, blank=True)
    pendUntil = models.DateField(db_column='PendUntil', null=True, blank=True)

    class Meta:
       managed = False
       db_table='Splits'

class InstallersPayment(models.Model):
    installerInvoice = models.CharField(db_column='InstallerInvoice', max_length=10, null=False)
    tech = models.CharField(db_column='Tech', max_length=50, null=False)
    payInstaller = models.DecimalField(db_column='PayInstaller', null=True, blank=True, max_digits=10, decimal_places=2)
    helper = models.CharField(db_column='Helper', max_length=50, null=False)
    payHelper = models.DecimalField(db_column='PayHelper', null=True, blank=True, max_digits=10, decimal_places=2)
    item = models.CharField(db_column='Item', max_length=26, null=True)

    class Meta: 
       managed = True
       db_table = 'InstallersPayment'


class Installation(models.Model):
    invoice = models.CharField(db_column='Invoice', max_length=16)  # Field name made lowercase.
    quan = models.FloatField(db_column='Quan')  # Field name made lowercase.
    install_desc = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'Installation'


