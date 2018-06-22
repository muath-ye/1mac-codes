from urllib import request , parse

def read_text():
   	file_open = open("readTest.txt",mode='r')
	file_contant=file_open.read()
	print (file_contant)
	file_open.close()
   
	check_profanity(file_contant)

def check_profanity(text_to_check):
	#lib from outside python27 lib folder
	url='http://www.wdylike.appspot.com/?q='
	url=url+parse.quote(text_to_check)
	connection=request.urlopen(url)
	output=connection.read()
	print(output)
	connection.close()
	
	if b'true' in output :
		print("Profanity Alert!")
	elif b'False' in output :
		print("This document has no curse words")
	else:
		print("Could not scan document.")	
read_text()