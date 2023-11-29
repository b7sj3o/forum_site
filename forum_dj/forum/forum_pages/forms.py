from django.forms import ClearableFileInput, ModelForm
from .models import User
from django.core.exceptions import ValidationError


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'telegram', 'avatar', 'is_show_telegram']
        

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control w-25'
        self.fields['email'].widget.attrs['class'] = 'form-control w-25'
        self.fields['telegram'].widget.attrs['class'] = 'form-control w-25'
        self.fields['avatar'].widget.attrs['class'] = 'form-control w-25'
        self.fields['is_show_telegram'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_show_telegram'].widget.attrs['id'] = 'flexCheckChecked'

    def clean_username(self):
        username = self.cleaned_data['username']
        existing_user = User.objects.exclude(
            pk=self.instance.pk).filter(username=username)
        if existing_user.exists() and username != self.instance.username:
            raise ValidationError('Цей нікнейм вже зайнятий.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        existing_user = User.objects.exclude(
            pk=self.instance.pk).filter(email=email)
        if existing_user.exists() and email != self.instance.email:
            raise ValidationError('Цей емейл вже зареєстрований.')
        return email
