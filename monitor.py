import json
import os.path
import base64
import os

def checkfile():
    File = os.path.exists("settings.json")
    if File == True:
        analyzefile()
    else:
        createfile("off","off","off","bnVsbA==")  
        analyzefile()  

def analyzefile():
    with open('settings.json') as configure_file:
        data = json.load(configure_file)
        notice = data['notifications']
        username = data['username']
        telephone = data['telephone']
        key = data['key']
        codes = base64.b64decode(key) 
        keys = codes.decode()
        if telephone == keys:
            return True
        elif telephone != keys:
            return False        

def createfile(notice,user,telephon,code):
    settings = {
        "notifications" : notice,
        "username" : user,
        "telephone" : telephon,
        "key" : code
    }     
    json_object = json.dumps(settings,indent=4)
    with open("settings.json", "w") as outfile:
        outfile.write(json_object)   

def getNotice(): 
    File = os.path.exists("settings.json")
    if File == True:
        with open('settings.json') as configure_file:
            data = json.load(configure_file)
            notice = data['notifications']
            return notice 
    else:          
        createfile("off","off","off","bnVsbA==")

def getUser(): 
    with open('settings.json') as configure_file:
        data = json.load(configure_file)
        username = data['username']
        return username

def getTele(): 
    with open('settings.json') as configure_file:
        data = json.load(configure_file)
        telephone = data['telephone']
        return telephone  

def getKey(): 
    with open('settings.json') as configure_file:
        data = json.load(configure_file)
        key = data['key']
        return key    