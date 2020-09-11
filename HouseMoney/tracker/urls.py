from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/<int:id>', views.payment_details, name='payment'),
    path('payments', views.all_payments, name='allpayments'),
    path('submit/payment', views.submit_payment, name='submitpayment'),
    path('submit/log', views.submit_log, name='submitlog'),
    path('success', views.success, name='success'),
    path('logs', views.all_logs, name='logs')
]
