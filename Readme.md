# Cat Cafe Delivery Service 🐾

Сервис для заказа еды с доставкой котиками. Пользователи могут выбирать блюда из меню, назначать кота-курьера и оформлять заказы.

## 🚀 Основные функции
- Просмотр меню с категориями блюд
- Добавление товаров в заказ
- Выбор котика-курьера
- Оформление заказа с выбором способа оплаты
- Авторизация через Telegram-логин

## 🛠 Структура проекта

### Модели данных
```plaintext
- Category (Категории блюд)
- MenuItem (Позиции меню)
- Client (Клиенты)
- Order (Заказы)
- OrderItem (Позиции заказа)
- Payment (Оплата)
- Cat (Котики-курьеры)
```
#### Связи
```plaintext
Order 1:M OrderItem
Order 1:1 Payment
Order M:1 Client
Cat M:M MenuItem (любимые блюда)
```

## 🛠 Установка и запуск

1. Клонируйте репозиторий
```
git clone [ваш-репозиторий]
cd cat_cafe
```

2. Установите зависимости
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Настройте базу данных
```
python manage.py migrate
python manage.py createsuper user
```

4. Заполните тестовыми данными
```
python manage.py fill_db
```

5. Запустите сервер
```
python manage.py runserver
```

## 🌐 Использование
```plaintext
Перейдите по адресу: http://localhost:8000/login/
Введите Telegram-логин (тестовый: @testuser)
Выбирайте блюда в меню
Оформите заказ на странице оплаты
```

### 🐱 Особенности реализации
```plaintext
Сессионное хранение корзины
Middleware для контроля доступа
Валидация форм при оформлении
Система уведомлений Django Messages
```

### 🔮 Планы по развитию
```plaintext
Интеграция с Telegram API
Система рейтинга котов
Онлайн-оплата через платежные системы
История заказов для пользователей
```

## 📄 Лицензия
MIT License.