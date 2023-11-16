import os
import hashlib

def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		lastid = result.id
		newid = lastid + 1
	else:
		lastid = 0
		newid = 1
	return lastid, newid
def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()

def getjustnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
	else:
		newid = 1
	return newid

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

def split_string(string):
	string2 = string.split()
	return string2[0].lower()

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

      R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c

def getNewKPJMemberAccount(table_name):
	result = table_name.objects.last()
	if result:
		numeruKontaFoun = result.memberAccountNumber
		newNumber = numeruKontaFoun.split("-")
		newid = int(newNumber[1])+1
		if len(str(newid)) == 1:
			newid = "KPJ-00000"+str(newid)
		elif len(str(newid)) == 2:
			newid = "KPJ-0000"+str(newid)
		elif len(str(newid)) == 3:
			newid = "KPJ-000"+str(newid)
		elif len(str(newid)) == 4:
			newid = "KPJ-00"+str(newid)
		elif len(str(newid)) == 5:
			newid = "KPJ-0"+str(newid)
		elif len(str(newid)) == 6:
			newid = "KPJ-"+str(newid)
		newNumber = newid
	else:
		newNumber = "KPJ-000001"

	return newNumber

def getMonthDireffence(date1,date2,totalFulanSelu):
	month = (date2.year - date1.year)*12 + (date2.month - date1.month)
	return abs(month) - totalFulanSelu

def getdatedifferencebymonth(date1,date2):
	month = (date2.year - date1.year)*12 + (date2.month - date1.month)
	return abs(month)

def getFulanNaran(num):
	if num == 1:
		month = "Janeiru"
	if num == 2:
		month = "Fevreiru"
	if num == 3:
		month = "Marsu"
	if num == 4:
		month = "Abril"
	if num == 5:
		month = "Maiu"
	if num == 6:
		month = "Junhu"
	if num == 7:
		month = "Julhu"
	if num == 8:
		month = "Agustu"
	if num == 9:
		month = "Setembru"
	if num == 10:
		month = "Outubru"
	if num == 11:
		month = "Novembru"
	if num == 12:
		month = "Dezembru"
	return month


		