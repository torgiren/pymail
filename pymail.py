#!/usr/bin/env python
#*-* coding: utf8 *-*
from interface import Interface
from mail import Mail
import email
import email.header
plik = open('config.cfg')
cfg = plik.readlines()
plik.close()
config={}
for i in cfg:
	j = i.split('=')
	print j
	if len(j) == 2:
		config[j[0].rstrip().lstrip()] = j[1].lstrip().rstrip()
m = Mail()
m.login(config['login'],config['passwd'])
print m.list_folders()
m.select()
x = m.fetch_all_mail()
x = ",".join(x.split())
h =  m.get_header(x)
for i in h:
	i = email.header.decode_header(i.replace('\r\n','\n'))
	i = " ".join([j[0] for j in i])
	print i
	#e =  email.Header.decode_header(i)[0][0]
	#print e
	#print "%s\n%s\n%s\n%s\n\n" % (e['DATE'],e['FROM'],email.utils.parseaddr(e['TO']), e['SUBJECT'])
	print "-------------------"
