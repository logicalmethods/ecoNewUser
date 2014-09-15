"""
This code hacked together by Alex Speaks : @logicalmethods : alex@sneaksneak.org
It's my first python script.. be gentle.

new user creation script for Ecotrust
-------------------------------------

does:
*creates users in AD 
*adds them to everybody and development_ro and terra access
*adds user to home folder

to do:
* read CSV of user names and attributes
* add ad user to optional groups from config file
* set appropriate attributes to AD user: manager,  
* create social cast user
* create mediawiki user
* create resource space user
* create basecamp user?
* create google apps user
* create o365 user
* create user in GLPI
* assign user to computer in GLPI
* option : create mailbox?
* option : create linux dev boxen user?
* generate safe password and save it somewhere

config file format:
{
"firstName":"Jon",
"lastName":"Doe",
"userName":"jdoe",
"groups":["mis","ncc"],
"socialcastP":true,
"basecampP":true,
"company":"Ecotrust",
"temporary":true,
"manager":"aspeaks",
"description":"just this guy, you know?"
}


"""


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
	addToGrp("everybody", userData["firstName"]+" "+userData["lastName"])
	addToGrp("development_ro", userData["firstName"]+" "+userData["lastName"])
	addToGrp("development_ro", userData["firstName"]+" "+userData["lastName"])
	addToGrp("terra access", userData["firstName"]+" "+userData["lastName"])
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
