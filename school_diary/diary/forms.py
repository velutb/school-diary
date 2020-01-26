from django import forms


class StudentRegistration(forms.Form):
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

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
    litera = forms.ChoiceField(label="Литера:", choices=[
        ("А", "А"),
        ("Б", "Б"),
        ("В", "В"),
        ("Г", "Г"),
        ("Д", "Д"),
        ("Е", "Е"),
        ("Ж", "Ж"),
        ("З", "З")])
