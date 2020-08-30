from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:id>', views.payment_details, name='payment'),
    path('payments', views.all_payments, name='allpayments'),
    path('submit', views.submit, name='submit'),
    path('success', views.success, name='success'),
]
