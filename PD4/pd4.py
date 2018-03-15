#!/usr/bin/env python2.7

import csv
import sys
from collections import defaultdict
import os #use os.system('clear') to clear terminal

#import datetime

#import the classes
import  myClasses

from myClasses import User
from myClasses import manufacturer
from myClasses import Product

#import regex
import re


####################################### Read in CSV file ####################################### 
def createDict(csv_file):
	lab_dict = defaultdict(list)

	filein=open(csv_file, 'r')
	data=csv.DictReader(filein, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

	return data

csv_file = 'test_results.csv'
data = createDict(csv_file)
dict_list = [row for row in data]
#To see the list, uncomment the line below:
#print csv_dict

####################################### VALIDATORS ####################################### 
def validateEmail(enteredEmail):
	validator = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	if len(enteredEmail) > 7:
		if re.match(validator, enteredEmail) is not None:
			return enteredEmail
		else:
			print ("Invalid. Email format: user@example.com")
			return False	
	else:
		print ("Invalid. Email length must be longer than 7 characters.")
		return False

def validatePhone(enteredPhone):
	validator = r"^(\d{3}-\d{3}-\d{4})"
	if re.match(validator, enteredPhone) is not None:
		return enteredPhone
	else:
		print ("This is an invalid phone format: ###-###-####")
		return False
		
def validateUserName(name):
	validator = "^[A-Za-z0-9]+$"
	if len(name) <= 20:
		if re.match(validator, name) is not None:
			return name
		else:
			print ("Username must contain only letters and numbers.")
			return False
	else:
		print ("Username must be less than 20 characters.")
		return False
		
def validatePassword(pword):
	validator = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,20}$"
	if re.match(validator, pword) is not None:
		return pword
	else:
		print("Password must be: \n" + "- Min: 4 characters \n" + "- Max: 20 characters \n" + "- Include 1 upper case letter \n" + "- Include 1 lower case letter \n" + "- Include 1 digit.")
		return False
		
def validateDate(enteredDate):
	validator="^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"
	if len(enteredDate) > 4:
		if re.match(validator, enteredDate) is not None:
			return enteredDate
		else:
			print("This is an invalid date.")
			return False
	else:
		print("This is an invalid date.")
		return False

def validateCompany(ctype):
	if  ctype == "Test Lab" or ctype == "Manufacturer" :
			return ctype

	else: 
		print ("Invalid. Company Type must be either Test Lab or Manufacturer.")
		return False 
		
def validateAddress(addr):
	validator = r"\d+\s[A-z]+\s[A-z]+"
	if re.match(validator, addr) is not None:
		return addr
	else:
		print ("Invalid. Format: 1234 ExampleName Ave")
		return False
	
def validateString(value):
	validator = "^[a-zA-Z]+$"
	if len(value) <= 20:
		if re.match(validator, value) is not None:
			return value
		else: 
			print ("Invalid. Must contain only letters.")
			return False 
	else: 
		print ("Invalid. Cannot exceed 20 characters.")
		return False 
	
def validateFloat(value):
	validator = r"[0-9]+\.+[0-9]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Not float format.")
		return False
		
def validateInt(value):
	validator = "[0-9]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Not an integer.")
		return False

def validateDimension(value):
	validator = "^[0-9]+x[0-9]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Format: ##x## (No spaces)")
		return False

def validateAlphaNum(value):
	validator = r"^[a-zA-Z]+\s[0-9]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Format: Name Number")
		return False
		
def validateRating(value):
	validator = r"^[0-9]+\/[0-9A-Z0-9]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Example Format: 10/10SQ050 ")
		return False

def validateSub(value):
	validator = r"^[A-Z]+\/[0-9]+\.+[0-9]+[a-zA-Z]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Example Format: TPT/0.35mm ")
		return False	

def validatebox(value):
	validator = r"^[A-Z]+\-[A-Z0-9A-Z]+$"
	if re.match(validator, value) is not None:
		return value
	else:
		print("Invalid. Example Format: PV-RH050BV")
		return False	

####################################### Clear Screens ####################################### 
def ClearUser():
		os.system('clear')
        	print "----------------NEW USER REGISTRATION---------------"
			print ""
			
def ClearMDS():
		os.system('clear')
		print "----------------MDS FORM---------------"
		print ""
		
def ClearProduct():
		os.system('clear')
		print "----------Product Information-----------"
		print ""

		
#REGISTER PV MODULE MDS FORM : this function gets input and returns the data in a  dictionary
def addPV():	
	#list of input fields
	keys = ['Manufacturer', 'Location', 'Contact','Address','Email', 'Phone', 'Model Number', 'Module lxw', 'Module Weight', 'Individual Cell Area', 'Cell Technology','Cell Manufacturer','Cell Manufactureing Location','Total number of cells', 'Number of cells in a series','Number of series strings','Number of bypass diodes', 'Bypass diode rating', 'Bypass diode max junct temp', 'Series fuse rating', 'Innterconnect material', 'Interconnect dimensions', 'Superstrate type', 'Superstrate Manufacturer', 'Substrate Type', 'Substrate Manufacturer', 'FrameType' ,'Frame adhesive', 'Encapsulant Type','Encapsulant Manufacturer', 'Junction Box Type', 'Junction box manufacturer', 'Junction box potting material', 'Junction box adhesive', 'Junction Box Use Intention', 'Cable & Connector type', 'Maximum system voltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff' ]
	#empty list which will hold user input
	datalist = []
	
	ClearMDS()
	man = raw_input("Manufacturer: ")
	while validateString(man) is False:
		man = raw_input("Re-enter Manufacturer: ")
	datalist.append(man)
	
	ClearMDS()
	loc = raw_input("Location: ")
	while validateString(loc) is False:
		loc = raw_input("Re-enter Location: ")
	datalist.append(loc)

	ClearMDS()
	cont = raw_input("Contact: ")
	while validateString(cont) is False:
		cont = raw_input("Re-enter Contact: ")
	datalist.append(cont)

	ClearMDS()
	addr = raw_input("Address: ")
	while validateAddress(addr) is False:
		addr = raw_input("Re-enter Address: ")
	datalist.append(addr)
	
	ClearMDS()
	email = raw_input("Email: ")
	while validateEmail(email) is False:
		email = raw_input("Re-enter Email: ")
	datalist.append(email)
	
	ClearMDS()
	phone = raw_input("Phone: ")
	while validatePhone(phone) is False:
		phone = raw_input("Re-enter phone: ")
	datalist.append(phone)
	
	ClearMDS()
	mnum = raw_input("Model Number: ")
	while validateInt(mnum) is False:
		mnum = raw_input("Re-enter Model Number: ")
	datalist.append(mnum)
	
	ClearMDS()
	mlxw = raw_input("Module total length x width (cmxcm): ")
	while validateDimension(mlxw) is False:	
		mlxw = raw_input("Re-enter Module total length x width (cmxcm): ")
	datalist.append(mlxw)
	
	ClearMDS()
	mwgt = raw_input("Module weight(kg): ")
	while validateFloat(mwgt) is False:
		mwgt = raw_input("Re-enter Module weight(kg): ")
	datalist.append(mwgt)

	ClearMDS()
	icarea = raw_input("Individual Cell Area(cm^2): ")
	while validateFloat(icarea) is False:
		icarea = raw_input("Re-enter Individual Cell Area(cm^2): ")
	datalist.append(icarea)
	
	ClearMDS()
	ctech = raw_input ("Cell Technology: ")
	while validateString(ctech) is False:
		ctech = raw_input ("Re-enter Cell Technology: ")
	datalist.append(ctech)
	
	ClearMDS()
	cmanpt = raw_input("Cell Manufacturer and Part#: ")
	while validateAlphaNum(cmanpt) is False:
		cmanpt = raw_input("Re-enter Cell Manufacturer and Part#: ")
	datalist.append(cmanpt)

	ClearMDS()
	cmanloc = raw_input("Cell Manufacturing Location: ")
	while validateString(cmanloc) is False:
		cmanloc = raw_input("Re-enter Cell Manufacturing Location: ")
	datalist.append(cmanloc)

	ClearMDS()
	totcell = raw_input("Total number of cells: ")
	while validateInt(totcell) is False:
		totcell = raw_input("Re-enter Total number of cells: ")
	datalist.append(totcell)

	ClearMDS()
	cseries = raw_input("Number of cells in series: ")
	while validateInt(cseries) is False:
		cseries = raw_input("Re-enter Number of cells in series: ")
	datalist.append(cseries)

	ClearMDS()
	serstg = raw_input("Number of series strings: ")
	while validateInt(serstg) is False:
		serstg = raw_input("Re-enter Number of series strings: ")
	datalist.append(serstg)

	ClearMDS()
	bydid = raw_input("Number of bypass diodes: ")
	while validateInt(bydid) is False:
		bydid = raw_input("Re-enter Number of bypass diodes: ")
	datalist.append(bydid)

	ClearMDS()
	bdrateA = raw_input("Bypass diode rating(A): ")
	while validateRating(bdrateA) is False:
		bdrateA = raw_input("Re-enter Bypass diode rating(A): ")
	datalist.append(bdrateA)

	ClearMDS()
	juntemp = raw_input("Bypass diode max junction temp(C): ")
	while validateInt(juntemp) is False:
		juntemp = raw_input("Re-enter Bypass diode max junction temp(C): ")
	datalist.append(juntemp)

	ClearMDS()
	sfratingA = raw_input("Series Fuse Rating(A): ")
	while validateInt(sfratingA) is False:
		sfratingA = raw_input("Re-enter Series Fuse Rating(A): ")
	datalist.append(sfratingA)

	ClearMDS()
	matsup = raw_input("Interconnect material and supplier model no.: ")
	while validateAlphaNum(matsup) is False:
		matsup = raw_input("Re-enter Interconnect material and supplier model no.: ")
	datalist.append(matsup)

	ClearMDS()
	dimen = raw_input("Interconnect dimensions(mm x mm): ")
	while validateDimension(dimen) is False:
		dimen =  raw_input("Re-enter Interconnect dimensions(mm x mm): ")
	datalist.append(dimen)

	ClearMDS()
	suptype = raw_input("Superstrate Type: ")
	while validateString(suptype) is False:
		suptype = raw_input("Re-enter Superstrate Type: ")
	datalist.append(suptype)

	ClearMDS()
	supmanpt = raw_input("Superstrate Manfacturer and part#: ")
	while validateAlphaNum(supmanpt) is False:
		supmanpt = raw_input("Re-enter Superstrate Manfacturer and part#: ")
	datalist.append(supmanpt)

	ClearMDS()
	subtype = raw_input("Substrate Type: ")
	while validateSub(subtype) is False:
		subtype = raw_input("Re-enter Substrate Type: ")
	datalist.append(subtype)

	ClearMDS()
	submanpt = raw_input("Substrate Manufacturer and part#: ")
	while validateAlphaNum(submanpt) is False:
		submanpt = raw_input("Re-enter Substrate Manufacturer and part#: ")
	datalist.append(submanpt)

	ClearMDS()
	frametype = raw_input("Frame Type and Material: ")
	while validateString(frametype) is False:
		frametype = raw_input("Re-enter Frame Type and Material: ")
	datalist.append(frametype)

	ClearMDS()
	framead = raw_input("Frame adhesive: ")
	while validateAlphaNum(framead) is False:
		framead = raw_input("Re-enter Frame adhesive: ")
	datalist.append(framead)

	ClearMDS()
	encaptype = raw_input("Encapsulant Type: ")
	while validateSub(encaptype) is Flase:
		encaptype = raw_input("Re-enter Encapsulant Type: ")
	datalist.append(encaptype)

	ClearMDS()
	encapmanpt = raw_input("Encapsulant Manufacturer and part#: ")
	while validateAlphaNum(encapmanpt) is False:
		encapmanpt = raw_input("Encapsulant Manufacturer and part#: ")
	datalist.append(encapmanpt)

	ClearMDS()
	junboxtype = raw_input("Junction box type: ")
	while validatebox(junboxtype) is False:
		junboxtype = raw_input("Re-enter Junction box type: ")
	datalist.append(junboxtype)

	ClearMDS()
	junboxmanpt = raw_input("Junction box manufacturer and part#: ")
	while validateAlphaNum(junboxmanpt) is False:
		junboxmanpt = raw_input("Re-enter Junction box manufacturer and part#: ")
	datalist.append(junboxmanpt)

	ClearMDS()
	junboxpot = raw_input("Junction box potting material, if any: ")
	while validateString(junboxpot) is False:
		junboxpot = raw_input("Re-enter Junction box potting material, if any: ")
	datalist.append(junboxpot)

	ClearMDS()
	junboxadh = raw_input("Junction box adhesive: ")
	while validateAlphaNum(junboxadh) is False:
		junboxadh = raw_input("Re-enter Junction box adhesive: ")
	datalist.append(junboxadh)

	ClearMDS()
	junboxuse = raw_input("Is junction box intended for use with Conduit?: ")
	while validateString(junboxuse) is False:
		junboxuse = raw_input("Re-enter - Is junction box intended for use with Conduit?: ")
	datalist.append(junboxuse)

	ClearMDS()
	cabcontype = raw_input("Cable & Connector Type: ")
	while validateAlphaNum(cabcontype) is False:
		cabcontype = raw_input("Re-enter Cable & Connector Type: ")
	datalist.append(cabcontype)

	ClearMDS()
	maxsysvol = raw_input("Max system voltage(V): ")
	while validateInt(maxsysvol) is False:
		maxsysvol = raw_input("Max system voltage(V): ")
	datalist.append(maxsysvol)

	ClearMDS()
	voc = raw_input("Voc(V): ")
	while validateFloat(voc) is False:
		voc = raw_input("Re-enter Voc(V): ")
	datalist.append(voc)

	ClearMDS()
	isc = raw_input("Isc(A): ")
	while validateFloat(isc) is False:
		isc = raw_input("Re-enter Isc(A): ")
	datalist.append(isc)

	ClearMDS()
	vmp = raw_input("Vmp(V): ")
	while validateFloat(vmp) is False:
		vmp = raw_input("Re-enter Vmp(V): ")
	datalist.append(vmp)

	ClearMDS()
	imp = raw_input("Imp(A): ")
	while validateFloat(imp) is False:
		imp = raw_input("Re-enter Imp(A): ")
	datalist.append(imp)

	ClearMDS()
	pmp = raw_input("Pmp(W): ")
	while validateInt(pmp) is False:
		pmp = raw_input("Re-enter Pmp(W): ")
	datalist.append(pmp)

	ClearMDS()
	ff = raw_input("FF(%): ")
	while validateInt(ff) is False:
		ff = raw_input("Re-enter FF(%): ")
	datalist.append(ff)
	
	os.system('clear')

	#zip to combine both lists into a dictionary
	return dict(zip(keys, datalist))

#REGISTER USER: this function gets input and returns the data in a  dictionary	
def addUser():	
	#list of input fields
	keys = ['Username','Password','First Name', 'Middle Name', 'Last Name', 'Company Name', 'Company Type', 'Address', 'Office Phone Number', 'Cell Phone Number', 'Email Address']
	#empty list which will hold user input
	datalist = []
	
	ClearUser()
	uname = raw_input("Username: ")
	while validateUserName(uname) is False:
		uname = raw_input("Re-enter Username: ")
	datalist.append(uname)
	
	ClearUser()
	pword = raw_input("Password: ")
	while validatePassword(pword) is False:
		pword = raw_input("Re-enter Password: ")
	datalist.append(pword)

	ClearUser()
	fname = raw_input("First Name: ")
	while validateString(fname) is False:
		fname = raw_input("Re-enter First Name: ")
	datalist.append(fname)

	ClearUser()
	mname = raw_input("Middle Name: ")
	while validateString(mname) is False:
		mname = raw_input("Re-enter Middle Name: ")
	datalist.append(mname)

	ClearUser()
	lname = raw_input("Last Name: ")
	while validateString(lname) is False:
		lname = raw_input("Re-enter Last Name: ")	
	datalist.append(lname)

	ClearUser()
	cname = raw_input("Company Name: ")
	while validateString(cname) is False:
		cname = raw_input("Re-enter Company Name: ")
	datalist.append(cname)

	ClearUser()
	ctype = raw_input("Company Type(Test Lab or Manufacturer): ")
	while validateCompany(ctype) is False:
		ctype = raw_input("Re-enter Company Type(Test Lab or Manufacturer): ")
	datalist.append(ctype)

	ClearUser()
	addr = raw_input("Address: ")
	while validateAddress(addr) is False:
		addr = raw_input("Re-enter Address: ")
	datalist.append(addr)

	ClearUser()
	ophone = raw_input("Office phone number: ")
	while validatePhone(ophone) is False:
		ophone = raw_input("Re-enter Office phone number: ")
	datalist.append(ophone)

	ClearUser()
	cphone = raw_input("Cell phone number: ")
	while validatePhone(cphone) is False:
		cphone = raw_input("Re-enter Cell phone number: ")
	datalist.append(cphone)
	
	ClearUser()
	email = raw_input("Email Address: ")
	while validateEmail(email) is False:
		email = raw_input("Re-enter Email Address: ")
	datalist.append(email)
	
	os.system('clear')
	
	#zip to combine both lists into a dictionary
	return dict(zip(keys, datalist))

	
#The following functions will ultimately get the MDS data and instantiate a product. (first contacat person, then manufacturer, then product)

#instantiate the contact person using the User Class
def createUser(UREG):
	uname = UREG.get('Username')
	pword = UREG.get('Password')
	fname = UREG.get('First Name')
	mname = UREG.get('Middle Name')
	lname = UREG.get('Last Name')	
	addr = UREG.get('Address')
	ophone = UREG.get('Office Phone Number')
	cphone = UREG.get('Cell Phone Number')
	email = UREG.get('Email Address')
	return User(uname, pword, fname, mname, lname, addr, ophone, cphone, email) 

#instantiate the manufacturer contact person
def createManufacturer(MDS, User):
	mname = MDS.get('Manufacturer')
	country = MDS.get('Location')
	return manufacturer(mname, country, User)
	
def createProduct(MDS, man1):
	#instantiate the product
	mnum = MDS.get('Model Number')
	mname = man1.getContact().getFirstName()
	mdate = 'Date'
	length = MDS.get('Module lxw')
	wdh = MDS.get('Module lxw')
	wgt = MDS.get('Module Weight')
	cellarea = MDS.get('Individual Cell Area')
	celltec = MDS.get('Cell Technology')
	numcell = MDS.get('Total number of cells')
	numcellseries = MDS.get('Number of cells in a series')
	numstring = MDS.get('Number of series strings')
	numbypass= MDS.get('Number of bypass diodes')
	fuserating = MDS.get('Series fuse rating')
	intermat = MDS.get('Innterconnect material')
	intersup = MDS.get('Cell Manufacturer')
	suptype= MDS.get('Superstrate Type')
	supman = MDS.get('Superstrate Manufacturer')
	subtype = MDS.get('Substrate Type')
	subman = MDS.get('Substrate Manufacturer')
	framemat = MDS.get('Frame Type')
	frameadh = MDS.get('Frame adhesive')
	entype = MDS.get('Encapsulant Type')
	enman = MDS.get('Encapsulant Manufacturer')
	jbtype = MDS.get('Junction Box Type')
	jbman = MDS.get('Junction box manufacturer')
	jbad = MDS.get('Junction box adhesive')
	cabtype = MDS.get('Cable & Connector type')
	contype = MDS.get('Cable & Connector type')
	maxsys = MDS.get('Maximum system voltage')
	rvoc = MDS.get('voc')
	risc = MDS.get('isc')
	rvmp = MDS.get('vmp')
	rimp = MDS.get('imp')
	rpmp = MDS.get('pmp')
	rff = MDS.get('ff')
	
	return Product(mnum, mname, mdate, length, wdh, wgt, cellarea, celltec, numcell, numcellseries, numstring, numbypass, fuserating, intermat, intersup, suptype, supman, subtype, subman, framemat, frameadh, entype, enman, jbtype, jbman, jbad, cabtype, contype, maxsys, rvoc, risc, rvmp, rimp, rpmp, rff)
		

#function will print product information
def productInformation():
	print "----------Product Information-----------"
	print ""
	print "Manufacturer Name: " + str(pv1.getManufacturer())
	print "Contact Name: " + str(u1.getFirstName())
	print "Contact Email: " + str(u1.getEmail())
	print "Model Number: " + str(pv1.getModelNumber())
	print "Cell Technology: " + str(pv1.getCellTechnology())
	print "System Voltage: " +  str(pv1.getmaxsysvoltage())
	print "Rated Power (PMP): " + str( pv1.getratedpmp())

#function will print baseline test result	
def BaselineTestResults():
	print "----------Baseline Test Results----------"
	print ""
	
	for i in dict_list:
		for key in i:
			if i[key] == 'Baseline':
				test = myClasses.TestResults(i)
				print "Model: " + i['Model']
				print "Test Sequence: " + test.getTestSequence()
				print "Condition:     " + test.getReportingConditon()
				print "Date:          " + test.getTestDate()
				print "Isc:           " + test.getIsc()
				print "Voc:           " + test.getVoc()
				print "Imp:           " + test.getImp()
				print "Vmp:           " + test.getVmp()
				print "FF:            " + test.getFF()
				print "Pmp:           " + test.getPmp()
				print ""
				print "-------------------------------------------------"  
				print ""	

def main():
	print "\n"
	print "*********************WELCOME**********************"
	print ""
	##reg form 
	
	##connnect database
	##populate database
	##close database
	

	UREG = addUser()
	user1 = createUser(UREG)
	MDS = addPV()
	manufacturer1 = createManufacturer(MDS, user1)
	pv1 = createProduct(MDS, manufacturer1)





				
	#data form
	
	
	
	
main()





