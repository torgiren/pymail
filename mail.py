#*-* coding: utf8 *-*
import imaplib
class Mail:
	def __init__(self, server='imap.gmail.com'):
		self.__mail = imaplib.IMAP4_SSL(server)
		self.__folder = None
	def login(self, user, passwd):
		self.__mail.login(user, passwd)
	def list_folders(self):
		folders = self.__mail.list()[1]
		folders = [ f.split()[2] for f in folders]	
		return '\n'.join(folders)
	def select(self, folder='inbox'):
		self.__mail.select(folder)
	def fetch_all_mail(self):
		result, data = self.__mail.uid('search', None, 'ALL')

		return data[0]
	def read_mail(self, id):
		result, data = self.__mail.fetch(id, "(RFC822)")
		return data[0][1]
	def get_header(self, id):
		result, data = self.__mail.uid('fetch', id, '(BODY[HEADER.FIELDS (DATE SUBJECT FROM TO)])')
		data = [x[1] for x in data if len(x)>1]
		return data
