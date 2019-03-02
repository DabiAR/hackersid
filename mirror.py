import requests
import re
import sys, os, time

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def banner():
	print ("""
\033[32m
┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐┬┌┬┐  ┌┐┌┌─┐┌┬┐┬┌─┐┬┌─┐┬─┐
├─┤├─┤│  ├┴┐├┤ ├┬┘└─┐│ ││  ││││ │ │ │├┤ │├┤ ├┬┘
┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─└─┘┴─┴┘  ┘└┘└─┘ ┴ ┴└  ┴└─┘┴└─ 
\033[36m cOd3d By : Dabi    -    Pirates Crew   - Fa Haxor - Rai Haxor - Vanda The God                                                                                                                                     
""")

def menu():
	print ("""
	[1] Single Notifier
	[2] Mass Notifier
	""")

class single:
	def __init__(self):
		self.url2 = 'https://hackersid.com/mass'
		self.nick2 = input("Ur Nick => ")
		self.team2 = input("Ur Team")
	def zekkel(self):
		try:
			self.listt2 = input("masukan url => ")
			data2 = {'hacker':self.nick2,
		 	 		 'team':self.team2,
					 'uri':self.listt2,
					 'poc':'SQL Injection',
			 		 'reason':'Heh...just for fun!',
			 		 'submit':'submit'
					 }
			zeze = requests.post(self.url2, data=data2).text
			if "success" in zeze:
				print ("\033[36m{} --> sukses".format(self.listt2))
			else:
				print ("\033[0;33m{} --> Gagal".format(self.listt2))
				
		except KeyboardInterrupt:
			print ("CTRL + C")


class dabi:
	def __init__(self):
		self.url1 = 'https://hackersid.com/mass'
		self.nick = input("Your Nick => ")
		self.team = input("Your Team => ")
	def anggi(self):
		try:
			self.listt = input("Your List => ")
			z = open(self.listt,'r').readlines()
			for mpp in z:
				anjing = mpp.strip()
				data1 = {'hacker':self.nick,
		 	 			 'team':self.team,
						 'uri':anjing,
						 'poc':'SQL Injection',
			 		 	 'reason':'Heh...just for fun!',
			 		 	 'submit':'submit'
						 }
				az = requests.post(self.url1, data=data1).text
				if "success" in az:
					print ("\033[36m{} --> sukses".format(anjing))
				else:
					print ("\033[0;33m{} --> Gagal".format(anjing))
		except KeyboardInterrupt:
			print ("CTRL + C")

if __name__ == "__main__":
	os.system('clear')
	banner()
	menu()
	nyan = input("Choose => ")
	if nyan == '1':
		tangtung = single()
		tangtung.zekkel()
	elif nyan == '2':
		vektor = dabi()
		vektor.anggi()


