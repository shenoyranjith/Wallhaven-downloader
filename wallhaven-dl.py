import os
import getpass
import bs4
import re
import requests
import tqdm
import time
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

def login():
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    req = requests.post('https://alpha.wallhaven.cc/auth/login', data={'username':username, 'password':password})
    return req.cookies

def search():
    searchurl = input('Enter url: ')
    searchurl += '&page='
    return (searchurl, login())

def main():
    BASEURL, cookies = search()
    location = input('Enter path to folder where the images are to be downloaded: ')
    pgid = int(input('Enter number of pages to download: '))	
    print('Number of Wallpapers to Download: ' + str(24 * pgid))
    for j in range(1, pgid + 1):
        totalImage = str(24 * pgid)
        url = BASEURL + str(j)
        urlreq = requests.get(url, cookies=cookies)
        soup = bs4.BeautifulSoup(urlreq.text, 'lxml')
        soupid = soup.findAll('a', {'class': 'preview'})
        imgext = ['jpg', 'png', 'bmp']
        for i in range(len(soupid)):
            currentImage = (((j - 1) * 24) + (i + 1))
            currentId = str(soupid[i]['href']).rsplit('/', 1)[-1]
            subPath = currentId[:2]
            url = 'https://w.wallhaven.cc/full/%s/wallhaven-%s.' %(subPath, currentId)
            for ext in imgext:
                iurl = url + ext
                osPath = os.path.join(location, os.path.basename(iurl))
                if not os.path.exists(osPath):
                    imgreq = requests.get(iurl, cookies=cookies)
                    if imgreq.status_code == 200:
                        print("Downloading : %s - %s / %s" % ((os.path.basename(iurl)), currentImage , totalImage))
                        with open(osPath, 'ab') as imageFile:
                            for chunk in imgreq.iter_content(1024):
                                imageFile.write(chunk)
                        break
                else:
                    print("Already exists: %s %s/%s" % ((os.path.basename(iurl)),currentImage , totalImage))
if __name__ == '__main__':
    main()
