from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Worker(models.Model):
    SEX = [
        ('f', 'Женщина'),
        ('m', 'Мужчина'),
    ]
    EXP = [
        ('<5', 'Меньше 6 месяцев'),
        ('>5', 'От 6 месяцев до 1 года'),
        ('>1', 'От 1 года до 3'),
        ('>3', 'Больше 3х лет'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField('Должность', max_length=10)
    name = models.CharField('Имя', max_length=15)
    last_name = models.CharField('Отчество', max_length=15, blank=True)
    surname = models.CharField('Фамилия', max_length=20)
    telephone = models.CharField('Телефон', max_length=12, unique=True)
    sex = models.CharField('Пол', max_length=1, choices=SEX, default='m')
    age = models.IntegerField('Возраст', validators=[MinValueValidator(15), MaxValueValidator(70)])
    experience = models.CharField('Опыт', max_length=2, choices=EXP, default='<5')
    salary = models.IntegerField('Зарплата', default=0)

    def __str__(self):
        return f'{self.id}: {self.title}-{self.surname} {self.name}'
