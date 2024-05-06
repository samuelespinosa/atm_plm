
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeView, BillViewSet, ProcessList, CustomerSearchView, ProcessDetail

router = DefaultRouter()
router.register(r'bills', BillViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the views that don't require ViewSets manually.

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('processes/', ProcessList.as_view(), name='process-list'),
    path('process/<int:pk>/', ProcessDetail.as_view(), name='process-detail'),
    path('customer-search/', CustomerSearchView.as_view(), name='customer-search'),
    path(r'api/',include(router.urls))
]
