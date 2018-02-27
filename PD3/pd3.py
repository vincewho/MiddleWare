#!/usr/bin/env python

import csv, sys
from collections import defaultdict

class importResults(object):

    def __init__(self, model='',test_seq='',condition='',date='',isc='',voc='',imp='',vmp='',ff='',pmp=''):
    	self.__model = model
    	self.__test_seq = test_seq
    	self.__condition = condition
    	self.__date = date
    	self.__isc = isc
    	self.__voc = voc
    	self.__imp = imp
    	self.__vmp = vmp
    	self.__ff = ff
    	self.__pmp = pmp
     
    def setModel(self, var1):
      self.__model = var1

    def setTest_seq(self, var2):
    	self.__test_seq = var2
    
    def setCondition(self, var3):
    	self.__condition = var3
    	
    def setDate(self, var4):
    	self.__date = var4
    	
    def setIsc(self, var5):
    	self.__isc = var5
    	
    def setVoc(self, var6):
    	self.__voc = var6
    	
    def setImp(self, var7):
    	self.__imp = var7
    	
    def setVmp(self, var8):
    	self.__vmp = var8
    	
    def setFF(self, var9):
    	self.__ff = var9
    	
    def setPmp(self, var10):
    	self.__pmp = var10
    	
    # getters
    def getModel(self):
    	return self.__model
    
    def getTest_seq(self):
    	return self.__test_seq
    
    def getCondition(self):
    	return self.__condition
    
    def getDate(self):
    	return self.__date
    
    def getIsc(self):
    	return self.__isc
    	
    def getVoc(self):
    	return self.__voc
    
    def getImp(self):
    	return self.__imp
    
    def getVmp(self):
    	return self.__vmp
    
    def getFF(self):
    	return self.__ff
    
    def getPmp(self):
    	return self.__pmp
  
#  	def makeDict(self, data):

def main():

  filename = sys.argv[1]
  infile = open('test_results.csv', 'r')
  data = csv.DictReader(infile)
  s=[]
  i = 0  
  
  for record in data:
    s.insert(i, importResults(record['Model'], record['Test Sequence'], record['Condition'], record['Date'], record['Isc'], record['Voc'], record['Imp'], record['Vmp'], record['FF'], record['Pmp']))
    i += 1
  
  sys.stdout.write("Model\tTest_Sequence\tCondition\tDate\tISC\tVOC\tIMP\tVMP\tFF\tPMP\n")      
  
  for i in range(len(s)):
    sys.stdout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (s[i].getModel(),s[i].getTest_seq(),s[i].getCondition(),s[i].getDate(),s[i].getIsc(),s[i].getVoc(),s[i].getImp(),s[i].getVmp(),s[i].getFF(),s[i].getPmp()))
    #sys.stdout.write('%s\t%s\n' % (s[i].getModel(), s[i].getTest_seq()))
#########################################################
main()
