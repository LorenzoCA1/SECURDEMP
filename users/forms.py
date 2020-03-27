from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

SECURITY_QUESTION= [
    ('Question1', 'In what city did you have your first ever birthday party?'),
    ('Question2', 'What is the last name of your Science class teacher in high school?'),
    ('Question3', 'Which company manufactured your first mobile phone?'),
    ('Question4', 'Who was your childhood hero?'),
    ('Question5', 'Where was your best family vacation?'),
    ]

ROLE_CHOICE= [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ]


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	#IDnum = forms.CharField(label='Enter 8 Digit ID number', max_length = 8)
	IDnum = forms.CharField(label='What is your ID number?',required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
	classification= forms.CharField(label='What is your Role?', widget=forms.Select(choices=ROLE_CHOICE))
	SecurityQ= forms.CharField(label='Select A Security Question', widget=forms.Select(choices=SECURITY_QUESTION))
	SecuirtyA = forms.CharField()


	class Meta:
		model = User
		fields = ['username', 'email','IDnum', 'password1', 'password2','classification','SecurityQ','SecuirtyA']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	#IDnum = forms.CharField(max_length = 100)

	class Meta:
		model = User
		fields = ['username', 'email']
		
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']			

