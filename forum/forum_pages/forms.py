from django.forms import ModelForm
from .models import (
    BaseTheme,
    User,
    Advertisement,
    MainPictureBanner,
    MainTextBanner,
    Theme,
    TopAgency,
    SubTheme,
    AgencyJobOrganization
)
from django.core.exceptions import ValidationError


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'telegram',
                  'avatar', 'is_show_telegram']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'

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


class MainPictureBannerForm(ModelForm):
    class Meta:
        model = MainPictureBanner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MainPictureBannerForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class AdvertismentForm(ModelForm):
    class Meta:
        model = Advertisement
        exclude = ['name']

    def __init__(self, *args, **kwargs):
        super(AdvertismentForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ThemeForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class MainTextBannerForm(ModelForm):
    class Meta:
        model = MainTextBanner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MainTextBannerForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class TopAgencyForm(ModelForm):
    class Meta:
        model = TopAgency
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TopAgencyForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class SubThemeForm(ModelForm):
    class Meta:
        model = SubTheme
        fields = ['title', 'main_text']

    def __init__(self, *args, **kwargs):
        super(SubThemeForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class BaseThemeForm(ModelForm):
    class Meta:
        model = BaseTheme
        # fields = ['title', 'text', 'link']
        fields = ['title', 'text']

    def __init__(self, *args, **kwargs):
        super(BaseThemeForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class AgencyJobOrganizationForm(ModelForm):
    class Meta:
        model = AgencyJobOrganization
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(AgencyJobOrganizationForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'
