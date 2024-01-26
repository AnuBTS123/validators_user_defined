from django import forms
from app.models import *
from django.core.validators import MinLengthValidator

def validate_for_c(data):
    if data.lower().startswith('c'):
        raise forms.ValidationError('started with c')
    
def validate_for_length(data):
    if len(data)<5:
        raise forms.ValidationError('length is < 5')


class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_c,MinLengthValidator(5)])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField(widget=forms.Textarea(attrs={'cols':7,'rows':7}))
    email=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput())


    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('email not matched')
        
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')
        
    