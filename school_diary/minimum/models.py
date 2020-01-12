from django.db import models


class Subject(models.Model):
    name = models.CharField(verbose_name='Навание предмета', max_length=128)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return str(self.name)


class Grade(models.Model):
    num = models.IntegerField(verbose_name='Номер')
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    first = models.FileField(upload_to='min/', blank=True, verbose_name='Первая четверть')
    second = models.FileField(upload_to='min/', blank=True, verbose_name='Вторая четверть')
    third = models.FileField(upload_to='min/', blank=True, verbose_name='Третья четверть')
    fourth = models.FileField(upload_to='min/', blank=True, verbose_name='Четвертая четверть')

    class Meta:
        ordering = ['subj', 'num']
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return str(self.subj) + ' ' + str(self.num)
# Create your models here.
