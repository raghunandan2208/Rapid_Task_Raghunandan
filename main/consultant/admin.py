from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from consultant.models import ( User,
                                PersonalDetails,
                                OfficialDetails,
                                ProjectDetails,
                                TrainingDetails,
                                FinancialDetails,
                                InvoicingDetails,
                                BenchDetails,
                                ProspectDetails,
                                )



# Register your models here.

class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'personal_email', 'immigration_status']


class OfficialDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'employee_type', 'ssn', 'official_phone_number', 'technology', 'employee_status' ]


class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'client', 'client_city', 'vendor', 'job_title', 'start_date', 'end_date']


class TrainingDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'technology', 'training_status', 'trainer_rating', 'trainer_comments']


class FinancialDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'bill_rate', 'pay_rate', 'margin', 'recruiter_margin']


class InvoicingDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'invoicing_company', 'invoice_contact_name', 'invoice_contact_email', 'invoice_terms']


class BenchDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'title', 'visa', 'availability_date', 'bench_days']


class ProspectDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee', 'technology', 'prospect_type', 'availability_date', 'comments']



admin.site.register(User, UserAdmin)
admin.site.register(PersonalDetails, PersonalDetailsAdmin)
admin.site.register(OfficialDetails, OfficialDetailsAdmin)
admin.site.register(ProjectDetails, ProjectDetailsAdmin)
admin.site.register(TrainingDetails, TrainingDetailsAdmin)
admin.site.register(FinancialDetails, FinancialDetailsAdmin)
admin.site.register(InvoicingDetails, InvoicingDetailsAdmin)
admin.site.register(BenchDetails, BenchDetailsAdmin)
admin.site.register(ProspectDetails, ProspectDetailsAdmin)
