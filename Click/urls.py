from django.urls import path
from .views import ClickUzMerchantAPIView

urlpatterns = [
    path('click/', ClickUzMerchantAPIView.as_view()),
]