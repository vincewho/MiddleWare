DROP DATABASE IF EXISTS
	Middleware;

CREATE DATABASE MiddleWare;
GO
USE Middleware;

DROP TABLE IF EXISTS
	Manufacturer;
CREATE TABLE Manufacturer(
	Manu_name varchar(20), Contact_email varchar(20), Contact_address varchar(20), Contact_Office_nume varchar(20),
    PRIMARY KEY (Manu_name));

DROP TABLE IF EXISTS
	PVModule;    
CREATE TABLE PVModule(
	Module_number varchar(40) NOT NULL, Length int, Width int, Weight varchar(20), Cell_Area varchar(20), Cell_Technology varchar(20), Total_num_cell int, Num_of_cell_series int,
    Num_of_series_parallel int, Series_fuse_rating varchar(20), Interconnect_material varchar(20), Interconnect_supplier varchar(20), Superstrate_type varchar(20), 
    Superstrate_manu varchar(20), Substrate_type varchar(20), Substrate_manu varchar(20), Frame_material varchar(20), Frame_adhesive varchar(20), Encapulant_type varchar(20),
    Encapsulant_manu varchar(20), Junction_box_type varchar(20), Junction_box_manu varchar(20), Junction_box_adhesive varchar(20), Cable_type varchar(20), Connector_type varchar(20),
    Max_system_voltage varchar(20), Manufacturer_Location varchar(40), Manufactured_date date, Manu_name varchar(20), NOCT varchar(20), ISC varchar(20), VOC varchar(20), IMP varchar(20), 
    VMP varchar(20), FF varchar(20), PMP varchar(20),
    PRIMARY KEY(Module_number),
    FOREIGN KEY (Manu_name) REFERENCES manufacturer(Manu_name));

DROP TABLE IF EXISTS
	Bypass_diode;
CREATE TABLE Bypass_diode(
	Module_number varchar(40), Model_number varchar(20), Maximum_junc_temp varchar(20), Rating int,
	FOREIGN KEY(Module_number) REFERENCES PVmodule(Module_number));

DROP TABLE IF EXISTS
	Testing_lab;
CREATE TABLE Testing_lab(
	Lab_name varchar(20) NOT NULL, Contact_address varchar(40), Contact_phone varchar(20), Contact_email varchar(20),
	PRIMARY KEY (Lab_name));
   
/*The middle table between PVModule and Testing_lab*/
DROP TABLE IF EXISTS
	test;
CREATE TABLE test(
	Module_number varchar(40), Lab_name varchar(20), Test_date date, Tester_name varchar(20), NOCT int, ISC int, VOC int, PMP int, FF int, VMP int, IMP int, Verdict varchar(10),
    FOREIGN KEY (Module_number) REFERENCES PVModule(Module_number),
    FOREIGN KEY (Lab_name) REFERENCES Testing_lab(Lab_name));

/*Middle table between PVMOdule and Manufacturer*/
DROP TABLE IF EXISTS
	manu_middle;
CREATE TABLE manu_middle(
	Module_number varchar(40), Manu_name varchar(40), Manufacturer_location varchar(40), Manufatured_date date,
    FOREIGN KEY (Module_number) REFERENCES PVModule(Module_number),
    FOREIGN KEY (Manu_name) REFERENCES Manufacturer(Manu_name));