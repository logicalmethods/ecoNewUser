This code hacked together by Alex Speaks : @logicalmethods : alex@sneaksneak.org
It's my first python script.. be gentle.

new user creation script for Ecotrust
-------------------------------------

does:
*reads input from a JSON formatted text file
*creates users in AD 
*adds them to everybody and development_ro and terra access
*adds user to home folder
*adds ad user to groups from config file


to do:
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
* issue them an available license from o365

bugs:
* something about how we create the user is causing the default email address to be jane@ecotrust.org rather than jdoe@ecotrust.org

