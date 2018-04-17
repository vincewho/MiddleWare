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
        return "Name: %s has Username: %s" % (self.fname, self.username)


class TestLab(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Name: %s, Address: %s, Contact: %s" % (self.name, self.address, self.contact)


class Manufacturer(models.Model):
    # countryChoice = (('usa', 'USA'),('france','France'))
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Manufacturer: %s, Country: %s, Contact: %s" % (self.name, self.country, self.contact)


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
        return "Model Number: %s" % (self.model_number)


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
        return "Condition %s" % (self.reportCondition)
