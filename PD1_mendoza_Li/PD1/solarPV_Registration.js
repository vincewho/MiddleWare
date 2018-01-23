function formValidation(form)
{
	var uname = form..username;
	var passid = form.Password;
	var cpassid = form.Cpassword;
	var lname = form.Lname;
	var gender = form.Gender;
	var address = form.Add1;
	var city = form.City;
	var state = form.State;
	var uzip = form.Zip;
	var uemail = form.Email;
	var phone = form.Phone;
	var company = form.Company; 
	
	if(username_validation(username))		
	{
		if(passid_validation(passid))
		{	
			if(cpassid_validation(cpassid, passid))
			{
				if(allLetter(lname))
				{
					if(gender_validation(gender))
					{
						if(c_allLetter(city))
						{
							if(state_validation(state))
							{
								if(allnumeric(uzip))
								{
									if(ValidateEmail(uemail))
									{
										if(phone_validation(phone))
										{
										}
									} 
								}
							}
						} 
					}
				}
			}
		}
	}

	return false;

}

function username_validation(uname)
{
	var uname_len = uname.value.length;
	if (uname_len == 0 || uname_len > 8)
	{
		alert("Username should not be empty / length be at most 8 characters long");
		uname.focus();
		return false;
	}
return true;
}

function passid_validation(passid)
{
	var passid_len = passid.value.length;
	var requirement = /((?=.*[a-z])(?=.*[A-Z]).{1,})/gm;
	if (passid_len == 0 || passid_len > 8 || pw.value.match(requirement) == false)
	{
		alert("Password should not be empty / length be at most 8 characters long & contain 1 upper, 1 lower, and 1 digit.");
		passid.focus();
		return false;
	}
return true;
}

function cpassid_validation(cpassid, passid)
{
	if (cpassid.value.match(passid) == false))
	{
		alert("Passwords must match.");
		cpassid.focus();
		return false;
	}
}

function allLetter(lname)
{ 
	var letters = /^[A-Za-z]+$/;
	if(lname.value.length > 0 || lname.value.match(letters))
	{
		return true;
	}
	else
	{
		alert('Last name should not be empty and have alphabet characters only');
		lname.focus();
		return false;
	}
}

function gender_validation(gender)
{
	if(gender.value == "Default")
	{
		alert('Select your Gender from the list');
		gender.focus();
		return false;
	}
	else
	{
		return true;
	}
}

function c_allLetter(city)
{ 
	var letters = /^[A-Za-z]+$/;
	if(city.value.length > 0 || city.value.match(letters))
	{
		return true;
	}
	else
	{
		alert('Cityshould not be empty and have alphabet characters only');
		city.focus();
		return false;
	}
}
function state_validation(state)
{
	if(state.value == "Default")
	{
		alert('Select your State from the list');
		state.focus();
		return false;
	}
	else
	{
		return true;
	}
}

function allnumeric(uzip)
{ 
	var numbers = /^[0-9]+$/;
	if(uzip.value.match(numbers) || uzip.value.length == 5)
	{	
		return true;
	}
	else
	{
		alert('ZIP code must have 5 numeric characters only');
		uzip.focus();
		return false;
	}
}

function ValidateEmail(uemail)
{
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(uemail.value.match(mailformat))
	{
		return true;
	}
	else
	{
		alert("You have entered an invalid email address!");
		uemail.focus();
		return false;
	}
}

function phone_validation(phone)
{
	var numbers = /^[0-9]+$/;
	if(phone.value.match(numbers) == false || phone.value.length != 10)
	{	
		alert('Phone Number must have 10 numeric characters only');
		phone.focus();
		return false;
	}

	else
	{
		alert('Form Succesfully Submitted');
		window.location.reload()
		return true;
	}
}
