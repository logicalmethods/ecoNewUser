from pyad import *	#for interacting with AD
import json		#for reading and writing json
import urllib2		#for parsing URLs
import argparse		#for reading the command line arguments
#from httplib2 import Http

def readWorkFile(fileName): #opens the to-do file and returns a json object of the things we should be doing
	f = open(fileName, "r")
	work = json.load(f)
	return(work)


def mkAD(userData): #create an ecotrust standard AD user
	ou = pyad.adcontainer.ADContainer.from_dn("OU=employees,OU=ecotrust,DC=ecotrust,DC=org")
	c = pyad.aduser.ADUser.create(name = userData["firstName"]+" "+userData["lastName"], container_object=ou, password=pwgen(), upn_suffix=None, enable=True, optional_attributes=dict(description = userData["description"], givenName = userData["firstName"], sn=userData["lastName"],displayName=userData["firstName"]+" "+userData["lastName"],sAMAccountName=userData["userName"],userPrincipalName=userData["userName"]+"@ecotrust.org", homeDirectory="\\\\daryl\\users\\"+userData["userName"],homeDrive="u:"))
	#addToGrp("everybody", userData["firstName"]+" "+userData["lastName"])
	#addToGrp("development_ro", userData["firstName"]+" "+userData["lastName"])
	#addToGrp("development_ro", userData["firstName"]+" "+userData["lastName"])
	#addToGrp("terra access", userData["firstName"]+" "+userData["lastName"])
	for i in userData[groups]
		addToGrp(i,userData["firstName"]+" "+userData["lastName"])
	return(c.displayName)


def addToGrp(groupName, fullName):	#add a specified user to a specified AD group
	userObj = aduser.ADUser.from_dn("CN={name},OU=employees,OU=ecotrust,DC=ecotrust,DC=org".format(name=fullName))
	groupObj = adgroup.ADGroup.from_cn(groupName)
	groupObj.add_members(userObj)
	return(None)


def pwgen():	# returns a 10 character human readable password
	return("Password!")

"""
def mkBasecamp():	#make basecamp user
	return(none)


def mkSocialcast(userName):
	httpCall = Http()
	data = dict(name="Joe", comment="A test comment")
	resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
	resp

def mkGoogle(userName)
	return(None)

def mkO365(userName)
	return(None)
"""

###########################

parser = argparse.ArgumentParser()
parser.add_argument("config", help="specify the name of the json formated config file containing new user info")
args = parser.parse_args()
userData = readWorkFile(args.config)
print mkAD(userData)
