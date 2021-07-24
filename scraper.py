import csv
from bs4 import BeautifulSoup
import requests

csv_file = open('Linkin_Park.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Album','Year of Release', 'Songs'])

source = requests.get('https://www.discogs.com/artist/40029-Linkin-Park').text

soup =  BeautifulSoup(source, 'lxml')

albums = soup.find_all(class_="title")
index = [0,4,5,8,11,12]
a = []
for i in index:
	a.append(albums[i])
	
for album in a:
	
	link =  requests.get("https://www.discogs.com/" + album.a['href']).text
	linkSoup = BeautifulSoup(link, 'lxml')
	year = linkSoup.find_all(class_="content")[2].a.text
	csv_writer.writerow([album.a.text, year,''])
	songs = linkSoup.find_all('span', class_="tracklist_track_title")
	for song in songs:	
		csv_writer.writerow(['', '',song.text])
	csv_writer.writerow(['', '', ''])

csv_file.close()
print("Done.")
