from django import forms
from website.models import Contact, newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255, required=False)  
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'required': False})  
        }

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        instance.name = 'Unknown'  
        if commit:
            instance.save()
        return instance

class newsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'