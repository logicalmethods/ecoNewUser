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



from httplib2 import Http
from urllib import urlencode


def mkAD()

def mkBasecamp()

def mkSocialcast()
	httpCall = Http()
	data = dict(name="Joe", comment="A test comment")
	resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
	resp