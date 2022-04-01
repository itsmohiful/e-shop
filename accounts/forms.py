from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
