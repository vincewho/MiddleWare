drop database iadb;
create database iadb;
use iadb;

CREATE TABLE IF NOT EXISTS Benefit (
					productID VARCHAR(60) PRIMARY KEY NOT NULL,
					productName VARCHAR(60),
					description VARCHAR(60),
					monthlyPrice FLOAT,
					company VARCHAR(60)		
					);

CREATE TABLE IF NOT EXISTS BenefitAdmin (
					parentID VARCHAR(60) PRIMARY KEY NOT NULL,
					parentName VARCHAR(60)
					);

CREATE TABLE IF NOT EXISTS Employer (
					clientID VARCHAR(10) PRIMARY KEY NOT NULL,
					parentID VARCHAR(60),
					FOREIGN KEY (parentID) REFERENCES BenefitAdmin (parentID), 
					clientName VARCHAR(60)
					);

CREATE TABLE IF NOT EXISTS Subscriber (
					subID INT NOT NULL AUTO_INCREMENT,
					PRIMARY KEY (subID),
					familyID VARCHAR(60),
					uniqueID VARCHAR(60) NOT NULL,
					employeeID VARCHAR(60) NOT NULL,
					relationship CHAR(60),
					SSN VARCHAR(60) NOT NULL, 
					firstName VARCHAR(60), 
					middleName VARCHAR(60), 
					lastName VARCHAR(60),
					payFrequency INT,
					dayOfBirth INT, 
					monthOfBirth VARCHAR(60), 
					yearOfBirth INT,
					address1 VARCHAR(60), 
					address2 VARCHAR(60), 
					city VARCHAR(60), 
					zipCode VARCHAR(60), 
					state VARCHAR(60), 
					areaCode VARCHAR(60), 
					homePhone VARCHAR(60), 
					email VARCHAR(60),
					employmentStatus VARCHAR(60),
					clientID VARCHAR(10),
					FOREIGN KEY (clientID) REFERENCES Employer(clientID),
					productID VARCHAR(60),
					FOREIGN KEY (productID) REFERENCES Benefit(productID),  
					effectiveDate DATE,
					deductionMethod VARCHAR(60)
					);

CREATE TABLE IF NOT EXISTS Enrollment (
					fileName VARCHAR(60) NOT NULL,
					clientID VARCHAR(10),
					FOREIGN KEY (clientID) REFERENCES Employer(clientID),
					dateSubmitted DATE,
					numberOfRecords INT,
					enrollmentStatus VARCHAR(60)
					);

CREATE TABLE IF NOT EXISTS Payment (
					paymentFileName VARCHAR(60) NOT NULL,
					subID INT NOT NULL AUTO_INCREMENT,
					FOREIGN KEY (subID) REFERENCES Subscriber(subID),
					clientID VARCHAR(10),
					FOREIGN KEY (clientID) REFERENCES Employer(clientID),
					paymentSubmitted DATE NULL DEFAULT NULL,
					deductionDate DATE NULL DEFAULT NULL,
					deductionCollected FLOAT NULL DEFAULT NULL,
					deductionAttempted FLOAT NULL DEFAULT NULL,
					status VARCHAR(60)	
					);

