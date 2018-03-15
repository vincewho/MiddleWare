DROP database mw;
Create database mw;
use mw;

CREATE TABLE IF NOT EXISTS Manufacturer(
	Manu_name varchar(40), 
    registered_country varchar(40), 
    PRIMARY KEY (Manu_name));

CREATE TABLE IF NOT EXISTS User(
	username varchar(40),
	password varchar(40),
	fname varchar(40),
	mname varchar (40),
	lname varchar (40),
	address varchar (40),
	officePhone varchar (12),
	cellphone varchar (12),
	email varchar (40));
    
CREATE TABLE IF NOT EXISTS testlab(
	Lab_name varchar(40) NOT NULL, 
    address varchar(40), 
	PRIMARY KEY (Lab_name));

CREATE TABLE IF NOT EXISTS test_results(
    Lab_name varchar(40), 
    Test_date date, 
    reportingCondition varchar(40), 
    NOCT float, 
    ISC float, 
    VOC float, 
    PMP float, 
    FF float, 
    VMP float, 
    IMP float, 
    FOREIGN KEY (Lab_name) REFERENCES testlab(Lab_name)
    );

CREATE TABLE IF NOT EXISTS Product(
    ManufacturedDate date, 
	modelNumber varchar(40) NOT NULL, 
    Length float, 
    Width float, 
    Weight float, 
    Cell_Area float, 
    Cell_Technology varchar(40), 
    Total_num_cell int, 
    Num_of_cell_series int,
    Num_of_series int, 
    Num_of_diodes int, 
    Series_fuse_rating float, 
    Interconnect_material varchar(40), 
    Interconnect_supplier varchar(40), 
    Superstrate_type varchar(40), 
    Superstrate_manu varchar(40), 
    Substrate_type varchar(40), 
    Substrate_manu varchar(40), 
    Frame_material varchar(40), 
    Frame_adhesive varchar(40), 
    Encapulant_type varchar(40),
    Encapsulant_manu varchar(40), 
    Junction_box_type varchar(40), 
    Junction_box_manu varchar(40), 
    Junction_box_adhesive varchar(40), 
    Cable_type varchar(40), 
    Connector_type varchar(40),
    Max_system_voltage float, 
    ISC float, 
    VOC float, 
    IMP float, 
    VMP float, 
    FF float, 
    PMP float,
    PRIMARY KEY(modelNumber)
);