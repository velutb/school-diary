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


WEIGHTS = [
    (5, "5 - отлично"),
    (4, "4 - хорошо"),
    (3, "3 - удовлетворительно"),
    (2, "2 - плохо"),
    (1, "1 - ужасно")
]


class Subjects(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class Teachers(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subjects)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['surname', 'first_name', 'second_name']
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    
    def __str__(self):
        return self.surname + " " + self.first_name + " " + self.second_name


class Grades(models.Model):
    number = models.IntegerField(choices=GRADES)
    letter = models.CharField(max_length=2)
    main_teacher = models.ForeignKey(Teachers, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['number', 'letter']
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return str(self.number) + self.letter


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE)

    class Meta:
        ordering = ['surname', 'first_name', 'second_name']
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return self.surname + " " + self.first_name + " " + self.second_name


class HomeTasks(models.Model):
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
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