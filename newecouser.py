"""
This code hacked together by Alex Speaks : @logicalmethods : alex@sneaksneak.org
It's my first python script.. be gentle.

new user creation script for Ecotrust
-------------------------------------

does:
* nothing (atm)

to do:
* create AD user
* create social cast user
* create mediawiki user
* create resource space user
* create basecamp user?
* create user in GLPI
* assign user to computer in GLPI
* option : create mailbox?
* option : create linux dev boxen user?
"""


from pyad import *
#from httplib2 import Http
#from urllib import urlencode


def mkAD(username):
	ou = pyad.adcontainer.ADContainer.from_dn("OU=folder redirection,OU=employees,OU=ecotrust,DC=ecotrust,DC=org")
	c = pyad.aduser.ADUser.create(name = username, container_object=ou, password=pwgen(), upn_suffix=None, enable=True, optional_attributes=dict(description = "new user"))
	return c.displayName
	'''	pyad.from_dn("CN=Ryan Genuson,OU=point97,DC=ecotrust,DC=org")	
	newuser=pyad.aduser.ADUser('aspeaks')
	#date=newuser.get_password_last_set()
	#return date
'''

def pwgen():
	return("Password!")

print mkAD("aaron test")

#def mkBasecamp()

"""
def mkSocialcast()
	httpCall = Http()
	data = dict(name="Joe", comment="A test comment")
	resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
	resp
"""