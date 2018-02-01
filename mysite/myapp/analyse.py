import sys
import os
import time
import re

# Constant Strings
dx_list = list()
class logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "ab+")

def analyseEngine (path,dbData):
    #print ("Finding for " + path)
    # read file from path and load in ram
    #fp = open(path, 'r')
    #fileData = fp.read()
    #fp.close()
    #fileData.decode('utf-8')
   
    #Create a RX class object
    rxContext = analyseRX(dbData) 
    for rule in (dbData):
        #searchString=rule['RuleString']
        #Search every rule now
        rxContext.matchRule(rule,path)

    #for line in rxContext.match_plugin:
        #print "######################################"
        #print "Proudct is   : %s" % line['product']
        #print "Description  : %s" % line['description']
        #print "Bug ID       : %s" % line['bug_id']
        #print "RCA          : %s " % line['rca']
        #print "Filename     : %s" % line['filename']
        #print "######################################"
    return rxContext

class analyseRX(logger):
    def __init__(self, dbData=''):
        self.platform = ""
        self.release = ""
        self.version = ""
        self.uptime = ""
        self.match_plugin=list()
        self.platform = '10RX'
        self.xdata = '' #Any extra information to be displayed
        self.dbRules = dbData

    def matchRule(self,rule,filename):
        #
        # Search in complete file
        pattern=rule['RuleString']
        #pattern="Error"
        #pattern=rule
        for i, line in enumerate(open(filename)):
            for match in re.finditer(pattern, line):
               #print 'Found on line %s: %s' % (i+1, match.groups())
               d={}
               d['rule_id']= rule['ID']
               d['bug_id']=rule['BugID']
               d['product']= rule['Product']
               d['description'] ="description" #rule['description']
               d['rca'] = rule['RCA']
               d['workaround'] = "TEST" #rule['workaround']
               d['filename'] = filename 

               #append it to matchplugin list
               self.match_plugin.append(d)


    def checkFailure(self,data):
        status = data.find(".*ailure")
        print "\nstatus in checkFailure is %s\n" %status
        return status


    def checkError(self,data):
        status = data.find('Error')
        return status

    def checkVersion(self,filename):
        data.strip()
        log = data.split('\n')
        str1 = log[8].split(':')
        str2 = str1[1].split(' ')
        self.platform = str2[1].strip()
        self.release = str2[2].strip()
        str3 = str2[3].split('(')
        str4 = str3[1].split(')')
        self.version = str4[0].strip()
        #print self.release
        #print self.version 
        #print self.platform
        self.release = self.release
        self.version = self.version 
        self.platform = self.platform
