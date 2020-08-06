from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,FormView,DeleteView,DetailView,ListView
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
# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def consultant_dashboard_view(request, *args, **kwargs):
    personal = PersonalDetails.objects.all()
    official = OfficialDetails.objects.all()

    context = {
        'personal': personal,
        'official': official,
    }
    return render(request, 'dashboard/dashboard.html', context)


def training_dashboard_view(request, *args, **kwargs):
    training = TrainingDetails.objects.all()

    context = {
        'training': training,
    }
    return render(request, 'dashboard/training.html', context)


def prospect_dashboard_view(request, *args, **kwargs):
    prospect = ProspectDetails.objects.all()

    context = {
        'prospect': prospect,
    }
    return render(request, 'dashboard/prospect.html', context)


def onproject_dashboard_view(request, *args, **kwargs):
    project = ProjectDetails.objects.all()

    context = {
        'project': project,
    }
    return render(request, 'dashboard/on-project.html', context)


def benchlist_dashboard_view(request, *args, **kwargs):
    bench = BenchDetails.objects.all()

    context = {
        'bench': bench,
    }
    return render(request, 'dashboard/bench-list.html', context)
