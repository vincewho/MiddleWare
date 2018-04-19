from django.db import models

# Create your models here.


class User(models.Model):
    # these names are the columns
    username = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    address = models.TextField()
    officenum = models.CharField(max_length=15)
    cellnum = models.CharField(max_length=15)
    email = models.EmailField()
	
	def __str__(self):
		return ("Username: %s, First Name: %s, Mididle Name: %s, Last Name: %s, Address: %s, Office Number: %s, Cell Number: %s, Email: %s " % (self.username, self.fname, self.mname, self.lname, self.address, self.officenum, self.cellnum, self.email))


class TestLab(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
		return "Name: %s, Address: %s, Contact: %s" % (self.name, self.address, self.contact)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return "Name: %s, Country: %s, Contact: %s" % (self.name, self.country, self.contact)

class Product(models.Model):
    model_number             = models.CharField(max_length=20)
    manufacturing_date       = models.DateField()
    length                   = models.DecimalField(max_digits=10, decimal_places=2)
    width                    = models.DecimalField(max_digits=10, decimal_places=2)
    weight                   = models.DecimalField(max_digits=10, decimal_places=2)
    cellarea                 = models.DecimalField(max_digits=10, decimal_places=2)
    cell_technology          = models.CharField(max_length=20)
    num_of_cells             = models.IntegerField()
    num_of_cells_in_series   = models.IntegerField()
    num_of_series_strings    = models.IntegerField()
    num_of_diodes            = models.IntegerField()
    series_fuse_rating       = models.DecimalField(max_digits=10, decimal_places=2)
    interconnect_material    = models.CharField(max_length=20)
    interconnect_supplier    = models.CharField(max_length=20)
    superstrate_type         = models.CharField(max_length=20)
    superstrate_manufacturer = models.CharField(max_length=20)
    substrate_type           = models.CharField(max_length=20)
    substrate_manufacturer   = models.CharField(max_length=20)
    frame_material           = models.CharField(max_length=20)
    encapsulant_type         = models.CharField(max_length=20)
    encapsulant_manufacturer = models.CharField(max_length=20)
    max_sys_volt             = models.DecimalField(max_digits=10, decimal_places=2)
    rated_isc                = models.DecimalField(max_digits=10, decimal_places=2)
    rated_voc                = models.DecimalField(max_digits=10, decimal_places=2)
    rated_imp                = models.DecimalField(max_digits=10, decimal_places=2)
    rated_vmp                = models.DecimalField(max_digits=10, decimal_places=2)
    rated_pmp                = models.DecimalField(max_digits=10, decimal_places=2)
    rated_ff                 = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer             = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	
	def __str__(self):
		return "ModelNo: %s, Manufacturing Date: %s, Length: %s, Width: %s, Weight: %s, CellArea: %s, CellTechnology: %s, NumofCells: %s, NumofCellsinSeries: %s, NumofCellsinStrings: %s, NumofDiodes: %s, SeriesFuseRating: %s , Interconnect Material: %s, Interconnect Supplier: %s, Superstrate type: %s, Superstrate Manufacturer: %s, Substrate Type: %s, Substrate Manufacturer %s, Frame Material: %s, Encapsulant Type %s, Encapsulant Manufacturer: %s,  Max System Voltage: %s, rated isc : %s, rated voc: %s, rated imp: %s, rated vmp %s, rated pmp: %s, rated ff %s, manufacturer %s" % (self.model_number, self.manufacturing_date, self.length, self.width, self.cellarea, self.cell_technology, self.num_of_cells, self.num_of_cells_in_series, self.num_of_cells_in_strings, self.num_of_diodes , self.series_fuse_rating, self.interconnect_material, self. interconnect_supplier, self.superstrate_type, self.superstrate_manufacturer, self.substrate_type, self.substrate_manufacturer, self.frame_material, self.encapsulant_type, self.encapsulant_manufacturer, self.max_sys_volt , self.rated_isc, self.rated_voc, self.rated_imp, self.rated_vmp, self.rated_pmp, self.rated_ff, self.manufacturer )

class TestResult(models.Model):
    reportCondition = models.CharField(max_length=100)
    test_sequence = models.CharField(max_length=100)
    test_date = models.DateField()
    isc  = models.DecimalField(max_digits=10, decimal_places=2)
    voc  = models.DecimalField(max_digits=10, decimal_places=2)
    imp  = models.DecimalField(max_digits=10, decimal_places=2)
    vmp  = models.DecimalField(max_digits=10, decimal_places=2)
    pmp  = models.DecimalField(max_digits=10, decimal_places=2)
    ff   = models.DecimalField(max_digits=10, decimal_places=2)
    noct = models.DecimalField(max_digits=10, decimal_places=2)
    data_source = models.ForeignKey(TestLab, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
	
	def __str__(self):
		return "Report Condition: %s, Test Sequence: %s, Test Date: %s, ISC: %s, VOC: %s, IMP: %s, VMP: %s, PMP: %s, FF: %s, NOCT: %s, Data Source: %s, Product: %s" % (self.reportCondition, self.test_sequence, self.test_date, self.isc, self.voc, self.imp, self.vmp, self.pmp, self.ff, self.noct, self.data_source, self.product)