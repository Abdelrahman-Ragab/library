from django import forms
from .models import Book , Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('active',)

    widgets = {
        'retal_price_day': forms.NumberInput(attrs = {'class':'form-control' , 'id':'retalpriceday'}),
        'retal_period': forms.NumberInput(attrs = {'class':'form-control' , 'id':'retalperiod'}),
        'total_rental': forms.NumberInput(attrs = {'class':'form-control' , 'id':'totalrental'}),
    }