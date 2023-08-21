from django import forms

from products.models import Product, ProductVersion


class ProductUserForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'purchase_price', 'category')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Write your name here...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5, 'placeholder': 'Write a description...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'purchase_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['слова', 'казино', 'криптовалюта',
                           'крипта', 'биржа', 'дешево', 'бесплатно',
                           'обман', 'полиция', 'радар']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('This word is forbidden!')

        return cleaned_data


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5, 'placeholder': 'Write a description...'
            })
        }


class ProductVersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ProductVersion
        fields = ('version_number', 'version_name', 'status')
