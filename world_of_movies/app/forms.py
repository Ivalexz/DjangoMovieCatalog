from django import  forms

class AddMovieForm(forms.Form):
    cover= forms.URLField(
        label="Обкладинка",
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    title=forms.CharField(
        label="Назва",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    director = forms.CharField(
        label="Режисер",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year=forms.IntegerField(
        label="Рік",
        min_value=1896,
        max_value=2025,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    genre=forms.CharField(
        label="Жанр",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rating=forms.FloatField(
        label="Рейтинг",
        min_value=1,
        max_value=5,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class UpdateMovieForm(forms.Form):
    cover = forms.URLField(
        label="Обкладинка",
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        label="Назва",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    director = forms.CharField(
        label="Режисер",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        label="Рік",
        required=False,
        min_value=1896,
        max_value=2025,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    genre = forms.CharField(
        label="Жанр",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rating = forms.FloatField(
        label="Рейтинг",
        required=False,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class SearchMovieForm(forms.Form):
    title = forms.CharField(
        label="Назва",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    director = forms.CharField(
        label="Режисер",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    genre = forms.CharField(
        label="Жанр",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    min_year = forms.IntegerField(
        label="Мінімальний рік",
        required=False,
        min_value=1896,
        max_value=2025,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_year = forms.IntegerField(
        label="Максимальний рік",
        required=False,
        min_value=1896,
        max_value=2025,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    min_rating = forms.FloatField(
        label="Мінімальний рейтинг",
        required=False,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_rating = forms.FloatField(
        label="Максимальний рейтинг",
        required=False,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )