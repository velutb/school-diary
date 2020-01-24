from django.db import models
from datetime import date


GRADES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11)
]


LITERAS = [
    ("А", "А"),
    ("Б", "Б"),
    ("В", "В"),
    ("Г", "Г"),
    ("Д", "Д"),
    ("Е", "Е"),
    ("Ж", "Ж"),
    ("З", "З")
]


WEIGHTS = [
    (5, "5 - отлично"),
    (4, "4 - хорошо"),
    (3, "3 - удовлетворительно"),
    (2, "2 - плохо"),
    (1, "1 - ужасно")
]


class Subjects(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ['name']
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class Teachers(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    second_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    subjects = models.ManyToManyField(Subjects, verbose_name="Предметы")
    login = models.CharField(max_length=50, verbose_name="Логин")
    password = models.CharField(max_length=50, verbose_name="Пароль")
    
    class Meta:
        ordering = ['surname', 'first_name', 'second_name']
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    
    def __str__(self):
        return self.surname + " " + self.first_name + " " + self.second_name


class Grades(models.Model):
    number = models.IntegerField(choices=GRADES, verbose_name="Класс")
    letter = models.CharField(max_length=2, verbose_name="Буква")
    main_teacher = models.ForeignKey(Teachers, null=True, on_delete=models.SET_NULL, verbose_name="Классный руководитель")

    class Meta:
        ordering = ['number', 'letter']
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return str(self.number) + self.letter


class Students(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    second_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    login = models.CharField(max_length=50, verbose_name="Логин")
    password = models.CharField(max_length=50, verbose_name="Пароль")
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE, verbose_name="Класс")

    class Meta:
        ordering = ['surname', 'first_name', 'second_name']
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return self.surname + " " + self.first_name + " " + self.second_name


class HomeTasks(models.Model):
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE, verbose_name="Класс")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.CharField(max_length=1000, verbose_name="Описание домашнего задания")
    creation_date = models.DateField(verbose_name="Когда задано", default=date.today)
    day_to_make = models.DateField(verbose_name="На какой день задано")

    class Meta:
        ordering = ['day_to_make']
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"

    def __str__(self):
        return "Д/з на " + str(self.date_to_make)


class Marks(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    creation_date = models.DateField(default=date.today, verbose_name="Дата")
    weight = models.IntegerField(choices=WEIGHTS, verbose_name="Вес оценки")
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Ученик")
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE, verbose_name="Класс")
    comment = models.CharField(max_length=150, verbose_name="Комментарий", blank=True)

    class Meta:
        ordering = ['creation_date']
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self):
        return "{}: оценка {} за {}".format(self.student, self.mark, self.creation_date)