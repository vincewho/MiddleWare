#!/usr/bin/env python2.7

#this function gets input from maufacturer and returns the data in a  dictionary
def addUser():	
	#list of input fields
	keys = ['Username','Password','First Name', 'Middle Name', 'Last Name', 'Company Name', 'Company Type', 'Address', 'Office Phone Number', 'Cell Phone Number', 'Email Address']
	#empty list which will hold user input
	datalist = []
	
	uname = raw_input("Username: ")
	datalist.append(uname)	

	pword = raw_input("Password: ")
	datalist.append(pword)

	fname = raw_input("First Name: ")
	datalist.append(fname)

	mname = raw_input("Middle Name: ")
	datalist.append(mname)

	lname = raw_input("Last Name: ")
	datalist.append(lname)

	cname = raw_input("Company Name: ")
	datalist.append(cname)

	ctype = raw_input("Company Type(Test Lab or Manufacturer): ")
	datalist.append(ctype)

	addr = raw_input("Address: ")
	datalist.append(addr)

	ophone = raw_input("Office phone number: ")
	datalist.append(ophone)

	cphone = raw_input("Cell phone number: ")
	datalist.append(cphone)

	email = raw_input("Email Address: ")
	datalist.append(email)

	#zip to combine both lists into a dictionary
	return dict(zip(keys, datalist))

#this the main
def main():
	#prints the return value of function
	print addUser()

#calls main
main()











	                                                  
