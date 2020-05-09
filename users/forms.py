from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Role
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

class PropertyModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	#IDnum = forms.CharField(label='Enter 8 Digit ID number', max_length = 8)
	IDnum = forms.CharField(label='What is your ID number?',required=True,max_length =10,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))
	classification= PropertyModelChoiceField(queryset = Role.objects.filter(any_create=True))
	SecurityQ= forms.CharField(label='Select A Security Question', widget=forms.Select(choices=SECURITY_QUESTION))
	SecuirtyA = forms.CharField()


	class Meta:
		model = User
		fields = ['username', 'email','IDnum', 'password1', 'password2','classification','SecurityQ','SecuirtyA']

class ManagerRegisterForm(UserCreationForm):
	email = forms.EmailField()
	# IDnum = forms.CharField(label='Enter 8 Digit ID number', max_length = 8)
	IDnum = forms.CharField(label='What is your ID number?', required=True, widget=forms.TextInput(
		attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter numbers Only '}))
	classification = PropertyModelChoiceField(queryset=Role.objects.filter(add=True))
	SecurityQ = forms.CharField(label='Select A Security Question', widget=forms.Select(choices=SECURITY_QUESTION))
	SecuirtyA = forms.CharField(label='Answer')

	class Meta:
		model = User
		fields = ['username', 'email', 'IDnum', 'password1', 'password2', 'classification', 'SecurityQ', 'SecuirtyA']

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

