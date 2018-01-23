function formValid()
{	
	var prefix = document.Register-Form.Prefix;
    var suffix = document.Register-Form.Suffix;
	var gender = document.Register-Form.Gender;
	var month = document.Register-Form.Month;
	var day = document.Register-Form.Day;
	var year = document.Register-Form.Year;
	var uname = document.Register-Form.Uname;
	var pwd = document.Register-Form.Password;
	var cpwd = document.Register-Form.Cpassword;
    var phone = document.Register-Form.Phone;
	var city = document.Register-Form.City;
	var state = document.Register-Form.State;
	var zip = document.Register-Form.Zip;
	var ref = document.Register-Form.Referral;
	var pwdrequirement = /((?=.*[a-z])(?=.*[A-Z]).{1,})/gm;
	var phonerequirement = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
	var cityrequirement = /^[A-z]+$/;
	var ziprequirement = /^[0-9]+$/

		if (prefix.value == "Default")
	{
	    window.alert("Please select Prefix.");
        prefix.focus();
        return false;	
	}

	else if (suffix.value == "Default")
	{
	    window.alert("Please select Suffix.");
        suffix.focus();
        return false;	
	}
	
	else if (gender.value == "Default")
	{
	    window.alert("Please select Gender.");
        gender.focus();
        return false;	
	}
	
	else if (month.value == "Default")
	{
	    window.alert("Please select Birth Month.");
        month.focus();
        return false;	
	}

	else if (day.value == "Default")
	{
	    window.alert("Please select Birth Day.");
        day.focus();
        return false;	
	}	

	else if (year.value == "Default")
	{
	    window.alert("Please select Birth Year.");
        year.focus();
        return false;	
	}	

	else if (uname.value > 8)
	{
	    window.alert("Username must be at most 8 characters long.");
        uname.focus();
        return false;	
	}	
	
	else if (pwd.value > 8 && pwd.value.match(pwdrequirement) == false )
	{
	    window.alert("Password must be at most 8 characters long" + 
		" comprising at least a digit, a lowercase letter, and an uppercase letter");
        pwd.focus();
        return false;	
	}	
	
	else if (cpwd.value != pwd.value)
	{
		window.alert("Passwords must match" );
		cpwd.focus();
        return false;	
	}		

	else if (phone.value.match(phonerequirement) == false)
	{
	    window.alert("Phone format must be ###-###-####");
        phone.focus();
        return false;	
	}	
	
	else if (city.value.match(cityrequirement) == false)
	{
	    window.alert("City must contain only letters.");
        city.focus();
        return false;	
	}	
	
		
	else if (zip.length != 5 && zip.value.match(ziprequirement) == false)
	{
	    window.alert("Zip must be 5 digits.");
        zip.focus();
        return false;	
	}	
	
	else if (referral.value == "Default")
	{
	    window.alert("Please select Referral.");
        referral.focus();
        return false;	
	}
	
	
	else {
		window.alert("Thank you for Registering, Enjoy!");
		window.location.reload()
		return true;
	}
}
