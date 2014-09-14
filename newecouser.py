"""
This code hacked together by Alex Speaks : @logicalmethods : alex@sneaksneak.org
It's my first python script.. be gentle.

new user creation script for Ecotrust
-------------------------------------

does:
*creates users in AD 

to do:
* read CSV of user names and attributes
* add ad user to appropriate groups: default: domain users, everybody, development_ro
* set appropriate attributes to AD user: manager, home folder: u: \\daryl\users\jdoe, 
* create social cast user
* create mediawiki user
* create resource space user
* create basecamp user?
* create user in GLPI
* assign user to computer in GLPI
* option : create mailbox?
* option : create linux dev boxen user?

config file format:
{
"fullName":"JOHN DOE",
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


def mkAD(userData):
	ou = pyad.adcontainer.ADContainer.from_dn("OU=employees,OU=ecotrust,DC=ecotrust,DC=org")
	c = pyad.aduser.ADUser.create(name = userData["userName"], container_object=ou, password=pwgen(), upn_suffix=None, enable=False, optional_attributes=dict(description = userData["description"]))
	addToGrp("everybody", userData["fullName"])
	return(c.displayName)


def addToGrp(groupName, fullName):	#add a specified user to a specified AD group
	uesrObj = aduser.ADUser.from_dn("CN={name},OU=employees,OU=ecotrust,DC=ecotrust,DC=org".format(name=fullName))
	groupObj = adgroup.ADGroup.from_dn("CN={group},OU=Lists,DC=ecotrust,DC=org".format(group=groupName))
	groupObj.add_members(userObj)
	return(none)


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
"""

###########################

parser = argparse.ArgumentParser()
parser.add_argument("config", help="specify the name of the json formated config file containing new user info")
args = parser.parse_args()
userData = readWorkFile(args.config)
print mkAD(userData)
