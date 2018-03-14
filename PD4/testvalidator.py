import re

def validateEmail(enteredEmail):
	validator = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	if len(enteredEmail) > 7:
		if re.match(validator, enteredEmail) != None:
			return enteredEmail
		else:
			return False
	else:
		return False
			
def validatePhone(enteredPhone):
	validator = r"^(\d{3}-\d{3}-\d{4})"
	if re.match(validator, enteredPhone) != None:
		return enteredPhone
	else:
		return False
	