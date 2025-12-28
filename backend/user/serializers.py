from datetime import date, datetime
from rest_framework import serializers
from .models import User, UserProfile, UserHousing, UserPhoto
import re


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "country", "city",
            "gender", "birthdate", "phone_number", "email",
            "password", "repeat_password",
        ]

    def validate_first_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError(
                "Має містити більше ніж 2 символи")

        if len(value) >= 50:
            raise serializers.ValidationError(
                "Має містити менше ніж 50 символів")

        if not value[0].isupper():
            raise serializers.ValidationError(
                "Перша літера має бути великою")

        if not re.match(UKRAINIAN_PATTERN, value):
            raise serializers.ValidationError("Тільки українські літери")

        return value

    def validate_last_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError(
                "Має містити більше ніж 2 символи")

        if len(value) >= 50:
            raise serializers.ValidationError(
                "Має містити менше ніж 50 символів")

        if not value[0].isupper():
            raise serializers.ValidationError(
                "Перша літера має бути великою")

        if not re.match(UKRAINIAN_PATTERN, value):
            raise serializers.ValidationError("Тільки українські літери")

        return value

    def validate_country(self, value):
        if value not in COUNTRY_CHOICES.values():
            raise serializers.ValidationError(
                "Має бути обрано дійсний варіант зі списку")

        return value

    def validate_city(self, value):
        if value not in CITY_CHOICES.values():
            raise serializers.ValidationError(
                "Має бути обрано дійсний варіант зі списку")

        return value

    def validate_gender(self, value):
        if value not in VALID_GENDERS.values():
            raise serializers.ValidationError(
                "Має бути обрано дійсний варіант зі списку")

        return value

    def validate_birthdate(self, value):
        # З фронта надсилається такий формат дати: 2006-10-19T21:00:00.000Z
        # Переформатування у запис: рік-місяць-день
        value = datetime.fromisoformat(value)
        value = value.date()

        min_date = date(1950, 1, 1)
        max_date = date.today()

        if min_date > value or max_date < value:
            raise serializers.ValidationError("Некоректна дата")

        return value

    def validate_phone_number(self, value):
        # З фронта надсилається такий формат: +38(0XX)-XXX-XX-XX
        # 380XXXXXXXXX - чиститься все, що не цифра
        value = re.sub(r'\D', '', value)

        if len(value) != 12:
            raise serializers.ValidationError(
                "Має містити 12 цифр"
            )

        phone_code = value[2:5]
        if phone_code not in VALID_UA_PHONE_CODES:
            raise serializers.ValidationError(
                "Невірний код мобільного оператора України")
        # Запис в БД у нормалізованому вигляді: +380XXXXXXXXX
        return f"+{value}"

    def validate_email(self, value):
        if len(value) >= 50:
            raise serializers.ValidationError(
                "Має містити не більше ніж 50 символів")

        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        repeat_password = validated_data.pop("repeat_password")
        user = User.create_user_with_password(
            validated_data, password, repeat_password)
        user.save()
        return user


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ['image']


class UserProfileSerializer(serializers.ModelSerializer):

    photos = UserPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHousing
        fields = '__all__'


UKRAINIAN_PATTERN = r"^[А-ЩЬЮЯҐЄІЇ][а-щьюяґєії'\-]*$"

VALID_UA_PHONE_CODES = [
    # Київстар
    '067', '068', '096', '097', '098',
    # Vodafone
    '050', '066', '095', '099',
    # lifecell
    '063', '073', '093',
    # Інтертелеком
    '089', '094',
    # ТриМоб
    '091',
    # People.net
    '092',
    # Фінтелеком
    '039'
]

COUNTRY_CHOICES = {
    "ua": "Україна"
}

CITY_CHOICES = {
    "kyiv": "Київ",
    "lviv": "Львів",
    "odessa": "Одеса",
    "kharkiv": "Харків",
    "dnipro": "Дніпро",
    "zaporizhzhia": "Запоріжжя",
    "vinnytsia": "Вінниця",
    "cherkasy": "Черкаси",
    "ivano_frankivsk": "Івано-Франківськ",
    "ternopil": "Тернопіль",
    "rivne": "Рівне",
    "zhytomyr": "Житомир",
    "sumy": "Суми",
    "poltava": "Полтава",
    "chernihiv": "Чернігів",
    "kropyvnytskyi": "Кропивницький",
    "lutsk": "Луцьк",
    "khmelnytskyi": "Хмельницький",
    "mykolaiv": "Миколаїв",
    "chernivtsi": "Чернівці",
    "uzhhorod": "Ужгород",
    "berehove": "Берегове",
    "kamianets_podilskyi": "Кам'янець-Подільський",
    "kamianske": "Кам'янське",
    "bila_tserkva": "Біла Церква",
    "brovary": "Бровари",
    "kherson": "Херсон",
    "mukachevo": "Мукачево",
    "kremenchuk": "Кременчук",
    "konotop": "Конотоп",
    "uman": "Умань",
    "krivyi_rih": "Кривий Ріг"
}

VALID_GENDERS = {
    "male": "Чоловік",
    "female": "Жінка",
    "other": "Інше"
}
