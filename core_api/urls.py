from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core_api import views

urlpatterns = [
    path("process/", views.ProcessList.as_view()),
    path("process/<int:pk>/", views.ProcessDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
