function formValid()
{
	var prefix = document.getElementById("Prefix").value;
    var suffix = document.getElementById("Suffix").value;
	var gender = document.getElementById("Gender").value;
	var uname = document.getElementById("Uname").value;
	var pwd = document.getElementById("Password").value;
	var cpwd = document.getElementById("Cpassword").value;
    var phone = document.getElementById("Phone").value;
	var city = document.getElementById("City").value;
	var state = document.getElementById("State").value;
	var zip = document.getElementById("Zip").value;
	var ref = document.getElementById("Referral").value;
	var pwdrequirement = /((?=.*[a-z])(?=.*[A-Z]).{1,})/gm;
	var phonerequirement = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
	var cityrequirement = /^[A-z]+$/;
	var ziprequirement = /^[0-9]+$/


	if (prefix == "Default")
	{
	    window.alert("Please select Prefix.");
        prefix.focus();
        return false;	
	}

	if (suffix == "Default")
	{
	    window.alert("Please select Suffix.");
        suffix.focus();
        return false;	
	}
	
	if (gender == "Default")
	{
	    window.alert("Please select Gender.");
        gender.focus();
        return false;	
	}

	if (uname > 8)
	{
	    window.alert("Username must be at most 8 characters long.");
        uname.focus();
        return false;	
	}	
	
	if (pwd > 8 && pwd.match(pwdrequirement) == false )
	{
	    window.alert("Password must be at most 8 characters long" + 
		" comprising at least a digit, a lowercase letter, and an uppercase letter");
        pwd.focus();
        return false;	
	}	
	
	if (cpwd != pwd)
	{
		window.alert("Passwords must match" );
		cpwd.focus();
        return false;	
	}		

	if (phone.match(phonerequirement) == false)
	{
	    window.alert("Phone format must be ###-###-####");
        phone.focus();
        return false;	
	}	
	
	if (city.match(cityrequirement) == false)
	{
	    window.alert("City must contain only letters.");
        city.focus();
        return false;	
	}	
	
		
	if (zip.length != 5 && zip.match(ziprequirement) == false)
	{
	    window.alert("Zip must be 5 digits.");
        zip.focus();
        return false;	
	}	
	
	if (referral == "Default")
	{
	    window.alert("Please select Referral.");
        referral.focus();
        return false;	
	}
	return true;
}
