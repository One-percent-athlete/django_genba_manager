from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'ユーザー名'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = '確認パスワード'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before for verification.</small></span>'
    
class UserProfileForm(forms.ModelForm):
	CHOICE = [
       	('元請', '元請'),
        ('正社員', '正社員'),
        ('管理', '管理'),]
	fullname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'お名前フルねーム、スペースなし'}))
	phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'携帯電話番号'}))
	note = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Note'}))
	contract_type = forms.ChoiceField(label="雇用形態", choices=CHOICE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	is_active = forms.BooleanField(label="is_active", required=False)

	class Meta:
		model = Profile
		fields = ('fullname', 'phone', 'note', 'contract_type', 'is_active')
		