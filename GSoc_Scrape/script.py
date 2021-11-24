import requests,csv,time
from bs4 import BeautifulSoup

start = time.time()
csv_file = open('GSoc_Org.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Index','Name', 'Link'])
baseLink = "https://summerofcode.withgoogle.com"

def geturl(year):
    return "https://summerofcode.withgoogle.com/archive/"+year+"/organizations/"

def req(url):
    source = requests.get(url).text
    return source

def soup(source):
    soup = BeautifulSoup(source, 'lxml')
    return soup

def findName(soupname):
    card = soupname.find_all(class_="organization-card__name")
    return card

def findCard(soupname):
    card = soupname.find_all(class_="organization-card__container")
    return card

p2021 = []
p2020 = []
p2019 = []
p2018 = []
commonName = []
i = 1

for a in findName(soup(req(geturl("2018")))):
    p2018.append(a.text)
    
for a in findName(soup(req(geturl("2019")))):
    p2019.append(a.text)

for a in findName(soup(req(geturl("2020")))):
    p2020.append(a.text)

for a in findName(soup(req(geturl("2021")))):
    p2021.append(a.text)

for a in findName(soup(req(geturl("2021")))):
    orgname = a.text
    if p2018.count(orgname) and p2019.count(orgname) and p2020.count(orgname):
        commonName.append(orgname)

for link in findCard(soup(req(geturl("2021")))):
    if commonName.count(link.find(class_="organization-card__name").text):
        name = link.find(class_="organization-card__name").text
        href = link.find(class_="organization-card__link")['href']
        csv_writer.writerow([i,name,baseLink + href])
        i+=1

csv_file.close()
end = time.time()
print("Done in",end-start,"seconds.")