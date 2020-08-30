from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm, LogForm
from .models import Payment


def all_payments(request):
    return render(request, 'tracker/all_payments.html',
                  {'payments': Payment.objects.all()})


def payment_details(request, id: int):
    try:
        payment = Payment.objects.get(id=id)
    except Payment.DoesNotExist:
        raise Http404("Payment with that ID does not exist")
    return render(request, 'tracker/payment.html',
                  {'payment': payment})


@login_required(redirect_field_name=reverse_lazy('login'))
def submit_payment(request):
    if request.method == 'POST':

        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            new_payment: Payment = form.save(commit=False)
            new_payment.user = request.user
            new_payment.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = PaymentForm()
    return render(request, 'tracker/submit_payment.html', {'form': form})


@login_required(redirect_field_name=reverse_lazy('login'))
def submit_log(request):
    if request.method == 'POST':

        form = LogForm(request.POST, request.FILES)

        if form.is_valid():
            new_log: Payment = form.save(commit=False)
            new_log.logger = request.user
            new_log.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = LogForm()
    return render(request, 'tracker/submit_log.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
