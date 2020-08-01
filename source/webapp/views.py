from django.shortcuts import render,redirect
from webapp.models import Guest
from webapp.forms import GuestForm, BROWSER_DATETIME_FORMAT
from django.http import HttpResponseNotAllowed

def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Guest.objects.all()
    else:
        data = Guest.objects.filter(status='active')
    return render(request, 'index.html', context={
        'guests': data
    })

def guest_create_view(request):
    if request.method == "GET":
        return render(request, 'guest_create.html', context={
            'form': GuestForm()
        })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            Guest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('index')
        else:
            return render(request, 'guest_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])