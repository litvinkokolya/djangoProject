from django import forms

class UserForm(forms.Form):
    fio = forms.CharField(label = "ФИО", help_text="Ну вводи ФИО)", max_length=70)
    age = forms.IntegerField(label = "Возраст", help_text="Сколько годиков тебе?", max_value=100)
    mail = forms.EmailField(label = "Емейл", help_text="собачку нужно вводить!", #error_messages="Господи да введи ты собачку просто!!!",
                            required=False)
    image = forms.ImageField(label = "Можете загрузить картиночку", help_text="Только без гадостей)")
    spisok = forms.ChoiceField(label="Выберите курс на котором учитесь",
                               choices=((1, 1),
                                       (2, 2),
                                       (3, 3),
                                       (4, 4)))
    dateAndTime = forms.SplitDateTimeField(label="Введите дату и время поступления")
    yesOrNo = forms.NullBooleanField(label="Вы робот?")
