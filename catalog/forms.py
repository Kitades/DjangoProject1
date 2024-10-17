from django import forms
from django.forms import BooleanField

from banwords import ban
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):  # делает красивые рамки для ввода
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ('image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in ban:
            raise forms.ValidationError('BAN WORD')
        return cleaned_data


class ProductModerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
