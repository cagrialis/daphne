from toolPy import terminalCommands
from subDomainPy import subDomainResearch
import writeName
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from colorama import *
from datetime import datetime
import sys
from urllib import parse
import time
import threading

NOW = datetime.utcnow().replace(microsecond=0)


class Crawler:

    def __init__(self, urls=[]):
        self.visitedUrls = []
        self.urlsToVisit = urls

    def downloadUrl(self, url):
        return requests.get(url).text

    def getLinkedUrls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def addUrlToVisit(self, url):
        if url not in self.visitedUrls and url not in self.urlsToVisit:
            self.urlsToVisit.append(url)

    def crawlAll(self, url):
        html = self.downloadUrl(url)
        for url in self.getLinkedUrls(url, html):
            self.addUrlToVisit(url)

    def run(self):
        while self.urlsToVisit:
            url = str(self.urlsToVisit.pop(0))
            if url.find(parse.urlsplit(sys.argv[1]).netloc) != -1:
                print(f"{Style.BRIGHT}[{NOW}]{Fore.GREEN}[CRAWLED URL] => {Fore.BLUE}{url}{Style.RESET_ALL}")
                with open("urls.txt", "a") as fileUrl:
                    fileUrl.write(url + "\n")
                try:
                    self.crawlAll(url)
                except Exception:
                    with open("error-logs.txt", "a") as fileError:
                        fileError.write(str(Exception.__str__) + " - " + 'Failed to crawl:' + url + "\n")
                finally:
                    self.visitedUrls.append(url)

def startProg():
    th1 = threading.Thread(target=writeName.name())
    th1.start()
    print(f"{Style.BRIGHT}Crawling Url {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(10)
    th2 = threading.Thread(target=Crawler(urls=[sys.argv[1]]).run())
    th2.start()
    print(f"\n{Style.BRIGHT}Search Subdomains {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(10)
    th3 = threading.Thread(target=subDomainResearch(sys.argv[1]))
    th3.start()
    print(f"\n{Style.BRIGHT}Start Scanning wit Tools for {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(10)
    th4 = threading.Thread(target=terminalCommands(sys.argv[1]))
    th4.start()

if __name__ == '__main__':

    try:
        startProg()
    except KeyboardInterrupt:
        print("\nExiting...")
        time.sleep(5)
