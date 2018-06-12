
import requests
from bs4 import BeautifulSoup


 # 17328 9dcc11f04d350a593ce36298c6690b7792a3bbfcb2c68a1f6b4ed97241b576e7
c = '17328'
s = '9dcc11f04d350a593ce36298c6690b7792a3bbfcb2c68a1f6b4ed97241b576e7'
r = requests.post('http://104.199.235.135:31332/_hidden_flag_.php',data={'c':c,'s':s})
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
		break

# print(c,s)

# print(r.headers)
# print(r.text)
# 