# Imports
import gzip
import os.path
import os, sys
from stat import *
import stat
import glob
import shutil
import tarfile
from analyse import analyseEngine

# Globals
import ConnecttoSql

TempFilePath = r'/tmp/logs'
ERROR = -1;
OK = 1
FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL  # Refer to "man 2 open".
MODE = stat.S_IRUSR | stat.S_IWUSR  # This is 0o600 in octal and 384 in decimal.


def unzipFile(path):
    # Check Path
    if not os.path.isdir(path):
        # Open the gz file and read
        with gzip.open(path, 'rb') as in_file:
            srcFile = in_file.read()
            in_file.close()
            # Remove .gz extension
            path_to_store = path[:-3]
        with open(path_to_store, 'wb') as f:
            print("Extracting srcFile " + path_to_store)
            f.write(srcFile)
            f.close()


def checkAndExtract(logPath):
    # Create temp store
    if not os.path.exists(TempFilePath):
        os.makedirs(TempFilePath)

    # Iterate to logPath files
    if os.path.isfile(logPath) and os.access(logPath, os.R_OK):
        logTar = tarfile.open(logPath, "r:gz")
        # Extracted the tar at temp path
        try:
            logTar.extractall(path=TempFilePath)
            for filenames in logTar.getnames():
                tmpFile = TempFilePath + "/" + filenames
                print (tmpFile)
                if tmpFile.endswith('.tar.gz'):
                    print("Extracing tar " + tmpFile)
                    checkAndExtract(tmpFile)
                elif tmpFile.endswith('.gz'):
                    unzipFile(tmpFile)

            logTar.close()
            return OK
        except:
            return ERROR

    else:
        print ( "Error Log File " + logPath + " doesn't exists")
        return ERROR

    return OK


def cleanUp():
    if os.path.exists(TempFilePath):
        shutil.rmtree(TempFilePath)


def findMatchingRulesFromLog(path, dbData):
    #print ("Finding for " + path)
    # read file from path and load in ram
    #fp = open(path, 'r')
    #fileData = fp.read()
    #fp.close()
    #fileData.decode('utf-8')
    #for rule in (dbData):
	#searchString=data['RuleString']
        #rxContext = analyseRX(rule,searchString) 
	#if searchString in fileData:
	#  print( path+" found " + searchString)
    rxContext = analyseEngine(path,dbData) 
    for line in rxContext.match_plugin:
        print "######################################"
        print "Proudct is   : %s" % line['product']
        print "Description  : %s" % line['description']
        print "Bug ID       : %s" % line['bug_id']
        print "RCA          : %s " % line['rca']
        print "Filename     : %s" % line['filename']
        print "######################################"

    # print fileData


def iterateFolder(path, dbData):
    print ("In iterateFolder" + path)
    for files in os.listdir(path):
        absPathfile = path + "/" + files
        mode = os.stat(absPathfile).st_mode
        if S_ISDIR(mode):
            iterateFolder(absPathfile, dbData)
        elif S_ISREG(mode):
            if not absPathfile.endswith('.gz'):
                os.chmod(absPathfile, 777)
                findMatchingRulesFromLog(absPathfile, dbData)
        else:
            print ('Skipping %s' % absPathfile)


def getAnalysis(logPath):
    # First extract the tar and zips

    # Please check the hard coding of paths, it should be changed.........please make.....
    if OK == checkAndExtract(logPath):
        dbData = ConnecttoSql.fetchAllPLuginRows(r"/home/django/mysite/db.sqlite3")
        iterateFolder(TempFilePath, dbData)
    else:
        print ("Failed")


if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf-8')
    	cleanUp()
    	getAnalysis(r"/home/django/mysite/infocollect_12_12_2017_07_49_28.tar.gz")
    	#cleanUp()
