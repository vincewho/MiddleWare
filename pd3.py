#!/usr/bin/env python2.7

import csv
import sys
from collections import defaultdict
import os #use os.system('clear') to clear terminal
import datetime

import the classes
from myClasses import manufacturer 
from myClasses import Product

def createDict(csv_file):
	lab_dict = defaultdict(list)

	filein=open(csv_file, 'r')
	data=csv.DictReader(filein, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

	return data

csv_file = 'test_results.csv'
data = createDict(csv_file)
csv_dict = [row for row in data]

#To see the list, uncomment the line below:
#print csv_dict

#this function gets input from maufacturer and returns the data in a  dictionary
def addPV():	
	#list of input fields
	keys = ['Manufacturer', 'Location', 'Contact','Address','Email', 'Phone', 'Model Number', 'Module lxw', 'Module Weight', 'Individual Cell Area', 'Cell technology','Cell Manufacturer','Cell Manufactureing Location','Total number of cells', 'Number of cells in a series','Number of series strings','Number of bypass diodes', 'Bypass diode rating', 'Bypass diode max junct temp', 'Series fuse rating', 'Innterconnect material', 'Interconnect dimensions', 'Superstrate type', 'Superstrate Manufacturer', 'Substrate Type', 'Substrate Manufacturer', 'FrameType' ,'Frame adhesive', 'Encapsulant Type','Encapsulant Manufacturer', 'Junction Box Type', 'Junction box manufacturer', 'Junction box potting material', 'Junction box adhesive', 'Junction Box Use Intention', 'Cable & Connector type', 'Maximum system voltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff' ]
	#empty list which will hold user input
	datalist = []
	
	man = raw_input("Manufacturer: ")
	datalist.append(man)
	
	loc = raw_input("Location: ")
	datalist.append(loc)

	cont = raw_input("Contact: ")
	datalist.append(cont)

	addr = raw_input("Address: ")
	datalist.append(addr)

	email = raw_input("Email: ")
	datalist.append(email)

	phone = raw_input("Phone: ")
	datalist.append(phone)

	mnum = raw_input("Model Number: ")
	datalist.append(mnum)

	mlxw = raw_input("Module total length x width (cmxcm): ")
	datalist.append(mlxw)

	mwgt = raw_input("Module weight(kg): ")
	datalist.append(mwgt)

	icarea = raw_input("Individual Cell Area(cm^2): ")
	datalist.append(icarea)
	
	ctech = raw_input ("Cell Technology: ")
	datalist.append(ctech)
	
	cmanpt = raw_input("Cell Manufacturer and Part#: ")
	datalist.append(cmanpt)

	cmanloc = raw_input("Cell Manufacturing Location: ")
	datalist.append(cmanloc)

	totcell = raw_input("Total number of cells: ")
	datalist.append(totcell)

	cseries = raw_input("Number of cells in series: ")
	datalist.append(cseries)

	serstg = raw_input("Number of series strings: ")
	datalist.append(serstg)

	bydid = raw_input("Number of bypass diodes: ")
	datalist.append(bydid)

	bdrateA = raw_input("Bypass diode rating(A): ")
	datalist.append(bdrateA)

	juntemp = raw_input("Bypass diode max junction temp(C): ")
	datalist.append(juntemp)

	sfratingA = raw_input("Series Fuse Rating(A): ")
	datalist.append(sfratingA)

	matsup = raw_input("Interconnect material and supplier model no.: ")
	datalist.append(matsup)

	dimen = raw_input("Interconnect dimensions(mm x mm): ")
	datalist.append(dimen)

	suptype = raw_input("Superstrate Type: ")
	datalist.append(suptype)
	
	supmanpt = raw_input("Superstrate Manfacturer and part#: ")
	datalist.append(supmanpt)

	subtype = raw_input("Substrate Type: ")
	datalist.append(subtype)

	submanpt = raw_input("Substrate Manufacturer and part#: ")
	datalist.append(submanpt)

	frametype = raw_input("Frame Type and Material: ")
	datalist.append(frametype)

	framead = raw_input("Frame adhesive: ")
	datalist.append(framead)

	encaptype = raw_input("Encapsulant Type: ")
	datalist.append(encaptype)

	encapmanpt = raw_input("Encapsulant Manufacturer and part#: ")
	datalist.append(encapmanpt)

	junboxtype = raw_input("Junction box type: ")
	datalist.append(junboxtype)

	junboxmanpt = raw_input("Junction box manufacturer and part#: ")
	datalist.append(junboxmanpt)

	junboxpot = raw_input("Junction box potting material, if any: ")
	datalist.append(junboxpot)

	junboxadh = raw_input("Junction box adhesive: ")
	datalist.append(junboxadh)

	junboxuse = raw_input("Is junction box intended for use with Conduit?: ")
	datalist.append(junboxuse)

	cabcontype = raw_input("Cable & Connector Type: ")
	datalist.append(cabcontype)

	maxsysvol = raw_input("Max system voltage(V): ")
	datalist.append(maxsysvol)

	voc = raw_input("Voc(V): ")
	datalist.append(voc)

	isc = raw_input("Isc(A): ")
	datalist.append(isc)

	vmp = raw_input("Vmp(V): ")
	datalist.append(vmp)

	imp = raw_input("Imp(A): ")
	datalist.append(imp)

	pmp = raw_input("Pmp(W): ")
	datalist.append(pmp)

	ff = raw_input("FF(%): ")
	datalist.append(ff)

	#zip to combine both lists into a dictionary
	return dict(zip(keys, datalist))

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

	
#this function will get the MDS data and instantiate a product. 
#(first contacat person, then manufacturer, then product)

def main():

	MDS = addPV()
	
	#instantiate the contact person
	c = MDS.get('Contact')
	e = MDS.get('Email')
	p = MDS.get('Phone')
	manufacturer.addContact(c,e,p)
	contact = manufacturer.getContact()
	
	#instantiate the Manfacturer
	mname = MDS.get('Manufacturer')
	country = MDS.get('Location')
	man1 = manufacturer(mname, country, contact)
	
	#to use datetime function
	i = datetime.datetime.now()
	
	#instantiate the product
	mnum = MDS.get('Model Number')
	mname = MDS.get('Manfacturer')
	mdate = "%s/%s/%s" % (i.day, i.month, i.year) )
	length = MDS.get('Module lxw')
	length = length.split('x')[0]
	wdh = MDS.get('Module lxw')
	wdh = length.split('x')[1]
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
	
	pv1 = Product(mnum, man1, mdate, length, wdh, wgt, cellarea, celltec, numcell, numcellseries, numstring, numbypass, fuserating, intermat, intersup, suptype, supman, subtype, subman, framemat, frameadh, entype, enman, jbtype, jbman, jbad, cabtype, contype, maxsys, rvoc, risc, rvmp, rimp, rpmp, rff)
	
	print "-----Product Information-----"
	print ""
	print "Manufacturer Name: " + pv1.getManufacturer()
	print "Contact Name: " + contact[0] 
	print "Contact Email: " + contact[1]
	print "Model Number: " + pv1.getModelNumber()
	print "Cell Technology: " + pv1.getCellTechnology()
	print "System Voltage: " +  pv1.getmaxsysvoltage()
	print "Rated Power (PMP): " pv1.getratedpmp()

main()