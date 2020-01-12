from django import forms


class GetMinimumForm(forms.Form):
    subject = forms.ChoiceField(label="Предмет:", choices=[
        (1, "Информатика"),
        (2, "История"),
        (3, "Литература"),
        (4, "Математика"),
        (5, "Обществознание"),
        (6, "Русский язык"),
        (7, "Хим-Био"),
        (8, "Экономика"),
        (9, "Физика")])
    grade = forms.ChoiceField(label="Класс:", choices=[
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
        (11, 11)])
    quater = forms.ChoiceField(label="Четверть:", choices=[
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV")])
