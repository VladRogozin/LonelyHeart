from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateForm
from .models import Cat, Blog, Cards, OurNumbers
from django.urls import reverse


def cat_view(request):
    sort_param = request.GET.get('sort')

    if sort_param == 'Cat':
        cats = Cat.objects.filter(what_kind_of_pet='Cat').order_by('name')
    elif sort_param == 'Dog':
        cats = Cat.objects.filter(what_kind_of_pet='Dog').order_by('name')
    elif sort_param == 'Yoang Cat':
        cats = Cat.objects.filter(what_kind_of_pet='Yoang Cat').order_by('name')
    elif sort_param == 'Kitten':
        cats = Cat.objects.filter(what_kind_of_pet='Kitten').order_by('name')
    else:
        cats = Cat.objects.all()

    return render(request, 'cat/cat.html', {'cats': cats})


def cat_base(request):
    our_numbers = OurNumbers.objects.first()
    return render(request, 'cat/base.html', {'our_numbers': our_numbers})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'cat/blogs.html', {'blogs': blogs})


def cat_helps(request):
    cards = Cards.objects.all()
    debt = OurNumbers.objects.first()

    return render(request, 'cat/cat_helps.html', {'cards': cards, 'debt': debt})



def search_cats(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')  # Получение значения из формы поиска
        if search_query:  # Проверка наличия значения
            cats = Cat.objects.filter(
                Q(name__icontains=search_query) |
                Q(features__icontains=search_query) |
                Q(color__icontains=search_query) |
                Q(age__icontains=search_query) |
                Q(gender__icontains=search_query) |
                Q(sterilization__icontains=search_query) |
                Q(vaccination__icontains=search_query)
            )
        else:
            cats = Cat.objects.none()  # Если нет значения поиска, возвращаем пустой QuerySet
        return render(request, 'cat/search_cats.html', {'cats': cats})


def customers_form(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'GET':
        form = CreateForm()
    elif request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cat:cat_view'))

    return render(request, 'cat/customersForm.html', {'form': form, 'cat': cat})