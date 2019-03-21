from django import forms

from .models import ImiStatus

class ImiModelForm(forms.ModelForm):
    content = forms.CharField(label='',widget= forms.Textarea(attrs={'placeholder':' Whats in your mind!!','rows':4, 'cols':15}))
    class Meta:
        model = ImiStatus
        fields = [
           
            'content',
        ]

    # def clean_content(self,*args,**kwargs):
    #     content = self.cleaned_data.get('content')
    #     if content == 'abc':
    #         raise forms.ValidationError('Cannot be abc')
    #     return content