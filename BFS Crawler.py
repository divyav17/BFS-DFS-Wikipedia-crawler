import requests
from bs4 import BeautifulSoup
import re
import time

def my_crawler(seed):
#List_of_links is store links that are extracted on a page
 List_of_links = []
 parent_list = []
 child_list = []
 parent_list.append(seed)
 count = 1
 depth = 1
 x =0
 while (len(parent_list) < 1000):
 #	print(depth)
 	if (depth >= 7):
 	 break
 	List_of_links = go_crawl(parent_list[x])
 	for i in List_of_links:
 		if i not in child_list:
 			child_list.append(i)
 	for j in child_list:
 		if j not in parent_list and len(parent_list) < 1000:
 	    	 parent_list.append(j)
 	    	 count = count+1
 	if (len(child_list) == count):
 		child_list = []
 		depth = depth + 1
 #		print(depth)
 	x = x + 1	
 #for testing purposes
 #print(parent_list[0])
 #print(len(parent_list))
 #Writing to file
 number = 1
 f = open('Task-1-E-URLs.txt', 'w')
 for i in parent_list:
     row =  str(number) + " " + str(i) + "\n"
     f.write(row)
     number += 1
 f.close()


def go_crawl(url):
 #Respecting the politeness policy
 time.sleep(1)
 wikistring = "https://en.wikipedia.org"
 totallinks, child_links = [], []
 seedinfo = requests.get(url)
 raw_data = seedinfo.text
 soup = BeautifulSoup(raw_data, 'html.parser')
 body_content = soup.find('div', {'id': 'mw-content-text'})
 #Remove Thumbnails and links below images
 if len(soup.find('div',{'class':'thumbcaption'}) or ()) > 1:
        soup.find('div', {'class':'thumbcaption'}).decompose()
 #Remove vertical Navigation box on the right
 if len(soup.find('table',{'class':'vertical-navbox nowraplinks hlist'}) or ()) > 1:
        soup.find('table', {'class':'vertical-navbox nowraplinks hlist'}).decompose()
 #Remove vertical Navigation box on the right
 if len(soup.find('table',{'class':'vertical-navbox nowraplinks'}) or ()) > 1:
        soup.find('table', {'class':'vertical-navbox nowraplinks'}).decompose()
 #Removing refrences
 if len(soup.find('ol', class_='references') or ()) > 1:
 	soup.find('ol', class_='references').decompose()

 for link in body_content.find_all('a', {'href': re.compile("^/wiki")}):
     if ':' not in link.get('href'):
         link_text = wikistring + link.get('href')
         refine_text = link_text.split('#')
         totallinks.append(str(refine_text[0]))
 for i in totallinks:
    if i not in child_links:
        if len(i) > 1:
            child_links.append(i)
 return child_links


my_crawler('https://en.wikipedia.org/wiki/Tropical_cyclone')	
 	
# 	while (Depth < 6):
    # print("this is length of frontier_list")
    # print(len(frontier_list))
    # print("this is initial x")
    # print(x)
    # k = j
    # List_of_links = pg_crawler(frontier_list[x + 0])
    # print("this is children")
    # print(List_of_links)
    # while (List_of_links > 1):
    # 	j = j + 1
    # 	List_of_links = List_of_links - 1
    # x = j 
    # a = j - k 
    # while (a >= 1):
    # 	 a = a -1
    #  	 x = x -1
    # print("this next is x")
    # print(x)