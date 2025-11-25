from django.db import models
from django.db.models import JSONField

GENDER_CHOICES = [
    ('Чоловік', 'Чоловік'),
    ('Жінка', 'Жінка'),
    ('Інше', 'Інше'),
]

CLEANLINESS_CHOICES = [
    (1, '1 (Дуже неохайно)'),
    (2, '2'),
    (3, '3 (Середньо)'),
    (4, '4'),
    (5, '5 (Дуже охайно)'),
]

ROOM_SHARING_CHOICES = [
    ('Mені комфортно ділити кімнату з співмешканцем', 'Mені комфортно ділити кімнату з співмешканцем'),
    ('Я хочу мати окрему кімнату', 'Я хочу мати окрему кімнату'),
]

PREFERRED_GENDER_CHOICES = [
    ('Лише з хлопцями', 'Лише з хлопцями'),
    ('Лише з дівчатами', 'Лише з дівчатами'),
    ('Не має значення', 'Не має значення'),
]

HOUSING_STATUS_CHOICES = [
    ('Я шукаю квартиру та співмешканця', 'Я шукаю квартиру та співмешканця'),
    ('Я шукаю лише співмешканця, маю свою/орендовану квартиру', 'Я шукаю лише співмешканця, маю свою/орендовану квартиру'),
]


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    country = models.CharField(max_length=50, verbose_name="Країна")
    city = models.CharField(max_length=50, verbose_name="Місто")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Стать")
    birthdate = models.DateField(verbose_name="Дата народження")
    phone_number = models.CharField(max_length=13, unique=True, verbose_name="Номер телефону")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email")
# ПАРОЛЬ, ПОВТОР ПАРОЛЮ, ХЕШУВАННЯ ПАРОЛЮ
    password_hash = models.CharField(max_length=255, verbose_name="Хеш пароля")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        managed = False
        db_table = 'flat_buddy"."user'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="Користувач"
    )
    
    profile_photo_url = models.TextField(verbose_name="Фото профілю")
    university = models.CharField(max_length=100, verbose_name="Заклад освіти")
    specialization = models.CharField(max_length=50, verbose_name="Спеціалізація")
    study_year = models.CharField(max_length=50, verbose_name="Курс")
    languages = models.JSONField(verbose_name="Допустимі мови спілкування")
    political_view = models.CharField(max_length=100, verbose_name="Політичні погляди")
    cleanliness = models.IntegerField(choices=CLEANLINESS_CHOICES, verbose_name="Охайність (1-5)")
    lifestyle = models.TextField(verbose_name="Опишіть свій стиль життя")
    schedule = models.TextField(verbose_name="Розклад")
    sleep_schedule = models.TextField(verbose_name="Графік сну")
    bad_habits = models.TextField(verbose_name="Шкідливі звички")
    mbti = models.JSONField(verbose_name="MBTI")
    extra_intro_version = models.CharField(max_length=50, verbose_name="Екстравертність/інтровертність")
    hobbies = models.TextField(verbose_name="Розкажіть про ваші захоплення/хобі")
    bio = models.TextField(verbose_name="Біо")
    looking_for = models.TextField(verbose_name="Кого шукаєте")

    class Meta:
        managed = False
        db_table = 'flat_buddy"."user_profile'
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'
        
    def __str__(self):
        return f"Профіль {self.user.email}"


class UserHousing(models.Model):
    housing_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='housing',
        verbose_name="Користувач"
    )
    room_sharing_preference = models.CharField(
        max_length=100,
        choices=ROOM_SHARING_CHOICES,
        verbose_name="Чому надаєте перевагу?"
    )
    preferred_gender = models.CharField(
        max_length=30,
        choices=PREFERRED_GENDER_CHOICES,
        verbose_name="Із ким ви б хотіли проживати?"
    )
    housing_status = models.CharField(
        max_length=100,
        choices=HOUSING_STATUS_CHOICES,
        verbose_name="Що найкраще описує вашу ситуацію?"
    )
    budget = models.IntegerField(verbose_name="Який ваш бюджет?")
    preferred_districts = models.JSONField(verbose_name="Оберіть бажаний район/райони проживання")
    planned_duration = models.CharField(max_length=50, verbose_name="Як довго ви плануєте проживати у орендованій квартирі?")
    move_in_date = models.CharField(max_length=100, verbose_name="Коли б ви хотіли заїхати у квартиру?")
    has_pet = models.BooleanField(verbose_name="Чи є у вас домашній улюбленець?")
    pet_description = models.TextField(blank=True, null=True, verbose_name="Розкажіть про своїх домашніх улюбленців")

    class Meta:
        managed = False
        db_table = 'flat_buddy"."user_housing'
        verbose_name = 'Житлові уподобання'
        verbose_name_plural = 'Житлові уподобання'

    def __str__(self):
        return f"Житлові уподобання {self.user.email}"