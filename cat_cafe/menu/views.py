from django.shortcuts import render, redirect
from .models import Category, MenuItem, Order, OrderItem, Client, Cat, Payment  # <-- Client должен быть импортирован
from .forms import LoginForm  # <-- правильный импорт
from django.contrib import messages

def checkout(request):
    # Проверка авторизации
    if 'user_id' not in request.session:
        return redirect('menu:login')

    try:
        # Получаем текущий заказ
        order = Order.objects.get(
            client_id=request.session['user_id'],
            status='pending'
        )
    except Order.DoesNotExist:
        return redirect('menu:menu')

    errors = {
        'error_cat': None,
        'error_payment': None,
        'error_order': None
    }

    # Обработка подтверждения заказа
    if request.method == 'POST':
        cat_id = request.POST.get('cat_id')
        payment_method = request.POST.get('payment_method')

        # Валидация
        if not order.orderitem_set.exists():
            errors['error_order'] = "Заказ не может быть пустым"
        if not cat_id:
            errors['error_cat'] = "Выберите котика-курьера"
        if not payment_method:
            errors['error_payment'] = "Выберите способ оплаты"

        if not any(errors.values()):
            # Создаем оплату
            Payment.objects.create(
                order=order,
                amount=order.get_total(),
                method=payment_method,
                is_paid=False  # Можно изменить после интеграции с платежной системой
            )

            # Обновляем статус заказа
            order.status = 'completed'
            order.save()

            # Очищаем сессию
            request.session.flush()

            messages.success(request, "✅ Заказ оформлен успешно!")
            return redirect('menu:login')  # Важно использовать redirect, а не render

    # Данные для формы
    context = {
        'order': order,
        'cats': Cat.objects.all(),
        'payment_methods': Payment.PAYMENT_METHODS,
        **errors
    }
    return render(request, 'menu/checkout.html', context)

def login_redirect(request):
    return redirect('menu:login')  # Используем пространство имен

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            telegram_id = form.cleaned_data['telegram_login']
            try:
                client = Client.objects.get(telegram_id=telegram_id)
                request.session['user_id'] = client.id
                return redirect('/menu/')  # Явный путь
            except Client.DoesNotExist:
                form.add_error('telegram_login', 'Пользователь не найден')
    else:
        form = LoginForm()
    return render(request, 'menu/login.html', {'form': form})

def menu_list(request):
    # Проверка авторизации
    if 'user_id' not in request.session:
        return redirect('menu:login')
    
    try:
        client = Client.objects.get(id=request.session['user_id'])
    except Client.DoesNotExist:
        request.session.flush()
        return redirect('menu:login')
    
    # Получаем или создаем заказ
    order, created = Order.objects.get_or_create(
        client=client,
        status='pending'
    )
    
    # Обработка добавления товара
    if request.method == 'POST' and 'add_to_order' in request.POST:
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        
        try:
            menu_item = MenuItem.objects.get(id=item_id)
            order_item, created = OrderItem.objects.get_or_create(
                order=order,
                menu_item=menu_item,
                defaults={'quantity': quantity}
            )
            if not created:
                order_item.quantity += quantity
                order_item.save()
        except MenuItem.DoesNotExist:
            pass
        
        return redirect('menu:menu')

    # Получаем категории с предзагрузкой товаров
    categories = Category.objects.prefetch_related('menuitem_set').all()
    
    return render(request, 'menu/menu.html', {
        'categories': categories,
        'current_order': order
    })

def logout_view(request):
    request.session.flush()
    return redirect('login')