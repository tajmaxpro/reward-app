from .views import WalletCreateAPIView, WalletDetailAPIView
from django.urls import path, include


urlpatterns = [
    path('wallet/create/', WalletCreateAPIView.as_view(), name='wallet-create'),
    path('wallet/<int:pk>/', WalletDetailAPIView.as_view(), name='wallet-detail'),

]
