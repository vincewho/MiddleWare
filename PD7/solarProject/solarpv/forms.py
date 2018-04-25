# solarProject/forms.py
from django import forms
from django.forms import CharField, IntegerField, DecimalField
from backend.models import User, Manufacturer, Product, TestLab, fileUpload


class registerForm(forms.ModelForm):
	mname = CharField(max_length=100, required=False, label='Middle Name')
	officenum = CharField(max_length=15, required=False, label='Office Number')

	class Meta:
		model = User
		# fields = ('username', 'fname', 'lname', 'mname', 'address', 'officenum', 'cellnum', 'email',)
		fields = '__all__'
		labels = {
			'fname': 'First Name',
			'lname': 'Last Name',
			'cellnum': 'Cell Number'}


class registerModForm(forms.ModelForm):
	class Meta:
		model = Manufacturer
		fields = '__all__'


class registerTestLabForm(forms.ModelForm):
	class Meta:
		model = TestLab
		fields = '__all__'


class registerProductForm(forms.ModelForm):
	weight                   = DecimalField(max_digits=10, decimal_places=2, required=False)
	num_of_cells             = IntegerField(required=False)
	num_of_cells_in_series   = IntegerField(required=False)
	num_of_series_strings    = IntegerField(required=False)
	num_of_diodes            = IntegerField(required=False)
	series_fuse_rating       = DecimalField(max_digits=10, decimal_places=2, required=False)
	interconnect_material    = CharField(max_length=20, required=False)
	interconnect_supplier    = CharField(max_length=20, required=False)
	superstrate_type         = CharField(max_length=20, required=False)
	superstrate_manufacturer = CharField(max_length=20, required=False)
	substrate_type           = CharField(max_length=20, required=False)
	substrate_manufacturer   = CharField(max_length=20, required=False)
	frame_material           = CharField(max_length=20, required=False)
	encapsulant_manufacturer = CharField(max_length=20, required=False)
	max_sys_volt             = DecimalField(max_digits=10, decimal_places=2, required=False)

	class Meta:
		model = Product
		fields = '__all__'


class uploadForm(forms.Form):
	file = forms.FileField(
		label='Please upload a file'
		)

	# class Meta:
	# 	model = fileUpload
	# 	fields = '__all__'
