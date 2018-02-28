class manufacturer(object):

    def __init__(self, name = 'default', country = 'US', contact = []):
        self.__name = name
        self.__registerCountry = country
        self.__contact_person = contact

    def getName(self):
        return self.__name

    def setName(self,n):
        self.__name = name

    def getCountry(self):
        return self.__registerCountry

    def setCountry(self, c):
        self.__registerCountry = c

    def getContact(self):
        return self.__contact_person

    def addContact(self, newcontact):
        self.__contact_person.extend(newcontact)

###### This is the user object ######
class User(object):
	def __init__(self, uname='user1', passwd='null', fname='Dr.', mname='Kutiche', lname='Usha', addy='666 Place Pl.', officeNum='1', cellNum='6666666666', email='KU@asu.edu'):
		self.__username = uname
		self.__password = passwd
		self.__firstname = fname
		self.__middlename = mname
		self.__lastname = lname
		self.__address = addy
		self.__officephone = officeNum
		self.__cellphone = cellNum
		self.__email = email

	# Defining setters

	def setUsername(self, var1):
	    self.__username = var1

	def setPassword(self, var2):
		self.__password = var2

	def setFirstName(self, var3):
		self.__firstname = var3

	def setMiddleName(self, var4):
		self.__middlename = var4

	def setLastName(self, var5):
		self.__lastname = var5

	def setAddress(self, var6):
		self.__address = var6

	def setCellPhone(self, var7):
		self.__cellphone = var7

	def setOfficePhone(self, var8):
		self.__officephone = var8

	def setemail(self, var9):
		self.__email = var9


	# Defining getters

	def getUsername(self):
		return self.__username

	def getPassword(self):
		return self.__password

	def getFirstName(self):
		return self.__firstname

	def getMiddleName(self):
		return self.__middlename

	def getLastName(self):
		return self.__lastname

	def getAddress(self):
		return self.__address

	def getCellPhone(self):
		return self.__cellphone

	def getOfficePhone(self):
		return self.__officephone

	def getEmail(self):
		return self.__email

	def getAll(self):
		sub = {
				"username":self.getUsername(), "password":self.getPassword(), "firstname":self.getFirstName(),\
				"middlename":self.getMiddleName(), "lastname":self.getLastName(), "address":self.getAddress(),\
				"cellphone":self.getCellPhone(),"officephone":self.getOfficePhone(), "email":self.getEmail()\
			}
		return sub


###### This is the testlab object ######
class TestLab(object):
	def __init__(self, name='testlab', addy='123 Hello Wr', contact=[]):
		self.__name = name
		self.__addy = addy
		self.__contact = contact

	# Defining setters

	def setName(self, var1):
		self.__name = var1

	def setAddress(self, var2):
		self.__address = var2

	def setContactPerson(self, var3):
		self.__contactperson = var3

	# Defining getters
	def getName(self):
		return self.__name

	def getAddress(self):
		return self.__addy

	def getContactPerson(self):
		return self.__contact

	def getAll(self):
		sub = {
				"name":self.getName(), "address":self.getAddress(), "ContactPerson":self.getContactPerson()
		}

		return sub

###### This is the Product object ######
class Product(object):
	def __init__(self, modelNum, manu, manuDate, length, width, weight, cellArea, cellTech, totalNumCell, numCellSeries, numSeriesString, numBypassDiodes, seriesFuseRating, interconnectMat, interconnectSupp, superstrateType, superstrateManu, substrateType, substrateManu, frameMaterial, frameAdhesive, encapType, encapManu, junctionBoxType, junctionBoxManu, junctionBoxAdhesive, cableType, connectorType, maxSysVoltage, voc, isc, vmp, imp, pmp, ff):
		self.__modelnumber = modelNum
		self.__manufacturer = manu
		self.__manufacturingdate = manuDate
		self.__length = length
		self.__width = width
		self.__weight = weight
		self.__cellarea = cellArea
		self.__celltechnology = cellTech
		self.__totalnumberofcells = totalNumCell
		self.__numberofCellsinaSeries =  numCellSeries
		self.__numberofSeriesStrings =  numSeriesString
		self.__numberofbypassdiodes =  numBypassDiodes
		self.__seriesfuserating =  seriesFuseRating
		self.__interconnectmaterial = interconnectMat
		self.__interconnectsupplier = interconnectSupp
		self.__superstratetype = superstrateType
		self.__superstratemanufacturer = superstrateManu
		self.__junctionboxtype =  junctionBoxType
		self.__junctionboxmanufacturer =  junctionBoxManu
		self.__junctionboxadhesive =  junctionBoxAdhesive
		self.__cabletype = cableType
		self.__connnectortype = connectorType
		self.__maxsysvoltage =  maxSysVoltage
		self.__ratedvoc = voc
		self.__ratedisc = isc
		self.__ratedvmp = vmp
		self.__ratedimp = imp
		self.__ratedpmp = pmp
		self.__ratedff = ff

################## Defining setters

	def setModelNumber(self, var1):
		self.__modelnumber = var1

	def setManufacturer(self, var2):
		self.__manufacturer = var2

	def setManufacturingDate(self, var3):
		self.__manufacturingdate = var3

	def setLength(self, var4):
		self.__length = var4

	def setWidth(self, var5):
		self.__width = var5

	def setWeight(self, var6):
		self.__weight = var6

	def setCellArea(self, var7):
		self.__cellarea = var7

	def setCellTechnology(self, var8):
		self.__celltechnology = var8

	def setTotalNumberofCells(self, var9):
		self.__totalnumberofcells = var9

	def	setCellsinSeries(self, var10):
		self.__numberofCellsinaSeries = var10

	def setSeriesStrings(self, var11):
		self.__numberofSeriesStrings = var11

	def setnumberofbypassdiodes(self,var12):
		self.__numberofbypassdiodes = var12

	def setseriesfuserating(self, var13):
		self.__seriesfuserating = var13

	def	setinterconnectmaterial(self, var14):
		self.__interconnectmaterial = var14

	def setinterconnectsupplier(self, var15):
		self.__interconnectsupplier = var15

	def	setsuperstratetype(self, var16):
		self.__superstratetype = var16

	def setsuperstratemanufacturer(self, var17):
		self.__superstratemanufacturer = var17

	def setjunctionboxtype(self, var18):
		self.__junctionboxtype = var18

	def setjunctionboxmanufacturer(self, var19):
		self.__junctionboxmanufacturer = var19

	def	setjunctionboxadhesive(self, var20):
		self.__junctionboxadhesive = var20

	def cabletype(self, var21):
		self.__cabletype = var21

	def setconnnectortype(self, var22):
		self.__connnectortype = var22

	def setmaxsysvoltage(self, var23):
		self.__maxsysvoltage = var23

	def	setratedvoc(self, var24):
		self.__ratedvoc = var24

	def setratedisc(self, var25):
		self.__ratedisc = var25

	def setratedvmp (self, var26):
		self.__ratedvmp  = var26

	def	setratedimp(self, var27):
		self.__ratedimp = var27

	def	setratedpmp(self, var28):
		self.__ratedpmp = var28

	def setratedff(self, var29):
		self.__ratedff = var29

################## Defining getters

	def getModelNumber(self):
		return self.__modelnumber

	def getManufacturer(self):
		return self.__manufacturer

	def getManufacturingDate(self):
		return self.__manufacturingdate

	def getLength(self):
		return self.__length

	def getWidth(self):
		return self.__width

	def getWeight(self):
		return self.__weight

	def getCellArea(self):
		return self.__cellarea

	def getCellTechnology(self):
		return self.__celltechnology

	def getTotalNumberofCells(self):
		return self.__totalnumberofcells

	def	getCellsinSeries(self):
		return self.__numberofCellsinaSeries

	def getSeriesStrings(self):
		return self.__numberofSeriesStrings

	def getnumberofbypassdiodes(self,bypassdiodes):
		return self.__numberofbypassdiodes

	def getseriesfuserating(self):
		return self.__seriesfuserating

	def	getinterconnectmaterial(self):
		return self.__interconnectmaterial

	def getinterconnectsupplier(self):
		return self.__interconnectsupplier

	def	getsuperstratetype(self):
		return self.__superstratetype

	def getsuperstratemanufacturer(self):
		return self.__superstratemanufacturer

	def getjunctionboxtype(self):
		return self.__junctionboxtype

	def getjunctionboxmanufacturer(self):
		return self.__junctionboxmanufacturer

	def	getjunctionboxadhesive(self):
		return self.__junctionboxadhesive

	def getcabletype(self):
		return self.__cabletype

	def getconnnectortype(self):
		return self.__connnectortype

	def getmaxsysvoltage(self):
		return self.__maxsysvoltage

	def	getratedvoc(self):
		return self.__ratedvoc

	def getratedisc(self):
		return self.__ratedisc

	def getratedvmp (self):
		return self.__ratedvmp

	def	getratedimp(self):
		return self.__ratedimp

	def	getratedpmp(self):
		return self.__ratedpmp

	def getratedff(self):
		return self.__ratedff

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
	def __init__(self,record, dataSource="Test Lab", noct=0):
		self.__dataSource = dataSource
		self.__product = record["Model"]
		self.__reportingCondition = record["Condition"]
		self.__testSequence = record["Test Sequence"]
		self.__testDate = record["Date"]
		self.__isc = record["Isc"]
		self.__voc = record["Voc"]
		self.__imp = record["Imp"]
		self.__vmp = record["Vmp"] 
		self.__pmp = record["Pmp"]
		self.__ff = record["FF"]
		self.__noct = noct

	# Defining setters

	def setDataSource(self, dataSource):
		self.__dataSource = dataSource

	def setProduct(self, product):
		self.__product = product

	def setReportingConditon(self, reportingCondition):
		self.__reportingCondition = reportingCondition

	def setTestSequence(self, testSequence):
		self.__testSequence = testSequence

	def setTestDate(self, testDate):
		self.__testDate = testDate

	def setIsc(self, isc):
		self.__isc = isc

	def setVoc(self, voc):
		self.__voc = voc

	def setImp(self, imp):
		self.__imp = imp

	def setVmp(self, vmp):
		self.__vmp = vmp

	def setPmp(self, vmp):
		self.__vmp = vmp

	def setFF(self, ff):
		self.__ff = ff

	def setNoct(self, noct):
		self.__noct = noct

	# Define Getters

	def getDataSource(self):
		return self.__dataSource

	def getProduct(self):
		return self.__product

	def getReportingConditon(self):
		return self.__reportingCondition

	def getTestSequence(self):
		return self.__testSequence

	def getTestDate(self):
		return self.__testDate

	def getIsc(self):
		return self.__isc

	def getVoc(self):
		return self.__voc

	def getImp(self):
		return self.__imp

	def getVmp(self):
		return self.__vmp

	def getPmp(self):
		return self.__vmp

	def getFF(self):
		return self.__ff

	def getNoct(self):
		return self.__noct

	def getAll(self):
		sub = {
			"product":self.getProduct(), "reporting":self.getReportingCondition(),
			"testSequence":self.getTestSequence(), "testDate":getTestDate(),
			"isc":self.getIsc(), "voc":self.getVoc(),"Imp":self.getImp(),
			"Vmp":self.getVmp(), "pmp":self.getPmp(), "ff":self.getFF(), "noct":self.getNoct()
		}
		return sub		
####################################################################################

manu1 = manufacturer('James Boa')
