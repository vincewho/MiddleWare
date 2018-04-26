# solarProject/forms.py
from django import forms
from django.forms import CharField, FileField, IntegerField, DecimalField
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

	def clean_username(self):
		username = self.cleaned_data.get('username')
		# do stuff to the data here
		return username[0].upper() + username[1:].lower()

	def clean_fname(self):
		fname = self.cleaned_data.get('fname')
		return fname[0].upper() + fname[1:].lower()

	def clean_lname(self):
		lname = self.cleaned_data.get('lname')
		return lname[0].upper() + lname[1:].lower()

	def clean_mname(self):
		mname = self.cleaned_data.get('mname')
		return mname

	def clean_address(self):
		address = self.cleaned_data.get('address')
		return address

	def clean_officenum(self):
		officenum = self.cleaned_data.get('officenum')
		return officenum

	def clean_cellnum(self):
		cellnum = self.cleaned_data.get('cellnum')
		return cellnum

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email


class registerModForm(forms.ModelForm):
	class Meta:
		model = Manufacturer
		fields = '__all__'

	def clean_name(self):
		name = self.cleaned_data.get('name')
		return name

	def clean_address(self):
		address = self.cleaned_data.get('address')
		return address

	def clean_country(self):
		country = self.cleaned_data.get('country')
		return country


class registerTestLabForm(forms.ModelForm):
	class Meta:
		model = TestLab
		fields = '__all__'

	def clean_name(self):
		name = self.cleaned_data.get('name')
		return name

	def clean_address(self):
		address = self.cleaned_data.get('address')
		return address

	def clean_country(self):
		country = self.cleaned_data.get('country')
		return country


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


class uploadForm(forms.ModelForm):
	upload = FileField(
		label='Please upload a file',
		required=False)

	class Meta:
		model = fileUpload
		fields = '__all__'

	def handle_uploaded_file(self):

		with open(self, 'wb+') as destination:
			for chunk in self.chunks():
				destination.write(chunk)
