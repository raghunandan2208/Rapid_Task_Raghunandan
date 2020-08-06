from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView,FormView,DeleteView,DetailView,ListView
from django.contrib.auth.decorators import login_required
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
from consultant.forms import (  SignUpForm,
                                PersonalDetailsForm,
                                OfficialDetailsForm,
                                ProjectDetailsForm,
                                TrainingDetailsForm,
                                FinancialDetailsForm,
                                InvoicingDetailsForm,
                                BenchDetailsForm,
                                ProspectDetailsForm,
                                )


class UserCreateView(CreateView):
    template_name = "connect/signup.html"
    form_class = SignUpForm
    success_url = "/consultant/login/"


class PersonalDetailsView(CreateView):
    model = PersonalDetails
    form_class = PersonalDetailsForm
    template_name = "consultant/personal-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class PersonalDetailsUpdateView(UpdateView):
    model = PersonalDetails
    form_class = PersonalDetailsForm
    template_name = "consultant/personal-details.html"
    success_url = '/consultant'


class OfficialDetailsView(CreateView):
    model = OfficialDetails
    form_class = OfficialDetailsForm
    template_name = "consultant/official-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class OfficialDetailsUpdateView(UpdateView):
    model = OfficialDetails
    form_class = OfficialDetailsForm
    template_name = "consultant/official-details.html"
    success_url = '/consultant'


class ProjectDetailsView(CreateView):
    model = ProjectDetails
    form_class = ProjectDetailsForm
    template_name = "consultant/project-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ProjectDetailsUpdateView(UpdateView):
    model = ProjectDetails
    form_class = ProjectDetailsForm
    template_name = "consultant/project-details.html"
    success_url = '/consultant'


class TrainingDetailsView(CreateView):
    model = TrainingDetails
    form_class = TrainingDetailsForm
    template_name = "consultant/training-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class TrainingDetailsUpdateView(UpdateView):
    model = TrainingDetails
    form_class = TrainingDetailsForm
    template_name = "consultant/training-details.html"
    success_url = '/consultant'


class FinancialDetailsView(CreateView):
    model = FinancialDetails
    form_class = FinancialDetailsForm
    template_name = "consultant/finance-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class FinancialDetailsUpdateView(UpdateView):
    model = FinancialDetails
    form_class = FinancialDetailsForm
    template_name = "consultant/finance-details.html"
    success_url = '/consultant'


class InvoicingDetailsView(CreateView):
    model = InvoicingDetails
    form_class = InvoicingDetailsForm
    template_name = "consultant/invoicing-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class InvoicingDetailsUpdateView(UpdateView):
    model = InvoicingDetails
    form_class = InvoicingDetailsForm
    template_name = "consultant/invoicing-details.html"
    success_url = '/consultant'


class BenchDetailsView(CreateView):
    model = BenchDetails
    form_class = BenchDetailsForm
    template_name = "consultant/bench-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class BenchDetailsUpdateView(UpdateView):
    model = BenchDetails
    form_class = BenchDetailsForm
    template_name = "consultant/bench-details.html"
    success_url = '/consultant'


class ProspectDetailsView(CreateView):
    model = ProjectDetails
    form_class = ProspectDetailsForm
    template_name = "consultant/prospect-details.html"
    success_url = '/consultant'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        employee = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'employee': employee}})
        return kwargs

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ProspectDetailsUpdateView(UpdateView):
    model = ProspectDetails
    form_class = ProspectDetailsForm
    template_name = "consultant/prospect-details.html"
    success_url = '/consultant'


@login_required(login_url='login')
def employee_details(request, *args, **kwargs):

    try:
        emp_personal = PersonalDetails.objects.get(employee_id=request.user.id)
    except:
        emp_personal=None
    try:
        emp_official = OfficialDetails.objects.get(employee_id=request.user.id)
    except:
        emp_official=None
    try:
        emp_training = TrainingDetails.objects.get(employee_id=request.user.id)
    except:
        emp_training=None
    try:
        emp_project = ProjectDetails.objects.get(employee_id=request.user.id)
    except:
        emp_project=None
    try:
        emp_finance = FinancialDetails.objects.get(employee_id=request.user.id)
    except:
        emp_finance=None
    try:
        emp_invoice = InvoicingDetails.objects.get(employee_id=request.user.id)
    except:
        emp_invoice=None
    try:
        emp_bench = BenchDetails.objects.get(employee_id=request.user.id)
    except:
        emp_bench=None
    try:
        emp_prospect = ProspectDetails.objects.get(employee_id=request.user.id)
    except:
        emp_prospect=None

    context = {
        'emp_personal':emp_personal,
        'emp_official':emp_official,
        'emp_training':emp_training,
        'emp_project':emp_project,
        'emp_finance':emp_finance,
        'emp_invoice':emp_invoice,
        'emp_bench':emp_bench,
        'emp_prospect':emp_prospect,
    }
    return render(request, 'consultant/emp-details.html', context)
