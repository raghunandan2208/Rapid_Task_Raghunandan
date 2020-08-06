from django.urls import path, include
from dashboard.views import (   consultant_dashboard_view,
                                training_dashboard_view,
                                prospect_dashboard_view,
                                benchlist_dashboard_view,
                                onproject_dashboard_view,
                                )

urlpatterns = [
    path('consultant-dashboard', consultant_dashboard_view, name='consultant-dashboard'),
    path('training-dashboard', training_dashboard_view, name='training-dashboard'),
    path('prospect-dashboard', prospect_dashboard_view, name='prospect-dashboard'),
    path('bench-list-dashboard', benchlist_dashboard_view, name='bench-list-dashboard'),
    path('on-project-dashboard', onproject_dashboard_view, name='on-project-dashboard'),
]
