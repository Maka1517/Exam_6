from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guest
from webapp.forms import GuestForm, BROWSER_DATETIME_FORMAT
from django.utils.timezone import make_naive
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


def guest_update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        form = GuestForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
            'status': guest.status,
            # форматирование перед выводом для DateTime.
            'created_at': make_naive(guest.created_at) \
                .strftime(BROWSER_DATETIME_FORMAT)
            # для дат выглядит просто как:
            # 'publish_at': article.publish_at
        })
        return render(request, 'guest_update.html', context={
            'form': form,
            'guest': guest
        })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            # Article.objects.filter(pk=pk).update(**form.cleaned_data)
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.status = form.cleaned_data['status']
            guest.publish_at = form.cleaned_data['created_at']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'guest_update.html', context={
                'guest': guest,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])




def guest_delete_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])