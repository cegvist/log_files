from bs4 import BeautifulSoup
import requests
query = input('What are you searching for?:   ' )
url ='http://www.google.com/search?q='
page = requests.get(url + query)
soup = BeautifulSoup(page.text)
h3 = soup.find_all("h3",class_="r")
for elem in h3:
	elem=elem.contents[0]
	link=("https://www.google.com" + elem["href"])
	print(link)
