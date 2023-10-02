from django.db import models


SVG_ICONS = (
    ('M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm0 96c48.6 0 88 39.4 88 88s-39.4 88-88 88-88-39.4-88-88 39.4-88 88-88zm0 344c-58.7 0-111.3-26.6-146.5-68.2 18.8-35.4 55.6-59.8 98.5-59.8 2.4 0 4.8.4 7.1 1.1 13 4.2 26.6 6.9 40.9 6.9 14.3 0 28-2.7 40.9-6.9 2.3-.7 4.7-1.1 7.1-1.1 42.9 0 79.7 24.4 98.5 59.8C359.3 421.4 306.7 448 248 448z', 'Человек'),
    ('M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm144 276c0 6.6-5.4 12-12 12h-92v92c0 6.6-5.4 12-12 12h-56c-6.6 0-12-5.4-12-12v-92h-92c-6.6 0-12-5.4-12-12v-56c0-6.6 5.4-12 12-12h92v-92c0-6.6 5.4-12 12-12h56c6.6 0 12 5.4 12 12v92h92c6.6 0 12 5.4 12 12v56z', 'Аптечка'),
    ('M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z', 'Галочка'),
)

class Front(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    avatar = models.ImageField(upload_to='avatar/', verbose_name='Иконка вашего лички')
    link = models.CharField(max_length=500, verbose_name='Ссылка вашего лички')
    menu = models.CharField(max_length=500, verbose_name='Ссылка для меню')
    subtitle = models.CharField(max_length=100, verbose_name='Текст в белом цвете')
    title = models.CharField(max_length=50, verbose_name='Название')
    name = models.CharField(max_length=50, verbose_name='Текст в красном')
    white_name_button = models.CharField(max_length=50, verbose_name='Белая кнопка')
    white_link_button = models.CharField(max_length=500, verbose_name='Ссылка белой кнопки')
    black_name_button = models.CharField(max_length=50, verbose_name='Черная кнопка')
    black_link_button = models.CharField(max_length=500, verbose_name='Ссылка черной кнопки')

    class Meta:
        verbose_name = "Передний план"
        verbose_name_plural = "Передний план"

    def __str__(self):
        return self.title

class Datasets(models.Model):
    image = models.CharField(max_length=1000, choices=SVG_ICONS, verbose_name='Изображение')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(max_length=300, verbose_name='Содержание')
    link = models.CharField(max_length=500, verbose_name='Ссылка')

    class Meta:
        verbose_name = "Наборы данных"
        verbose_name_plural = "Наборы данных"

    def __str__(self):
        return self.title

class Statistics(models.Model):
    numbers = models.IntegerField(verbose_name='Число')
    title = models.CharField(max_length=100, verbose_name='Заголовок')

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"

    def __str__(self):
        return self.title

class Mentors(models.Model):
    img = models.ImageField(upload_to='portrait/', verbose_name='Изображение')
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    description = models.CharField(max_length=100, verbose_name='Описание')
    description_2 = models.CharField(max_length=100, verbose_name='Описание 2')
    link = models.CharField(max_length=500, verbose_name='Ссылка')

    class Meta:
        verbose_name = "Наставник"
        verbose_name_plural = "Наставники"

    def __str__(self):
        return self.full_name

class Courses(models.Model):
    course_type = models.CharField(max_length=60, null=True, blank=True, verbose_name='Тип курса')
    price = models.CharField(max_length=50, verbose_name='Цена')
    content = models.TextField(max_length=100, verbose_name='Содержание')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    fact_1 = models.CharField(max_length=50, verbose_name='Подзаголовок')
    fact_2 = models.CharField(max_length=50, verbose_name='Подзаголовок 2')
    fact_3 = models.CharField(max_length=50, verbose_name='Подзаголовок 3')
    fact_4 = models.CharField(max_length=50, verbose_name='Подзаголовок 4')
    fact_5 = models.CharField(max_length=50, verbose_name='Подзаголовок 5')
    link = models.CharField(max_length=500, verbose_name='Ссылка')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

class OffersBlack(models.Model):
    subtitle = models.CharField(max_length=50, verbose_name='Субтитры')
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(max_length=200, verbose_name='Содержание')

    class Meta:
        verbose_name = "Черные предложения"
        verbose_name_plural = "Черные предложении"

    def __str__(self):
        return self.title

class Offers(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    content = models.TextField(max_length=100, verbose_name='Содержание')
    link = models.CharField(max_length=500, verbose_name='Ссылка')

    class Meta:
        verbose_name = "Предложения"
        verbose_name_plural = "Предложении"

    def __str__(self):
        return self.title

class Gratitude(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name='Изображение')

    class Meta:
        verbose_name = "Благодарность"
        verbose_name_plural = "Благодарности"

    def __str__(self):
        return f"Изображение: {self.pk}"

class Speakers(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    offer_1 = models.TextField(max_length=100, verbose_name='Предложение')
    offer_2 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 2')
    offer_3 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 3')
    offer_4 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 4')
    offer_5 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 5')
    offer_6 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 6')
    offer_7 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 7')
    offer_8 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 8')
    offer_9 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 9')
    offer_10 = models.TextField(max_length=100, blank=True, null=True, verbose_name='Предложение 10')

    class Meta:
        verbose_name = "Динамик"
        verbose_name_plural = "Динамики"

    def __str__(self):
        return self.title

