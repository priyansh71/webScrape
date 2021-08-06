import requests, csv
from bs4 import BeautifulSoup

csv_file = open('courses.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Course Title','Course Website', 'Video Availability'])

url1 = "https://www.classcentral.com/report/stanford-on-campus-courses/"
source = requests.get(url1).text
soup =  BeautifulSoup(source, 'lxml')

lister = soup.find(class_="wysiwyg")
uls = lister.find_all('ul')
for ul in uls:
	items = ul.find_all('li')
	for item in items:
		if item.a.text[0] == 'C':
			title = item.a.text
			avail = "No"
		else:
			title = item.a.text[1:-1]
			avail = "Yes"
		link = item.a['href']
		csv_writer.writerow([title, link, avail])


csv_file.close()