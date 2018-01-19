function formValidation()
{
	var uname = document.registration.uname;
	var userPassword = document.registration.userPassword;
	var confirmPassword = document.registration.confirmPassword;
	var zip = document.registration.zip;
	var email = document.registration.email;

	if(username_validation(uname))
	{
		if(password_validation(userPassword))
		{
			if(confirm_password(userPassword, confirmPassword))
			{
				if(zip_validaiton(zip))
				{
					if(email_validation(email))
					{
					}
				}
			}
		}
	}
	return false;
}

function username_validation(uname)
{
	var uname_length = uname.value.length;
	var unameReq = '/^[a-z0-9_-]{1,}$/';
	uname = uname.toString();
	if (uname_length == 0 || uname_length > 8)
	{
		alert("Username required! Must be at most 8 characters long.");
		uname.focus();
		return false;
	}
	else if (uname.match(unameReq))
	{
		alert("This doesn't match");
		return false;
	}
	else
	{
		return true;
	}
}

function password_validation(pw)
{
	var requirement = /((?=.*[a-z])(?=.*[A-Z]).{1,})/gm;
	if (pw.value.match(requirement))
	{
		return true;
	}
	else
	{
		alert("Password must contain have one uppercase, one lower case, and one digit and be at most 8 characters long.");
		pw.focus();
		return false;
	}
}

function confirm_password(pw, cpw)
{
	if (cpw.value.match(pw))
	{
		return true;
	}
	else
	{
		alert("Passwords must match.");
		cpw.focus();
		return false;
	}
}

function zip_validation(zip)
{
	var requirement = /^[0-9]+$/;
	if(zip.value.match(requirement))
	{
		return true;
	}
	else
	{
		alert('ZIP code must have numeric characters only');
		zip.focus();
		return false;
	}
}

function email_validation(email)
{
	var requirement = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(email.value.match(requirement))
	{
		alert('Form Succesfully Submitted');
		window.location.reload()
		return true;
	}
	else
	{
		alert("You have entered an invalid email address!");
		email.focus();
		return false;
	}
}
