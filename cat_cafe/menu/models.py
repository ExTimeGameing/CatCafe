from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    telegram_id = models.CharField(max_length=50)

class Cat(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cats/')
    description = models.TextField()
    favorite_food = models.ManyToManyField(MenuItem)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('preparing', 'Готовится'),
        ('completed', 'Завершен'),
    ]
    client = models.ForeignKey(
        Client, 
        on_delete=models.SET_NULL,  # Заказ останется если клиент удален
        null=True,  # Разрешаем NULL значения
        blank=True  # Разрешаем пустое значение в формах
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    cat = models.ForeignKey(
        'Cat', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='Кот-курьер'
    )

    def get_total(self):
        return sum(
            item.menu_item.price * item.quantity 
            for item in self.orderitem_set.all()
        )    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('online', 'Online'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    is_paid = models.BooleanField(default=False)