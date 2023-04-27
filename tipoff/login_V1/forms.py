from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class add_user(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ['first_name','last_name','username','password1','password2']

class CustomUserCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name')