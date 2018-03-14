import re

def validateEmail(enteredEmail):
	validator = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	if len(enteredEmail) > 7:
		if re.match(validator, enteredEmail) != None:
			return enteredEmail
	else:
		print ("Email length must be longer than 7 characters")
		return False

def validatePhone(enteredPhone):
	validator = r"^(\d{3}-\d{3}-\d{4})"
	if re.match(validator, enteredPhone) != None:
		return enteredPhone
	else:
		return False

def validateDate(enteredDate):
	validator="^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"
	if len(enteredDate) > 4:
		if re.match(validator, enteredDate) != None:
			return enteredDate
	else:
		print("This is an invalid date")
		return False

###########################

print validateEmail("hello@asu.edu")
print validatePhone('323-435-2345')
print validateDate('2018/03/15')
