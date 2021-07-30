import csv, time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')

start = time.time()

csv_file = open('covid19India.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['State' , 'Confirmed' , 'Active', 'Recovered', 'Deceased', 'Tested' ,'Vaccine Doses Administered'])

url = 'https://www.covid19india.org'
browser = webdriver.Chrome('/Users/priyanshvyas/Downloads/chromedriver' , options= options)
browser.get(url)
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html , 'html.parser')

row = soup.find_all(class_="row")
a = []
for i in range(1,38):
	a.append(row[i])

for place in a:
	state = place.find(class_="state-name").text
	statistic = place.find_all(class_="total")
	confirmed = statistic[0].text
	active = statistic[1].text
	recovered = statistic[2].text
	deceased = statistic[3].text
	tested = statistic[4].text
	vaccine = statistic[5].text
	csv_writer.writerow([state, confirmed,active,recovered ,deceased ,tested, vaccine])

csv_file.close()
end = time.time()
done = int((end-start)*100)/100
print("Done in " + str(done) + " seconds.")