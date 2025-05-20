from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem, Cat, Client


class Command(BaseCommand):
    help = "Fill database with test data"

    def handle(self, *args, **options):
        # Очистка существующих данных
        Category.objects.all().delete()
        MenuItem.objects.all().delete()
        Cat.objects.all().delete()
        Client.objects.all().delete()

        test_client = Client.objects.create(
            name="Test User", phone="+79991112233", telegram_id="@testuser"
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Создан тестовый пользователь: {test_client.telegram_id}"
            )
        )

        # 1. Создаем категории
        coffee = Category.objects.create(
            name="Кофейные напитки", description="Ароматный кофе разных сортов"
        )
        desserts = Category.objects.create(
            name="Десерты", description="Сладкие угощения для наслаждения"
        )
        main = Category.objects.create(
            name="Основные блюда", description="Сытные блюда для голодных посетителей"
        )
        special = Category.objects.create(
            name="Специальные напитки", description="Уникальные авторские напитки"
        )

        # 2. Создаем все блюда
        # Кофейные напитки
        espresso = MenuItem.objects.create(
            name="Эспрессо",
            description="Крепкий черный кофе",
            price=150,
            category=coffee,
        )
        latte = MenuItem.objects.create(
            name="Латте",
            description="Кофе с молочной пенкой",
            price=200,
            category=coffee,
        )
        cappuccino = MenuItem.objects.create(
            name="Капучино",
            description="Кофе с воздушной молочной пеной",
            price=180,
            category=coffee,
        )
        raf = MenuItem.objects.create(
            name="Раф",
            description="Кофе со сливками и ванилью",
            price=220,
            category=coffee,
        )
        americano = MenuItem.objects.create(
            name="Американо",
            description="Черный кофе с водой",
            price=160,
            category=coffee,
        )

        # Десерты
        tiramisu = MenuItem.objects.create(
            name="Тирамису",
            description="Итальянский десерт с кофе",
            price=250,
            category=desserts,
        )
        cheesecake = MenuItem.objects.create(
            name="Чизкейк",
            description="Нежный творожный десерт",
            price=230,
            category=desserts,
        )
        croissant = MenuItem.objects.create(
            name="Круассан",
            description="Французская выпечка с шоколадом",
            price=120,
            category=desserts,
        )
        macaron = MenuItem.objects.create(
            name="Макарун",
            description="Воздушное печенье с начинкой",
            price=90,
            category=desserts,
        )
        honey_cake = MenuItem.objects.create(
            name="Медовик",
            description="Медовый торт со сметанным кремом",
            price=200,
            category=desserts,
        )

        # Основные блюда
        salmon_sandwich = MenuItem.objects.create(
            name="Сэндвич с лососем",
            description="Свежий лосось с авокадо",
            price=300,
            category=main,
        )
        cheese_soup = MenuItem.objects.create(
            name="Сырный суп",
            description="Ароматный суп с тремя видами сыра",
            price=280,
            category=main,
        )
        omelette = MenuItem.objects.create(
            name="Омлет с грибами",
            description="Воздушный омлет с шампиньонами",
            price=220,
            category=main,
        )
        caesar = MenuItem.objects.create(
            name="Салат Цезарь",
            description="Классический салат с курицей",
            price=240,
            category=main,
        )
        bruschetta = MenuItem.objects.create(
            name="Брускетты",
            description="Тосты с томатами и базиликом",
            price=180,
            category=main,
        )

        # Специальные напитки
        irish_coffee = MenuItem.objects.create(
            name="Кофе по-ирландски",
            description="Кофе с виски и сливками",
            price=350,
            category=special,
        )
        mulled_wine = MenuItem.objects.create(
            name="Глинтвейн",
            description="Ароматный горячий напиток",
            price=280,
            category=special,
        )
        matcha = MenuItem.objects.create(
            name="Матча латте",
            description="Японский зеленый чай с молоком",
            price=230,
            category=special,
        )
        hot_chocolate = MenuItem.objects.create(
            name="Горячий шоколад",
            description="Настоящий шоколадный напиток",
            price=200,
            category=special,
        )
        lemonade = MenuItem.objects.create(
            name="Лимонад мятный",
            description="Освежающий домашний лимонад",
            price=180,
            category=special,
        )

        # 3. Создаем всех котов
        barsik = Cat.objects.create(
            name="Барсик", description="Пушистый рыжий кот, любит спать на подоконнике"
        )
        barsik.favorite_food.set([espresso.id, tiramisu.id])

        murka = Cat.objects.create(
            name="Мурка", description="Игривая черно-белая кошка, обожает внимание"
        )
        murka.favorite_food.set([latte.id, cheesecake.id])

        snowball = Cat.objects.create(
            name="Снежок", description="Белоснежный перс с голубыми глазами"
        )
        snowball.favorite_food.set([cappuccino.id, croissant.id])

        ginger = Cat.objects.create(
            name="Рыжик", description="Оранжевый хулиган, всегда в движении"
        )
        ginger.favorite_food.set([raf.id, macaron.id])

        self.stdout.write(self.style.SUCCESS("✅ Все данные успешно добавлены!"))
