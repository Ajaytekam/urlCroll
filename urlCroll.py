#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

def Banner():
    print(f"Usage : {sys.argv[0]} <url>")
    return 
    sys.exit(1)

def getUrl(url):
    siteD = BeautifulSoup(requests.get(url).content, "html.parser")
    base_url = base_url = url.rsplit('/', 1)[0]+"/"
    for a_tag in siteD.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        else:
            print(base_url+href)

def main():
    if len(sys.argv) != 2:
        Banner()
    else:
        getUrl(str(sys.argv[1]))

if __name__ == "__main__":
    main()
