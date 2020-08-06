from django.db import models
from phone_field import PhoneField
from localflavor.us.models import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

M_STATUS = [
    ("Single", "Single"),
    ("Married", "Married"),
    ("Divorces", "Divorces"),
    ("Other", "Other")
]

IMMIGRATION_STATUS_CHOICES = [
    ('Opt','Opt'),
    ('CPT','CPT'),
    ('H1B','H1B'),
    ('H4Ead','H4Ead'),
    ('GC-EAD','GC -EAD'),
    ('Grean_Card','Green Card'),
    ('Citizen','Citizen'),
    ('TN','TN'),
    ('Other','Other'),
]

BOOL_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
]

INDUSTRY_CHOICES = [
    ('Banking&Finance','Banking & Finance'),
    ('Insurance','Insurance'),
    ('Government','Government'),
    ('Healthcare','Healthcare'),
    ('Manufacturing','Manufacturing'),
    ('Automobile','Automobile'),
    ('Entertainment','Entertainment'),
    ('Other','Other'),
]

EMPLOYEE_TYPE_CHOICES = [
    ('W-2_Full_Time_Employee','W-2 Full Time Employee'),
    ('1099-Independent_Contractor','1099- Independent Contractor'),
    ('Intern','Intern'),
    ('Subcontractor','Subcontractor'),
    ('Temp_Employee','Temp Employee'),
    ('Vacation','Vacation')
]

SENIORITY_LEVEL_CHOICES = [
    ('Associate','Associate'),
    ('Consultant','Consultant'),
    ('Senior_Consultant','Senior Consultant'),
    ('Manager','Manager'),
    ('Senior_Manager','Senior Manager'),
]

EMPLOYEE_STATUS_CHOICES = [
    ('On-Project','On-Project'),
    ('T&P','T&P'),
    ('Prospect','Prospect'),
    ('Bench','Bench'),
    ('Terminated','Terminated'),
]


class User(AbstractUser):
    email               =   models.EmailField(unique=True)

    REQUIRED_FIELDS     = ['email']


class PersonalDetails(models.Model):

    employee            =   models.ForeignKey(User,on_delete=models.CASCADE)
    first_name          =   models.CharField(max_length=50, blank=True, null=True)
    middle_name         =   models.CharField(max_length=50, blank=True, null=True)
    last_name           =   models.CharField(max_length=50)
    gender              =   models.CharField(max_length=10, choices=GENDER)
    date_of_birth       =   models.DateField()
    marital_status      =   models.CharField(max_length=10, choices=M_STATUS)
    anniversary_date    =   models.DateField()
    personal_email      =   models.EmailField()
    marketing_email     =   models.EmailField()
    address_line_1      =   models.CharField(max_length=250)
    address_line_2      =   models.CharField(max_length=250, blank=True, null=True)
    city                =   models.CharField(max_length=50)
    state               =   USStateField()
    zip_code            =   USZipCodeField()
    country             =   models.CharField(max_length=20, default='USA')
    immigration_status  =   models.CharField(max_length=20, choices=IMMIGRATION_STATUS_CHOICES)
    i_status            =   models.BooleanField(choices=BOOL_CHOICES, verbose_name="I-140 Status", blank=True, null=True)
    gc_priority_date    =   models.DateField(blank=True, null=True)
    industry            =   models.CharField(max_length=20, choices=INDUSTRY_CHOICES, blank=True, null=True)


    def __str__(self):
        return self.employee.username


class OfficialDetails(models.Model):

    employee                =   models.ForeignKey(User,on_delete=models.CASCADE)
    employee_num            =   models.CharField(max_length=15)
    official_email_id       =   models.EmailField(blank=True, null=True)
    official_phone_number   =   PhoneField(blank=True, null=True)
    employee_type           =   models.CharField(max_length=50, choices=EMPLOYEE_TYPE_CHOICES)
    date_of_joining         =   models.DateField()
    ssn                     =   USSocialSecurityNumberField(verbose_name="SSN")
    technology              =   models.CharField(max_length=50)
    job_title               =   models.CharField(max_length=50)
    seniority_level         =   models.CharField(max_length=50, choices=SENIORITY_LEVEL_CHOICES)
    employee_status         =   models.CharField(max_length=50, choices=EMPLOYEE_STATUS_CHOICES)
    date_of_termination     =   models.DateField(blank=True, null=True)
    description             =   models.TextField()

    def __str__(self):
        return self.employee.username


class ProjectDetails(models.Model):

    employee                =   models.ForeignKey(User,on_delete=models.CASCADE)
    client                  =   models.CharField(max_length=250, blank=True, null=True)
    vendor                  =   models.CharField(max_length=250, blank=True, null=True)
    vendor_contact          =   models.CharField(max_length=250, blank=True, null=True)
    phone                   =   PhoneField(blank=True, null=True)
    email                   =   models.EmailField(max_length=250, blank=True, null=True)
    start_date              =   models.DateField(max_length=250, blank=True, null=True)
    end_date                =   models.DateField(max_length=250, blank=True, null=True)
    client_address          =   models.CharField(max_length=250, blank=True, null=True)
    client_city             =   models.CharField(max_length=250, verbose_name="Client City, State", blank=True, null=True)
    technology              =   models.CharField(max_length=250, blank=True, null=True)
    job_title               =   models.CharField(max_length=250, blank=True, null=True)
    rate                    =   models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.employee.username


class TrainingDetails(models.Model):

    employee                =    models.ForeignKey(User,on_delete=models.CASCADE)
    technology              =    models.CharField(max_length=250, blank=True, null=True)
    training_status         =    models.CharField(max_length=250, blank=True, null=True)
    start_date              =    models.DateField(max_length=250, blank=True, null=True)
    end_date                =    models.DateField(max_length=250, blank=True, null=True)
    availability_date       =    models.DateField(blank=True, null=True)
    lead_source             =    models.CharField(max_length=250, blank=True, null=True)
    trainer_comments        =    models.CharField(max_length=250, blank=True, null=True)
    trainer_rating          =    models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.employee.username


class FinancialDetails(models.Model):

    employee                =    models.ForeignKey(User,on_delete=models.CASCADE)
    bill_rate               =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name="Bill Rate /hr")
    monthly_bill_rate       =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    annual_bill_rate        =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pay_rate                =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name="Pay Rate /hr")
    monthly_pay_rate        =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    annual_pay_rate         =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    perDm                   =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    federal_tax             =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    state_tax               =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    extra_expense           =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    immigration_cost        =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    insurance               =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    four_o_one_k            =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name="401 K")
    total_expense           =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    margin                  =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    recruiter_margin        =    models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.employee.username


class InvoicingDetails(models.Model):

    employee                =    models.ForeignKey(User,on_delete=models.CASCADE)
    invoice_terms           =    models.CharField(max_length=250)
    invoice_contact_name    =    models.CharField(max_length=250)
    invoice_contact_email   =    models.CharField(max_length=250)
    invoice_contact_address =    models.CharField(max_length=250)
    invoicing_company       =    models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.employee.username


class BenchDetails(models.Model):

    employee                =    models.ForeignKey(User,on_delete=models.CASCADE)
    title                   =    models.CharField(max_length=250, blank=True, null=True)
    visa                    =    models.CharField(max_length=250, blank=True, null=True)
    availability_date       =    models.DateField(blank=True, null=True)
    bench_days              =    models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.employee.username

class ProspectDetails(models.Model):

    employee                =    models.ForeignKey(User,on_delete=models.CASCADE)
    technology              =    models.CharField(max_length=250, blank=True, null=True)
    prospect_type           =    models.CharField(max_length=250, blank=True, null=True)
    comments                =    models.CharField(max_length=250, blank=True, null=True)
    availability_date       =    models.DateField(blank=True, null=True)

    def __str__(self):
        return self.employee.username
