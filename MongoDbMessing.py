import pymongo

client = pymongo.MongoClient("URL",PORT)
db = client.dbname

coll = db.my_collection #the collection of objects

#ChalupaCity Junk

m = '''
URI = "mongodb://admin:chalupacity@ds041651.mongolab.com:41651/rufound"
client = MongoClient(URI)
db = client.rufound
collection = db.namelist
firstname = ""
middlei = ""
lastname = ""
emailarray = []
namearray = []



def dbInsert(name, email, url):
    global collection
    collection.insert({"name" : name, "email" : email, "url": url})
def verify():
	global firstname
	global middlei
	global lastname
	global name

	name = firstname + " " + middlei + " " + lastname
	
	matches = db.namelist.find_one({"name" : name}) 
	if matches == None:
		return False 
	else:
		return True

def getMatches():
	matches = db.namelist.find({"name" : name})
	return matches

'''
