import re 
def Local_name(local):
    if (len(local)<=64 and len(local)>0 ):
        patt =  r'^([a-z 0-9 A-Z \. \'_! # $ % & * { | } + \- = / ~]+[a-z 0-9 A-Z \. \'_! # $ % & * { | } + \- = / ~]$)'
        string = re.search(patt,local)
        if (bool(string)):
            if(local.endswith('.') or local.startswith('.')):
                return False;
            else:
                return True;
    else:
        return False;
def domin_name(domin):
    if (domin.isnumeric()):
        print("False")

    else:
        if(domin.startswith('-') or domin.endswith('-')):
            patt = '^[a-z0-9A-Z-]+ [a-z0-9A-Z-]$'
            string = re.search(patt,domin)
            if(bool(string)):
                return True;
            else:
               return False;
            
        else:
            patt = '^[a-z0-9A-Z]+[a-z0-9A-Z]$'
            string = re.search(patt,domin)
            if(bool(string)):
                return True;
            else:
                return False;
        return False;
def exten(ext):
    if (len(ext)<=3):
        special_characters = "!@#$%^&*()-+?_=,<>/.[]:;{|}"
        if any(spc in special_characters for spc in ext):
            return False;
        else:
            return True;
    else:
        return False;
email = input("enter your email :")
local = email.split('@')[0]  #provide local 
ext = email.split('.',1)[1] #provide you the extension
a = email.split("@")[1]
domin = a.split('.')[0] #Provide the domin
if(Local_name(local) and domin_name(domin) and exten(ext)):
    print("True")
else:
    print("False")
