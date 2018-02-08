import MySQLdb

class DBModule(object):

	'''
	def __init__(self):
		pass
	'''

	def create_db(self):
		pass

	def connect_db(self, user='root', db='solarPV'):
		con = MySQLdb.connect(user=user, db=db, passwd="root")
		return con

	def create_table(self, sql_str):
		cur.execute(sql_str)
		return cur

	def insert_enrollment(self, tablename, cur, record):

		placeholder = ','.join(['%s'] * len(record))
		columns = ','.join(record.keys())
		query_str = 'INSERT INTO %s (%s) VALUES (%s)' % (tablename, columns, placeholder)
	#print query_str
		cur.execute(query_str, record.values())

	def update_table(self):
		pass

	def delete_row(self):
		pass

	def select_rows(self):
		pass

	def drop_table(self):
		pass

class Manufacturer(object):
	def __init__(self, record, User):
		self._name = record["Name"]
		self._registeredcountry= record["Reigistered Country"]
		self._contactperson = User

	# Defining setters

	def setName(self, name):
		self._name = name

	def setRegisteredCountry(self, rc):
		self._registeredcountry = rc

	def setContactPerson(self, cp):
		self._contactperson = cp

	# Defining getters
	def getName(self, name):
		return self._name

	def getRegisteredCountry(self, rc):
		return self._registeredcountry

	def getContactPerson(self, cp):
		return self._contactperson

	def getAll(self):
		sub = {
				"name":self.getName(), "registeredCountry":self.getRegisteredCountry(), "ContactPerson":self.getContactPerson()\
				
			}  

		return sub

class TestLab(object):
	def __init__(self, record, User):
		self._name = record["Name"]
		self._address = record["Address"]
		self._contactperson = User

	# Defining setters

	def setName(self, name):
		self._name = name

	def setAddress(self, address):
		self._address = address

	def setContactPerson(self, cp):
		self._contactperson = cp

	# Defining getters
	def getName(self, name):
		return self._name

	def getaddress(self, address):
		return self._address

	def getContactPerson(self, cp):
		return self._contactperson

	def getAll(self):
		sub = {
				"name":self.getName(), "address":self.getaddress(), "ContactPerson":self.getContactPerson()\
				
			}  

		return sub
		
class User(object):
	def __init__(self, record):
		self._username = record["Username"]
		self._password = record["Password"]
		self._firstname = record["First Name"]
		self._middlename = record["Middle Name"]
		self._lastname = record["Last Name"]
		self._address = record["Address"]
		self._cellphone = record["Cell Phone"]
		self._officephone = record["Office Phone"]
		self._email = record["Email"]

	# Defining setters

	def setUsername(self, username):
		self._username = username

	def setPassword(self, password):
		self._password = password

	def setFirstName(self, firstname):
		self._firstname = firstname

	def setMiddleName(self, middlename):
		self._middlename = middlename

	def setLastName(self, lastname):
		self._lastname = lastname

	def setAddress(self, address):
		self._address = address

	def setCellPhone(self, cellphone):
		self._cellphone = cellphone

	def setOfficePhone(self, officephone):
		self._officephone = officephone

	def setemail(self, email):
		self._email = email


	# Defining getters

	def getUsername(self):
		return self._username

	def getPassword(self):
		return self._password

	def getFirstName(self):
		return self._firstname

	def getMiddleName(self):
		return self._middlename

	def getLastName(self):
		return self._lastname

	def getAddress(self):
		return self._address

	def getCellPhone(self):
		return self._cellphone
	
	def getOfficePhone(self):
		return self._officephone

	def getEmail(self):
		return self._email

	def getAll(self):
		sub = {
				"username":self.getUsername(), "password":self.getPassword(), "firstname":self.getFirstName(),\
				"middlename":self.getMiddleName(), "lastname":self.getLastName(), "address":self.getAddress(),\
				"cellphone":self.getCellPhone(),"officephone":self.getOfficePhone(), "email":self.getEmail()\
			}  

		return sub

class Product(object):
	def __init__(self, record, Manufacturer):
		self._modelnumber = record["Model Number"]
		self._manufacturer = Manufacturer
		self._manufacturingdate = record["Manufacturer Date"]
		self._length = record["Length"]
		self._width = record["Width"]
		self._weight = record["Weight"]
		self._cellarea = record["Cell Area"]
		self._celltechnology = record["Cell Technology"]
		self._totalnumberofcells = record["Total Number of Cells"]
		self._numberofCellsinaSeries = record["Number of Cells in a Series"]
		self._numberofSeriesStrings = record["Number of Series Strings"]
		self._numberofbypassdiodes = record["Number of Bypass Diodes"]
		self._seriesfuserating = record["Series Fuse Rating"]
		self._interconnectmaterial = record["Interconnect Material"]		
		self._interconnectsupplier = record["Interconnect Supplier"]
		self._superstratetype= record["SuperstrateType"]
		self._superstratemanufacturer = record["Superstrate Manufacturer"]		
		self._junctionboxtype = record["Junction Box Type"]
		self._junctionboxmanufacturer = record["Junction Box Manufacturer"]
		self._junctionboxadhesive = record["Junction Box Adhesive"]
		self._cabletype = record["Cable Type"]
		self._connnectortype = record["Connector Type"]
		self._maxsysvoltage = record["Maximum System Voltage"]
		self._ratedvoc = record["Rated VOC"]
		self._ratedisc = record["Rated ISC"]
		self._ratedvmp = record["Rated VMP"]
		self._ratedimp = record["Rated IMP"]
		self._ratedpmp = record["Rated PMP"]
		self._ratedff = record["Rated FF"]
		
	# Defining setters

	def setModelNumber(self, modelnumber):
		self._modelnumber = modelnumber

	def setManufacturer(self, manufacturer):
		self._manufacturer = manufacturer

	def setManufacturingDate(self, mdate):
		self._manufacturingdate = mdate
		
	def setLength(self, length):
		self._length = length

	def setWidth(self, width):
		self._width = width

	def setWeight(self, weight):
		self._weight = weight

	def setCellArea(self, cellarea):
		self._cellarea = cellarea

	def setCellTechnology(self, celltechnology):
		self._celltechnology = celltechnology

	def setTotalNumberofCells(self, totalnumberofcells):
		self._totalnumberofcells = totalnumberofcells

	def	setCellsinSeries(self, numberofCellsinaSeries):
		self._numberofCellsinaSeries = numberofCellsinaSeries
	
	def setSeriesStrings(self, numberofSeriesStrings):
		self._numberofSeriesStrings = numberofSeriesStrings

	def setnumberofbypassdiodes(self,bypassdiodes):
		self._numberofbypassdiodes = bypassdiodes

	def setseriesfuserating(self, seriesfuserating):
		self._seriesfuserating = seriesfuserating

	def	setinterconnectmaterial(self, interconnectmaterial):
		self._interconnectmaterial = interconnectmaterial
	
	def setinterconnectsupplier(self, interconnectsupplier):
		self._interconnectsupplier = interconnectsupplier
		
	def	setsuperstratetype(self, superstratetype):
		self._superstratetype = superstratetype
	
	def setsuperstratemanufacturer(self, superstratemanufacturer):
		self._superstratemanufacturer = superstratemanufacturer

	def setjunctionboxtype(self, junctionboxtype):
		self._junctionboxtype = junctionboxtype

	def setjunctionboxmanufacturer(self, junctionboxmanufacturer):
		self._junctionboxmanufacturer = junctionboxmanufacturer

	def	setjunctionboxadhesive(self, junctionboxadhesive):
		self._junctionboxadhesive = junctionboxadhesive
	
	def cabletype(self, cabletype):
		self._cabletype = cabletype

	def setconnnectortype(self, connnectortype):
		self._connnectortype = connnectortype

	def setmaxsysvoltage(self, maxsysvoltage):
		self._maxsysvoltage = maxsysvoltage

	def	setratedvoc(self, ratedvoc):
		self._ratedvoc = ratedvoc
	
	def setratedisc(self, ratedisc):
		self._ratedisc = ratedisc

	def setratedvmp (self, ratedvmp ):
		self._ratedvmp  = ratedvmp 

	def	setratedimp(self, ratedimp):
		self._ratedimp = ratedimp
	
	def	setratedpmp(self, ratedpmp):
		self._ratedpmp = ratedpmp
	
	def setratedff(self, ratedff):
		self._ratedff = ratedff

	
	
		
	# Defining getters

	def getModelNumber(self):
		return self._modelnumber

	def getManufacturer(self):
		return self._manufacturer

	def getManufacturingDate(self):
		return self._manufacturingdate
		
	def getLength(self, length):
		return self._length 

	def getWidth(self, width):
		return self._width 

	def getWeight(self, weight):
		return self._weight 

	def getCellArea(self, cellarea):
		return self._cellarea

	def getCellTechnology(self, celltechnology):
		return self._celltechnology

	def getTotalNumberofCells(self, totalnumberofcells):
		return self._totalnumberofcells 

	def	getCellsinSeries(self, numberofCellsinaSeries):
		return self._numberofCellsinaSeries 
	
	def getSeriesStrings(self, numberofSeriesStrings):
		return self._numberofSeriesStrings 

	def getnumberofbypassdiodes(self,bypassdiodes):
		return self._numberofbypassdiodes 

	def getseriesfuserating(self, seriesfuserating):
		return self._seriesfuserating 

	def	getinterconnectmaterial(self, interconnectmaterial):
		return self._interconnectmaterial 
	
	def getinterconnectsupplier(self, interconnectsupplier):
		return self._interconnectsupplier 
		
	def	getsuperstratetype(self, superstratetype):
		return self._superstratetype 
	
	def getsuperstratemanufacturer(self, superstratemanufacturer):
		return self._superstratemanufacturer

	def getjunctionboxtype(self, junctionboxtype):
		return self._junctionboxtype 

	def getjunctionboxmanufacturer(self, junctionboxmanufacturer):
		return self._junctionboxmanufacturer 

	def	getjunctionboxadhesive(self, junctionboxadhesive):
		return self._junctionboxadhesive 
	
	def getcabletype(self, cabletype):
		return self._cabletype 
		
	def getconnnectortype(self, connnectortype):
		return self._connnectortype 

	def getmaxsysvoltage(self, maxsysvoltage):
		return self._maxsysvoltage

	def	getratedvoc(self, ratedvoc):
		return self._ratedvoc
	
	def getratedisc(self, ratedisc):
		return self._ratedisc

	def getratedvmp (self, ratedvmp ):
		return self._ratedvmp  

	def	getratedimp(self, ratedimp):
		return self._ratedimp 
	
	def	getratedpmp(self, ratedpmp):
		return self._ratedpmp
	
	def getratedff(self, ratedff):
		return self._ratedff 

	def getAll(self):
		sub = {"modelNumber": self.getModelNumber(), "manufacturer": self.getManufacturer(), "manufacturingDate":self.manufacturingDate(),\
				"length":self.length(),"width":self.getWidth(), "weight":self.getWieght(), "cellarea":self.getCellArea(),\
				"celltechnology":self.getCellTechnology(),"totalnumberofcells":self.getTotalNumberofCells(), "cellsinseries":self.getCellsinSeries(),\
				"numberofSeriesStrings":self.getSeriesStrings(), "bypassdiodes":self.getnumberofbypassdiodes(), "seriesfuserating":self.getseriesfuserating(),\
				"interconnectmaterial":self.getinterconnectmaterial(),"interconnectsupplier":self.getinterconnectsupplier(), "superstratetype":self.getsuperstratetype(),\
				"superstratemanufacturer":self.getsuperstratemanufacturer(), "junctionboxtype":self.getjunctionboxtype(), "junctionboxmanufacturer":self.getjunctionboxmanufacturer(),\
				"junctionboxadhesive":self.getjunctionboxadhesive(),"cabletype":self.getcabletype(), "connnectortype":self.getconnnectortype(), "maxsysvoltage":self.getmaxsysvoltage(),\
				"ratedvoc":self.getratedvoc(), "ratedisc":self.getratedisc(),"ratedvmp":self.getratedvmp(), "ratedimp":self.getratedimp(), "ratedpmp":self.getratedpmp(),\
				"ratedff":self.getratedff()\
			}  

		return sub		
		
class TestResults(object):
	def __init__(self, TestLab, Product, record):
		self._datasource = TestLab
		self._product = Product
		self._reportingcondition = ["Reporting Condition"]
		self._testsequence = record["Test Sequence"]
		self._testdate = record["Test Date"]
		self._isc = record["ISC"]
		self._voc = record["VOC"]
		self._imp = record["IMP"]
		self._vmp = record["VMP"]
		self._pmp = record["PMP"]
		self._ff = record["FF"]
		self._noct = record["NOCT"]
	# Defining setters
	def setdataSource(self, TestLab):
		self._datasource = TestLab

	def setproduct(self, Product):
		self._product = Product

	def setreportingCondition(self, rc):
		self._reportingcondition = rc

	def setTestSequence(self, ts):
		self._testsequence = ts

	def setTestDate(self, testdate):
		self._testdate = testdate

	def setISC(self, isc):
		self._isc = isc

	def setVOC(self, voc):
		self._voc = voc

	def setIMP(self, imp):
		self._imp = imp
		
	def setVMP(self, vmp):
		self._vmp = vmp

	def setPMP(self, pmp):
		self._pmp = pmp

	def setFF(self, ff):
		self._ff = ff

	def setNOCT(self, noct):
		self._noct = noct

	# Defining getters

	def getdataSource(self):
		return self._datasource

	def getproduct(self):
		return self._product

	def getreportingCondition(self):
		return self._reportingcondition

	def getTestSequence(self):
		return self._testsequence

	def getTestDate(self):
		return self._testdate

	def getISC(self):
		return self._isc

	def getVOC(self):
		return self._voc

	def getIMP(self):
		return self._imp
		
	def getVMP(self):
		return self._vmp

	def getPMP(self):
		return self._pmp

	def getFF(self):
		return self._ff

	def getNOCT(self):
		return self._noct

	def getAll(self):
		sub = {"dataSource": self.getDatasource(), "product": self.getproduct(), "reportingCondition":self.reportingCondition(),\
				"TestSequence":self.getTestSequence(),"TestDate":self.getTestDate(), "ISC":self.getISC(), "VOC":self.getVOC(),\
				"IMP":self.getIMP(),"VMP":self.VMP(), "PMP":self.getPMP(), "FF":self.getFF(), "NOCT":self.getNOCT()\
				}  

		return sub