from django.contrib.auth.forms import UserCreationForm
from forum_pages.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'telegram', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control' 
        self.fields['telegram'].widget.attrs['class'] = 'form-control' 
        self.fields['email'].widget.attrs['class'] = 'form-control' 
