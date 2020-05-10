from googlesearch import search
import requests, sys, os
from bs4 import BeautifulSoup as bs
from requests.exceptions import SSLError

#remove
try:
	os.system('rm -rf Vuln.txt')
except IOError:
	pass

vuln=[]
urls=input('\nDork: ')
print('Scanning url ...')
if urls:
	for x in search(urls,tld='co.in',num=20,stop=20,pause=2):
		ur = x+"'"
		r = requests.get(ur)
		s = bs(r.content, 'html.parser')
		f1 = s.find_all(text=True)
		for khaz in f1:
			try:
				if khaz.find('You have an error in your SQL'):
					vuln.append(x)
					print('\rTotal Web vuln : '+str(len(vuln)),end="",flush=True)
					break
			except requests.exceptions.SSLError:
				print('Error bypass url')


	f=open('Vuln.txt','a')
	for x in vuln:
		f.write(x + '\n')
	f.close()

	print('\nFile save Vuln.txt')

