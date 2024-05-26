# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=15)
    email = forms.EmailField(label='E-Mail')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    location = forms.ChoiceField(label='Location', choices=[
        ('ny', 'New York'),
        ('la', 'Los Angeles'),
        ('sf', 'San Francisco'),
    ])
    service = forms.ChoiceField(label='Service', choices=[
        ('web', 'Web Development'),
        ('seo', 'SEO Optimization'),
        ('design', 'Graphic Design'),
    ])
