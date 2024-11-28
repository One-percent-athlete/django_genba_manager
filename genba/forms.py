from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile, Genba, Daily_report

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

class GenbaForm(forms.ModelForm):
	head_person = forms.Select(attrs={"class":"form-select", "placeholder": "現場の長"}),
	attendees = forms.SelectMultiple(attrs={"class":"form-control", "placeholder": "その他作業員"}),
	name = forms.Select(attrs={"class":"form-select", "placeholder": "現場名"}),
	client = forms.Select(attrs={"class":"form-select", "placeholder": "取引先"}),
	address = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'場所'}))
	job_description = forms.CharField(label="", max_length=100,required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'作業内容'}))
	note = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'連絡事項'}))
	is_active = forms.BooleanField(label="未完了", required=False)
	start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

	class Meta:
		model = Genba
		fields = ('head_person', 'attendees', 'name', 'client', 'address', 'job_description','note', 'is_active', 'start_date', 'end_date')


class DailyReportForm(forms.ModelForm):
	PAYMENT_TYPES = (
        ('現金','現金'),
        ('カード', 'カード'),
        ('電子マネー', '電子マネー'),
        )
	DAY_OR_NIGHT = (
        ('日勤','日勤'),
        ('夜勤', '夜勤'),
        )
	genba = forms.Select(attrs={"class":"form-select", "placeholder": "現場名"}),
	distance = forms.Select(attrs={"class":"form-select", "placeholder": "距離"}),
	highway_start = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'高速道路乗ったインター'}))
	highway_end = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'高速道路降りたインター'}))
	highway_payment = forms.ChoiceField(label="支払い方法", choices=PAYMENT_TYPES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	shift = forms.ChoiceField(label="昼夜シフト", choices=DAY_OR_NIGHT, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	parking = forms.Select(attrs={"class":"form-select", "placeholder": "駐車料金"}),
	paid_by = forms.Select(attrs={"class":"form-select", "placeholder": "建替人"}),
	hotel = forms.BooleanField(label="宿泊利用", required=False)
	other_payment = forms.BooleanField(label="その他経費", required=False),
	other_payment_amount = forms.Select(attrs={"class":"form-select", "placeholder": "金額"}),
	daily_details = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'作業内容'}))
	daily_note = forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'その他連絡事項'}))
	kentaikyo = forms.BooleanField(label="建退共", required=False),
	start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
	end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

	class Meta:
		model = Daily_report
		fields = ('genba', 'distance', 'highway_start', 'highway_end', 'highway_payment', 'shift', 'parking','paid_by', 'hotel', 'other_payment', 'other_payment_amount', 'daily_details', 'daily_note', 'kentaikyo', 'start_time', 'end_time')
		