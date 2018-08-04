
import requests
from bs4 import BeautifulSoup

r = requests.post('http://104.199.235.135:31332/_hidden_flag_.php')



while True:
	soup = BeautifulSoup(r.text, 'html.parser')
	input_tags = soup.find_all('input')
	for index,tag in enumerate(input_tags):
		# print(tag.get('value'),end=" ")
		if index==0:
			c = tag.get('value')
		else:
			s = tag.get('value')
	# print(c,s)
	print(c)
	r = requests.post('http://104.199.235.135:31332/_hidden_flag_.php',data={'c':c,'s':s})
	# print(r.text)
	# if r.headers['Flag'] == "AIS3{NOT_A_VALID_FLAG}":
		# print('not ans')
	if r.headers['Flag'] != "AIS3{NOT_A_VALID_FLAG}":
		print(r.headers['Flag'])

# print(c,s)

# print(r.headers)
# print(r.text)
# 