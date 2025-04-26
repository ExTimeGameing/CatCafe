from django.shortcuts import render
from .models import MenuItem, Category

def menu_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})