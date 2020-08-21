from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from .models import Payment


def index(request):
    return render(request, 'tracker/index.html',
                  {'payments': Payment.objects.all()})


@login_required(redirect_field_name=reverse_lazy('login'))
def submit(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            new_payment: Payment = form.save(commit=False)
            new_payment.user = request.user
            new_payment.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = PaymentForm()
    return render(request, 'tracker/submit.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
