from django.forms import ModelForm, Form, CharField, PasswordInput
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserCreationForm(Form):
    username = CharField(max_length=150, required=True)
    email = CharField(max_length=254, required=True)
    password1 = CharField(widget=PasswordInput, required=True, label='Password')
    password2 = CharField(widget=PasswordInput, required=True, label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValueError('A user with that username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValueError('A user with that email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise ValueError('The passwords do not match.')
        
        return cleaned_data

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
